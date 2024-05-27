#!/usr/bin/python3
"""This function returns an object \
(Python data structure) represented by a JSON string:"""
import json


def from_json_string(my_str):
    """4. From JSON string to Object"""
    return json.loads(my_str)
