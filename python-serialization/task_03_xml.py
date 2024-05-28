#!/usr/bin/env python3
"""Python Module to import xml.etree.ElementTree as ET"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize and save data to the specified file."""
    root = ET.Element("data")

    def build_tree(element, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(element, key)
                build_tree(child, value)
        else:
            element.text = str(data)

    build_tree(root, dictionary)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Load and deserialize data from the specified file."""
    tree = ET.parse(filename)
    root = tree.getroot()

    def parse_element(element):
        if len(element):
            return {child.tag: parse_element(child) for child in element}
        else:
            text = element.text
            try:
                return int(text)
            except ValueError:
                try:
                    return float(text)
                except ValueError:
                    return text

    return {root.tag: parse_element(root)}
