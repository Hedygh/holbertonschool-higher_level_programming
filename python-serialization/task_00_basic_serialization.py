#!/usr/bin/python3
#!/usr/bin/python3
"""Basic JSON serialization module."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize dict `data` to JSON and write it to `filename`."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Read JSON from `filename` and return it as a Python dict."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
