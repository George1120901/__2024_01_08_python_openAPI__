#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
test_doctest - Trying doctest for unit testing
"""
import doctest

def my_cube(x):
    """
    (number) -> (number)
    Return the cube of the given number.

    :param x: number
    :return: number

    Examples (can be used by doctest for unit testing):
    >>> my_cube(5)
    125
    >>> my_cube(-5)
    -125
    >>> my_cube(0)
    0
    """
    return x*x*x

if __name__ == "__main__":
    import doctest
    doctest.testmod()