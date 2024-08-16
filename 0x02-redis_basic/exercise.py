#!/usr/bin/env python3
"""
Cache class that interacts with a Redis database to store and retrieve data.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to store data in Redis.
    """

    def __init__(self):
        """
        Initializes the Cache class with a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis using a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

