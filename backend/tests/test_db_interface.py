import fakeredis
import pytest

from src.db_interface import Database


@pytest.fixture
def redis_client():
    return fakeredis.FakeStrictRedis()


@pytest.fixture
def db(redis_client):
    return Database(namespace="test_namespace", client=redis_client)


def test_store_comparison(db):
    data = {
        "type": "algorithm",
        "data_series": [
            {
                "algorithm": "quick sort",
                "language": "python",
                "array_type": "random",
                "data": [[0, 0.01], [1, 0.011], [2, 0.012]],
                "repeats": 5,
            }
        ],
    }
    comparison_id = db.store_comparison(data)
    assert comparison_id.startswith("algorithm:")

    stored_data = db.get_comparison(comparison_id)
    assert stored_data == data

    metadata = db.get_metadata(comparison_id)
    assert metadata is not None
    assert metadata["type"] == "algorithm"


def test_get_comparison_not_found(db):
    result = db.get_comparison("nonexistent_id")
    assert result is None


def test_get_all_metadata(db):
    for _ in range(3):
        db.store_comparison(
            {
                "type": "sortedness",
                "data_series": [
                    {
                        "algorithm": "merge sort",
                        "language": "c",
                        "array_type": "random",
                        "data": [[0, 0.01], [1, 0.011], [2, 0.012]],
                        "repeats": 5,
                    }
                ],
            }
        )

    metadata = db.get_all_metadata()
    assert len(metadata) == 3
    assert all(item["type"] == "sortedness" for item in metadata)


def test_delete_comparison(db):
    data = {
        "type": "algorithm",
        "data_series": [
            {
                "algorithm": "bubble sort",
                "language": "c",
                "array_type": "random",
                "data": [[0, 0.01], [1, 0.011], [2, 0.012]],
                "repeats": 2,
            }
        ],
    }
    comparison_id = db.store_comparison(data)

    assert db.get_comparison(comparison_id) is not None

    db.delete_comparison(comparison_id)

    assert db.get_comparison(comparison_id) is None
    assert db.get_metadata(comparison_id) is None


def test_invalid_store_comparison(db):
    invalid_data = {"data_series": []}
    with pytest.raises(ValueError, match="Data must contain 'type' and 'data_series'"):
        db.store_comparison(invalid_data)
