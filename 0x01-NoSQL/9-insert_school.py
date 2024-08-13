from pymongo import MongoClient
from insert_school import insert_school

if __name__ == "__main__":
    # Connecting to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["my_database"]
    collection = db["school"]

    # Inserting a new document
    new_id = insert_school(collection, name="Holberton School", address="972 Mission Street")
    print("New document ID:", new_id)
