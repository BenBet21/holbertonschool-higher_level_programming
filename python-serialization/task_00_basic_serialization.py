#!/usr/bin/env python3
"""Python Module to demonstrate \
basic serialization and deserialization of data."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to the specified file."""

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from the specified file."""

    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
