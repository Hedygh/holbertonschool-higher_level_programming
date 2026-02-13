#!/usr/bin/python3
"""Pickling custom classes."""

import pickle


class CustomObject:
    """Custom object class."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file. Return None on failure."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError, AttributeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file. Return None on failure."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (OSError, pickle.UnpicklingError, EOFError, AttributeError):
            return None
