# test driven development
Python TDD (doctest): write tests first in ./tests/*.txt and run: python3 -m doctest ./tests/*
Each module and function must have a meaningful docstring (not a single word).
Validate inputs with isinstance() and raise the exact exceptions/messages required.
Prefer returning new data (no side effects) unless the task says to print.
Cover edge cases: wrong types, empty inputs, size mismatches, div by zero, rounding/format.