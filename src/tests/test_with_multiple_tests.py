from ..calc import *

"""
Make sure that a simple sum works fine
"""


def test_add_basic():
    assert add(1, 2) == 3


def test_add_basic_type():
    assert type(add(1, 2)) is int


def test_add_with_many():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0
