#!/usr/bin/env python3
"""
Cache class that interacts with a Redis database to store and retrieve data.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the method call count.
        """
        # Increment the call count using the method's qualified name as key
        self._redis.incr(method.__qualname__)
        # Call the original method
        return method(self, *args, **kwargs)

    return wrapper

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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis using a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, None]:
        """
        Retrieves data from Redis and applies a conversion function if provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

     def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data from Redis and converts it to a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from Redis and converts it to an integer.
        """
        return self.get(key, int)
