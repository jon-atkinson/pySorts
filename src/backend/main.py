from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import src.backend.backend_config as config
import src.backend.sorter as sorter


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


app = FastAPI()


@app.get("/config")
async def root():
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


@app.get("/algorithms")
async def root():
    """
    Return the algorithms configured in all supported languages
    """
    return {
        language: list(algorithms.keys())
        for language, algorithms in config.algorithms.items()
    }


@app.get("/arrays")
async def root():
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
    config.algorithms

    if (
        algorithm.language not in config.algorithms
        or algorithm.algorithm not in config.algorithms[algorithm.language]
    ):
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

    return reformatted
