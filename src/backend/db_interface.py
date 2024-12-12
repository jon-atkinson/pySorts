import json
import logging
import uuid
from typing import Dict, List, Optional

import redis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Database:
    def __init__(self, host: str, port: int, db: int, namespace: str = "comparisons"):
        self.client = redis.Redis(host=host, port=port, db=db)
        self.namespace = namespace

    def _generate_id(self, comparison_type: str) -> str:
        return f"{comparison_type}:{uuid.uuid4()}"

    def _generate_key(self, *parts: str) -> str:
        return f"{self.namespace}:{':'.join(parts)}"

    def store_comparison(self, data: Dict, ttl: Optional[int] = None) -> str:
        """
        Store a comparison in Redis.
        """
        if "type" not in data or "data_series" not in data:
            raise ValueError("Data must contain 'type' and 'data_series' fields.")

        comparison_id = self._generate_id(data["type"])
        metadata = {
            "id": comparison_id,
            "type": data["type"],
            "algorithms": [
                [
                    entry["algorithm"],
                    entry["language"],
                    {
                        "type": entry["array_type"],
                        "length": len(entry["data"]),
                        "start": entry["data"][0][0],
                        "stop": entry["data"][-1][0],
                        "step": entry["data"][1][0] - entry["data"][0][0],
                        "repeats": entry["repeats"],
                    },
                ]
                for entry in data["data_series"]
            ],
        }

        try:
            with self.client.pipeline() as pipe:
                pipe.set(
                    self._generate_key("comparison", comparison_id),
                    json.dumps(data),
                    ex=ttl,
                )
                pipe.hset(
                    self._generate_key("metadata"), comparison_id, json.dumps(metadata)
                )
                pipe.rpush(self._generate_key("ids"), comparison_id)
                pipe.execute()
            logger.info(f"Stored comparison with id: {comparison_id}")
        except redis.exceptions.RedisError as e:
            raise RuntimeError(f"Failed to store comparison: {str(e)}")

        return comparison_id

    def get_comparison(self, comparison_id: str) -> Optional[Dict]:
        """
        Retrieve a comparison, including its data points, by ID.
        """
        try:
            data = self.client.get(self._generate_key("comparison", comparison_id))
            if data is None:
                logger.warning(f"Comparison not found for id: {comparison_id}")
                return None
            return json.loads(data)
        except redis.exceptions.RedisError as e:
            raise RuntimeError(
                f"Failed to retrieve comparison {comparison_id}: {str(e)}"
            )

    def get_all_metadata(self) -> List[Dict]:
        """
        Retrieve metadata for all stored comparisons.
        """
        try:
            comparison_ids = self.client.lrange(self._generate_key("ids"), 0, -1)
            metadata = []
            for comparison_id in comparison_ids:
                metadata_entry = self.client.hget(
                    self._generate_key("metadata"), comparison_id.decode()
                )
                if metadata_entry:
                    metadata.append(json.loads(metadata_entry))
            return metadata
        except redis.exceptions.RedisError as e:
            raise RuntimeError(f"Failed to retrieve all metadata: {str(e)}")

    def delete_comparison(self, comparison_id: str) -> None:
        """
        Delete a comparison by ID.
        """
        try:
            with self.client.pipeline() as pipe:
                pipe.delete(self._generate_key("comparison", comparison_id))
                pipe.hdel(self._generate_key("metadata"), comparison_id)
                pipe.lrem(self._generate_key("ids"), 0, comparison_id)
                pipe.execute()
            logger.info(f"Deleted comparison with id: {comparison_id}")
        except redis.exceptions.RedisError as e:
            raise RuntimeError(f"Failed to delete comparison {comparison_id}: {str(e)}")

    def get_metadata(self, comparison_id: str) -> Optional[Dict]:
        """
        Retrieve metadata for a single comparison.
        """
        try:
            metadata = self.client.hget(self._generate_key("metadata"), comparison_id)
            if metadata is None:
                logger.warning(f"Metadata not found for id: {comparison_id}")
                return None
            return json.loads(metadata)
        except redis.exceptions.RedisError as e:
            raise RuntimeError(
                f"Failed to retrieve metadata for {comparison_id}: {str(e)}"
            )
