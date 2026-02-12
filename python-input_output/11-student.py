#!/usr/bin/python3
"""Student class."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if isinstance(attrs, list):
            new_dict = {}
            for name in attrs:
                if isinstance(name, str) and name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dict."""
        for key, value in json.items():
            setattr(self, key, value)
