# To Load & filters the JSON data

import json
import os


def load_attractions(filename: str = "sf_attractions.json") -> list:
    # Reads the sf_attractions JSON file & returns a list

    # ADD CODE
    return []

def load_test_queries(filename: str = "test_queries.json") -> list:
    # Reads the draft test queries JSON file & returns a list of queries

    # ADD CODE
    return []

def filter_attractions_by_category(attractions: list, category: str) -> list:
    # (Helper function) - to filter by category 

    # ADD CODE
    return []


# Test
if __name__ == "__main__":
    data = load_attractions()
    print(f"{len(data)} attractions from json")
    if data:
        print("Sample item:", data[0]["name"])