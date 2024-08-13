#!/usr/bin/env python3
"""
Module for updating the topics of a school document.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the school name.
    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
