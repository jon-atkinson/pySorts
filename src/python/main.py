from fastapi import FastAPI, Query, HTTPException
from typing import List
import python.arrays as arrays
import python.sorter as sorter
from pydantic import BaseModel 

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

@app.get("/")
async def root():
    return {"message": "Welcome to pySorts, please hit another endpoint to do something useful"}

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

    if arr_type not in arrays.generators.keys():
        raise HTTPException(status_code=400, detail=f"Unsupported array type {arr_type}")

    results = {(algorithm.algorithm, algorithm.language): [] for algorithm in algorithms}
    array_generator = arrays.generators[arr_type]

    for current_length in range(low, high + 1, step):
        current_round = {(algorithm.algorithm, algorithm.language): [] for algorithm in algorithms}

        for _ in range(num_reps):
            array = array_generator(current_length)

            for algorithm in algorithms:
                _, time = sorter.call(
                    algorithm.algorithm,
                    algorithm.language,
                    arrays.deep_copy(array),
                )
                current_round[(algorithm.algorithm, algorithm.language)].append(time)

        for (algorithm, language), times in current_round.items():
            average_time = sum(times) / len(times)
            results[(algorithm, language)].append((current_length, average_time))

    reformatted = [
        (algorithm, language, series)
        for (algorithm, language), series in results.items()
    ]
    return {"results": reformatted}
