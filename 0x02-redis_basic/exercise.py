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

def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a particular function.

    Args:
        method (Callable): The method to be wrapped.

    Returns:
        Callable: The wrapped method with call history functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores the history of function inputs and outputs.

        Args:
            self (Cache): The instance of the Cache class.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of the original method call.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the input arguments as a string
        self._redis.rpush(input_key, str(args))

        # Execute the original function and get the output
        output = method(self, *args, **kwargs)

        # Store the output
        self._redis.rpush(output_key, str(output))

        return output

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
