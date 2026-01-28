#!/usr/bin/python3
"""Class Square that defines a square."""


class Square:
    """Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int)
                or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # and position."""
        print(self, end="")

    def __str__(self):
        """Return the square representation as a string."""
        if self.__size == 0:
            return "\n"

        lines = []

        # vertical offset (blank lines)
        for _ in range(self.__position[1]):
            lines.append("")

        # square lines with horizontal offset (spaces)
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
