#!/usr/bin/env python3
"""Python Module to import xml.etree.ElementTree as ET"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize and save data to the specified file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Load and deserialize data from the specified file."""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
