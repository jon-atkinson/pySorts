import re

import fakeredis
import pytest
from fastapi.testclient import TestClient

import tests.helpers as helpers
from backend.backend_config import algorithms, arrays
from backend.db_interface import Database
from backend.main import app
from tests.helpers import first_algorithm, first_array_type, first_language


@pytest.fixture
def redis_client():
    redis_client = fakeredis.FakeRedis()
    app.db = Database(namespace="test_namespace", client=redis_client)

    yield redis_client

    app.db.client.flushall()


@pytest.fixture
def client(redis_client):
    return TestClient(app)


def test_get_config(client):
    response = client.get("/config")

    assert response.status_code == 200
    response_data = response.json()

    assert "algorithms" in response_data
    assert "array types" in response_data
    assert response_data == {
        "algorithms": {
            language: list(algorithms.keys())
            for language, algorithms in algorithms.items()
        },
        "array types": list(arrays.keys()),
    }


def test_get_algorithms(client):
    response = client.get("/algorithms")

    assert response.status_code == 200
    response_data = response.json()

    assert isinstance(response_data, dict)
    assert response_data == {
        language: list(algorithms.keys()) for language, algorithms in algorithms.items()
    }


def test_get_arrays(client):
    response = client.get("/arrays")

    assert response.status_code == 200
    response_data = response.json()

    assert isinstance(response_data, list)
    assert response_data == list(arrays.keys())


def test_compare_algorithms_valid(client):
    input_data = {
        "algorithms": [
            {
                "algorithm": first_algorithm,
                "language": first_language,
            },
        ],
        "low": 0,
        "high": 100,
        "arr_type": first_array_type,
        "num_reps": 1,
        "step": 1,
    }

    response = client.post("/compare-algorithms", json=input_data)
    assert response.status_code == 200
    response_data = response.json()
    assert all(key in response_data for key in ["type", "data_series"])
    assert isinstance(response_data["data_series"], list)
    helpers.test_comparison_results_shape(response_data)


def test_compare_algorithms_invalid_array_type(client):
    input_data = {
        "algorithms": [
            {
                "algorithm": first_algorithm,
                "language": first_language,
            },
        ],
        "low": 0,
        "high": 100,
        "arr_type": "invalid_array_type",
        "num_reps": 1,
        "step": 1,
    }

    response = client.post("/compare-algorithms", json=input_data)
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Unsupported array type" in response.json()["detail"]


def test_compare_sortedness_valid(client):
    input_data = {
        "algorithm": {"algorithm": first_algorithm, "language": first_language},
        "low": 0,
        "high": 100,
        "arr_type": [first_array_type],
        "num_reps": 1,
        "step": 1,
    }

    response = client.post("/compare-sortedness", json=input_data)
    assert response.status_code == 200
    response_data = response.json()
    assert "data_series" in response_data
    assert isinstance(response_data["data_series"], list)
    helpers.test_comparison_results_shape(response_data)


def test_compare_sortedness_invalid_algorithm(client):
    first_language = list(algorithms.keys())[0]
    first_array_type = list(arrays.keys())[0]

    input_data = {
        "algorithm": {"algorithm": "invalid algorithm", "language": first_language},
        "low": 0,
        "high": 100,
        "arr_type": [first_array_type],
        "num_reps": 1,
        "step": 1,
    }

    response = client.post("/compare-sortedness", json=input_data)
    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Unsupported algorithm-language pairing" in response.json()["detail"]


def test_get_comparisons_empty(client):
    response = client.get("/history")
    assert response.status_code == 200
    response_data = response.json()
    assert "comparisons" in response_data
    assert (
        isinstance(response_data["comparisons"], list)
        and response_data["comparisons"] == []
    )


def test_get_comparisons_populated(client):
    input_data = {
        "algorithms": [
            {
                "algorithm": first_algorithm,
                "language": first_language,
            },
        ],
        "low": 0,
        "high": 100,
        "arr_type": first_array_type,
        "num_reps": 1,
        "step": 1,
    }

    response = client.post("/compare-algorithms", json=input_data)
    assert response.status_code == 200

    response = client.get("/history")
    assert response.status_code == 200

    response_data = response.json()

    # shape
    helpers.test_get_all_comparisons_shape(response_data)

    # values
    assert re.match(
        "algorithm:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        response_data["comparisons"][0]["id"],
    )
    assert response_data["comparisons"][0]["type"] == "algorithm"
    assert response_data["comparisons"][0]["algorithms"][0][2] == {
        "type": "random",
        "length": 101,
        "repeats": 1,
        "start": 0,
        "stop": 100,
        "step": 1,
    }


def test_get_comparison_valid_id(client):
    input_data = {
        "algorithms": [
            {
                "algorithm": first_algorithm,
                "language": first_language,
            },
        ],
        "low": 0,
        "high": 100,
        "arr_type": first_array_type,
        "num_reps": 1,
        "step": 1,
    }

    response = client.post("/compare-algorithms", json=input_data)
    assert response.status_code == 200

    response = client.get("/history")
    assert response.status_code == 200

    helpers.test_get_all_comparisons_shape(response.json())
    id = response.json()["comparisons"][0]["id"]

    response = client.get(f"/comparison/{id}")
    response_data = response.json()

    assert response.status_code == 200
    helpers.test_comparison_results_shape(response_data)

    assert response_data["data_series"][0]["algorithm"] == first_algorithm
    assert response_data["data_series"][0]["array_type"] == first_array_type


def test_get_comparison_invalid_id(client):
    response = client.get("/comparison/invalid_id")
    assert response.status_code == 404
    assert "detail" in response.json()
    assert "Comparison not found" in response.json()["detail"]


def test_delete_comparison_valid_id(client):
    input_data = {
        "algorithms": [
            {
                "algorithm": first_algorithm,
                "language": first_language,
            },
        ],
        "low": 0,
        "high": 100,
        "arr_type": first_array_type,
        "num_reps": 1,
        "step": 1,
    }

    response = client.post("/compare-algorithms", json=input_data)
    assert response.status_code == 200

    response = client.get("/history")
    assert response.status_code == 200

    helpers.test_get_all_comparisons_shape(response.json())
    id = response.json()["comparisons"][0]["id"]

    response = client.delete(f"/delete/{id}")
    assert response.status_code == 200
    assert "comparisons" in response.json()
    assert len(response.json()["comparisons"]) == 0

    response = client.get("/comparison/{id}")
    assert response.status_code == 404
    assert "detail" in response.json()
    assert "Comparison not found" in response.json()["detail"]


def test_delete_comparison_invalid_id(client):
    response = client.delete("/delete/invalid_id")
    assert response.status_code == 404
    assert "detail" in response.json()
    assert "Comparison not found" in response.json()["detail"]
