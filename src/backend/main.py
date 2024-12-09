import hashlib
import json
import uuid
from typing import Any, Dict, List, Union

import redis
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import src.backend.backend_config as config
import src.backend.sorter as sorter

redis_client = redis.Redis(host="localhost", port=6379, db=0)


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/config", response_model=Dict[str, Any])
async def get_config() -> Dict[str, Any]:
    """
    Exposes configured algorithms, implemented languages and input array types.

    Returns:
        dict: keys=algorithms, array types
    """
    result = {}

    result["algorithms"] = {
        language: list(algorithms.keys())
        for language, algorithms in config.algorithms.items()
    }

    result["array types"] = list(config.arrays.keys())
    return result


@app.get("/algorithms", response_model=Dict[str, List[str]])
async def get_algorithms() -> Dict[str, List[str]]:
    """
    Return the algorithms configured in all supported languages
    """
    return {
        language: list(algorithms.keys())
        for language, algorithms in config.algorithms.items()
    }


@app.get("/arrays", response_model=List[str])
async def get_arrays() -> List[str]:
    """
    Return the arrays configured
    """
    return list(config.arrays.keys())


@app.post(
    "/compare-algorithms",
    response_model=List[Dict[str, Union[str, List[Dict[str, Any]]]]],
)
async def compare_algorithms(
    request: CompareAlgorithmsRequest,
) -> List[Dict[str, Union[str, List[Dict[str, Any]]]]]:
    """
    Compare sorting algorithms and return time taken to run for a range of input lengths
    """

    # Check for cache
    cache_request = json.dumps(request.dict(), sort_keys=True)
    key = hashlib.sha256(cache_request.encode()).hexdigest()

    result = redis_client.get(key)
    if result:
        return json.loads(result.decode())

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
                _, time = sorter.call(
                    algorithm.algorithm,
                    algorithm.language,
                    array,
                )
                current_round[(algorithm.algorithm, algorithm.language)].append(time)

        for (algorithm, language), timing in current_round.items():
            average_time = sum(timing) / len(timing)
            results[(algorithm, language)].append((current_length, average_time))

    reformatted = [
        (algorithm, language, series)
        for (algorithm, language), series in results.items()
    ]

    result_data = {
        "type": "compare-algorithms",
        "data": reformatted,
    }

    comparison_id = f"compare-algorithms:{uuid.uuid4()}"
    redis_client.set(comparison_id, json.dumps(result_data))
    redis_client.lpush("comparisons", comparison_id)

    redis_client.set(key, json.dumps(result_data))

    return reformatted


@app.post("/compare-sortedness", response_model=List[Dict[str, Any]])
async def compare_sortedness(request: CompareSortednessRequest) -> List[Dict[str, Any]]:
    """
    Compare algorithm performance on sorting different input sortedness arrays
            and return time taken to run for a range of input lengths
    """

    # check for cached
    cache_request = json.dumps(request.dict(), sort_keys=True)
    key = hashlib.sha256(cache_request.encode()).hexdigest()

    result = redis_client.get(key)
    if result:
        return json.loads(result.decode())

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
                _, time = sorter.call(
                    algorithm.algorithm,
                    algorithm.language,
                    array,
                )
                current_round[sortedness].append(time)

        for sortedness, timing in current_round.items():
            average_time = sum(timing) / len(timing)
            results[sortedness].append((current_length, average_time))

    reformatted = [(sortedness, series) for sortedness, series in results.items()]

    result = {
        "type": "compare-sortedness",
        "data": reformatted,
    }
    comparison_id = f"compare-sortedness:{uuid.uuid4()}"
    redis_client.set(comparison_id, json.dumps(result))
    redis_client.lpush("comparisons", comparison_id)

    redis_client.set(key, json.dumps(result))

    return reformatted


@app.post("/cache-comparison", response_model=Dict[str, str])
def cache_comparison(result: ComparisonResult) -> Dict[str, str]:
    """
    Cache a comparison result
    """
    key = f"comparison:{result.id}"
    redis_client.set(key, json.dumps(result.dict()))
    redis_client.lpush("comparisons", result.id)
    return {"message": "Success: comparison cached"}


@app.get("/history", response_model=Dict[str, List[Dict[str, Any]]])
def get_comparisons() -> Dict[str, List[Dict[str, Any]]]:
    """
    Return list of all previous comparisons
    """
    ids = redis_client.lrange("comparisons", 0, -1)
    comparisons = []

    for id in ids:
        full_id = id.decode()
        comparison_type, comparison_id = full_id.split(":")
        comparison_key = f"{comparison_type}:{comparison_id}"
        data = redis_client.get(comparison_key)

        if data:
            comparison = json.loads(data)
            comparisons.append(
                {
                    "id": comparison_id,
                    "type": comparison["type"],
                    "data": comparison["data"],
                }
            )

    return {"comparisons": comparisons}


@app.get("/comparison/{id}", response_model=Dict[str, Any])
def get_comparison(id: str) -> Dict[str, Any]:
    """
    Retrieve a comparison
    """
    key = f"compare-algorithms:{id}"
    result = redis_client.get(key)

    # secondary, reroll this in future
    if result == None:
        key = f"compare-sortedness:{id}"
        result = redis_client.get(key)

    if result is None:
        raise HTTPException(status_code=404, detail="Comparison not found")

    return json.loads(result)
