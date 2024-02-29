import pytest

from ..calc import *

"""
A parametrized test giving the possibility of a list of inputs for a single test
"""


@pytest.mark.parametrize('num1, num2, expected', [(3, 5, 8)])
def test_add_with_one_value(num1, num2, expected):
    assert add(num1, num2) == expected


@pytest.mark.parametrize('num1, num2, expected', [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)])
def test_add_with_multi_value(num1, num2, expected):
    assert add(num1, num2) == expected
