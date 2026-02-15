#!/usr/bin/python3
"""XML serialization / deserialization (simple, no type conversion)"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary (values as strings)."""
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text if child.text is not None else ""

    return data
