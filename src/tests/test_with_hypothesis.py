import hypothesis.strategies as _strategies
from hypothesis import given, settings, Verbosity, example

from ..calc import *

"""
Test using hypotesis library, wide number of possibilities are tested
"""


@given(_strategies.integers(), _strategies.integers())
def test_add_basic(num1, num2):
    assert add(num1, num2) == num1 + num2


@given(_strategies.integers(), _strategies.integers())
@example(1, 2)
# @settings(verbosity=Verbosity.verbose)
def test_add_basic_with_example(num1, num2):
    assert add(num1, num2) == num1 + num2


@settings(verbosity=Verbosity.verbose)
@given(_strategies.integers(), _strategies.integers())
def test_add_with_shrinking_example(num1, num2):
    assert add(num1, num2) == num1 + num2
    # Test Identity property
    assert add(num1, 0) == num1
    assert add(0, num2) == num2
    # Test Commutative property
    assert add(num1, num2) == add(num2, num1)

# Marking this test as expected to fail:
# @pytest.mark.xfail
#@settings(verbosity=Verbosity.verbose)
@given(_strategies.integers(), _strategies.integers())
def test_subtract(num1, num2):
    """
    Shrinking failures is the process by which Hypothesis tries to produce human-readable examples when it
    finds a failure. It takes a complex example and turns it into a simpler one. To demonstrate this feature, 
    let’s add one more property to our test_sum function which says num1 should be less than or equal to 30.

    :param num1: integer value
    :param num2: integer value
    """
    assert subtract(num1, num2) == num1 - num2
    assert num1 <= 30 # if we want to fail

@given(_strategies.integers(), _strategies.integers())
def test_multiply(num1, num2):
    assert multiply(num1, num2) == num1 * num2

# Marking this test as expected to fail:
# @pytest.mark.xfail
@settings(verbosity=Verbosity.verbose)
@given(_strategies.floats(), _strategies.floats())
def test_add_with_floats(num1, num2):
    assert add(num1, num2) == num1 + num2
    # Test Identity property
    assert add(num1, 0) == num1
    # Test Commutative property
    assert add(num1, num2) == add(num2, num1)
    # assert num1 <= 30 : if we want to fail
