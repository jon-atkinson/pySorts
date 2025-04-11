import os
from typing import List

import redis
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import core.backend_config as config
import sorter.sorter as sorter
from core.arrays import deep_copy
from core.db_interface import Database

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)

db = Database(
    namespace="comparisons",
    client=redis.StrictRedis(host=redis_host, port=int(redis_port), db=0),
)


class Algorithm(BaseModel):
    algorithm: str
    language: str


class CompareAlgorithmsRequest(BaseModel):
    algorithms: List[Algorithm]
    low: int = 0
    high: int = 10000
    arr_type: str = "random"
    num_reps: int = 1
    step: int = 1


class CompareSortednessRequest(BaseModel):
    algorithm: Algorithm
    low: int = 0
    high: int = 10000
    arr_types: List[str] = ["random"]
    num_reps: int
    step: int = 1


class DataPoint(BaseModel):
    length: int
    time: float


class Series(BaseModel):
    label: str
    data: List[DataPoint]


class ComparisonResult(BaseModel):
    id: str
    description: str
    results: List[Series]


app = FastAPI()

app.db = db

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/config")
async def get_config():
    """
    Exposes configured algorithms, implemented languages and input array types.

    Returns:
        dict: keys=algorithms, array types
    """

    return {
        "algorithms": {
            language: list(algorithms.keys())
            for language, algorithms in config.algorithms.items()
        },
        "array types": list(config.arrays.keys()),
    }


@app.get("/algorithms")
async def get_algorithms():
    """
    Return the algorithms configured in all supported languages
    """
    return {
        language: list(algorithms.keys())
        for language, algorithms in config.algorithms.items()
    }


@app.get("/arrays")
async def get_arrays():
    """
    Return the arrays configured
    """
    return list(config.arrays.keys())


@app.post("/compare-algorithms")
async def compare_algorithms(request: CompareAlgorithmsRequest):
    """
    Compare sorting algorithms and return time taken to run for a range of input lengths
    """

    algorithms = request.algorithms
    low = request.low
    high = request.high
    arr_type = request.arr_type
    num_reps = request.num_reps
    step = request.step

    if arr_type not in config.arrays:
        raise HTTPException(
            status_code=400, detail=f"Unsupported array type {arr_type}"
        )

    results = {
        (algorithm.algorithm, algorithm.language): [] for algorithm in algorithms
    }
    array_generator = config.arrays[arr_type]

    for current_length in range(low, high + 1, step):
        current_round = {
            (algorithm.algorithm, algorithm.language): [] for algorithm in algorithms
        }

        for _ in range(num_reps):
            array = array_generator(current_length)

            for algorithm in algorithms:
                copy_array = deep_copy(array)
                _, time = sorter.call(
                    algorithm.algorithm,
                    algorithm.language,
                    copy_array,
                )
                current_round[(algorithm.algorithm, algorithm.language)].append(time)

        for (algorithm, language), timing in current_round.items():
            average_time = sum(timing) / len(timing)
            results[(algorithm, language)].append((current_length, average_time))

    reformatted = {
        "type": "algorithm",
        "data_series": [
            {
                "algorithm": algorithm,
                "language": language,
                "array_type": arr_type,
                "data": series,
                "repeats": num_reps,
            }
            for (algorithm, language), series in results.items()
        ],
    }

    app.db.store_comparison(reformatted)

    return reformatted


@app.post("/compare-sortedness")
async def compare_sortedness(request: CompareSortednessRequest):
    """
    Compare algorithm performance on sorting different input sortedness arrays
            and return time taken to run for a range of input lengths
    """

    algorithm = request.algorithm
    low = request.low
    high = request.high
    arr_types = request.arr_types
    num_reps = request.num_reps
    step = request.step

    algorithms = config.algorithms.get(algorithm.language)
    if algorithms is None or algorithm.algorithm not in algorithms:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported algorithm-language pairing {algorithm}",
        )

    results = {sortedness: [] for sortedness in arr_types}

    for current_length in range(low, high + 1, step):
        current_round = {sortedness: [] for sortedness in arr_types}

        for _ in range(num_reps):

            for sortedness in arr_types:
                array_generator = config.arrays[sortedness]
                array = array_generator(current_length)
                copy_array = deep_copy(array)
                _, time = sorter.call(
                    algorithm.algorithm,
                    algorithm.language,
                    copy_array,
                )
                current_round[sortedness].append(time)

        for sortedness, timing in current_round.items():
            average_time = sum(timing) / len(timing)
            results[sortedness].append((current_length, average_time))

    reformatted = {
        "type": "sortedness",
        "data_series": [
            {
                "algorithm": algorithm.algorithm,
                "language": algorithm.language,
                "array_type": sortedness,
                "data": series,
                "repeats": num_reps,
            }
            for (sortedness, series) in results.items()
        ],
    }

    app.db.store_comparison(reformatted)

    return reformatted


@app.get("/history")
def get_comparisons():
    """
    Return list of all previous comparisons
    """
    return {"comparisons": app.db.get_all_metadata()}


@app.get("/comparison/{id}")
def get_comparison(id: str):
    """
    Retrieve a comparison
    """
    result = app.db.get_comparison(id)

    if result is None:
        raise HTTPException(status_code=404, detail="Comparison not found")

    return result


@app.delete("/delete/{id}")
def delete_comparison(id: str):
    """
    delete a comparison
    """
    try:
        if app.db.delete_comparison(id) == 0:
            raise HTTPException(status_code=404, detail="Comparison not found")
    except RuntimeError as e:
        raise HTTPException(status_code=404, detail=f"Comparison not found: {e}")

    return {"comparisons": app.db.get_all_metadata()}
