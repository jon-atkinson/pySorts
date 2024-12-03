from fastapi import FastAPI, HTTPException
from typing import List
import python.arrays as arrays
import python.sorter as sorter
from pydantic import BaseModel 
import python.config as config

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
        for language, algorithms
        in config.algorithms.items()
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
        for language, algorithms
        in config.algorithms.items()
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
        raise HTTPException(status_code=400, detail=f"Unsupported array type {arr_type}")

    results = {(algorithm.algorithm, algorithm.language): [] for algorithm in algorithms}
    array_generator = config.arrays[arr_type]

    for current_length in range(low, high + 1, step):
        current_round = {(algorithm.algorithm, algorithm.language): [] for algorithm in algorithms}

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
