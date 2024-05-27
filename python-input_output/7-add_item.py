#!/usr/bin/python3
"""This function adds all arguments \
to a Python list, and then save them to a file:”"""
import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

arguments = sys.argv[1:]
items.extend(arguments)

save_to_json_file(items, filename)
