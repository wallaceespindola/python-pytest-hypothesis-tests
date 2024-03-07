import datetime
import decimal
import math
import random
import re
import uuid
from fractions import Fraction
from ipaddress import IPv4Address, IPv6Address
from typing import List

import hypothesis.strategies as st
from hypothesis import given, settings, Verbosity, example

from ..calc import *

"""
Test using hypothesis library, wide number of possibilities are tested
"""


@given(st.integers(), st.integers())
def test_add_basic(num1, num2):
    assert add(num1, num2) == num1 + num2


@given(st.integers(), st.integers())
@example(1, 2)
# @settings(verbosity=Verbosity.verbose)
def test_add_basic_with_example(num1, num2):
    assert add(num1, num2) == num1 + num2


@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_add_with_shrinking_example(num1, num2):
    assert add(num1, num2) == num1 + num2
    # Test Identity property
    assert add(num1, 0) == num1
    assert add(0, num2) == num2
    # Test Commutative property
    assert add(num1, num2) == add(num2, num1)

@settings(verbosity=Verbosity.verbose)
# Marking this test as expected to fail:
# @pytest.mark.xfail
# @settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_subtract(num1, num2):
    """
    Shrinking failures is the process by which Hypothesis tries to produce human-readable examples when it
    finds a failure. It takes a complex example and turns it into a simpler one. To demonstrate this feature, 
    let’s add one more property to our test_sum function which says num1 should be less than or equal to 30.
    :param num1: an integer value
    :param num2: an integer value
    """
    assert subtract(num1, num2) == num1 - num2
    #assert num1 <= 30  # if we want to fail


# Marking this test as expected to fail:
# @pytest.mark.xfail
@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_add_with_shrinking(num1, num2):
    assert add(num1, num2) == num1 + num2
    # Test Identity property
    assert add(num1, 0) == num1
    # Test Commutative property
    assert add(num1, num2) == add(num2, num1)
    # assert num1 <= 30 : if we want to fail


@given(st.floats(allow_infinity=False, allow_nan=False, min_value=-1e10, max_value=1e10))
def test_floats(value):
    """
    This test function will receive a wide range of float values within the specified bounds and assert that
    they indeed fall within these bounds.
    :param value: a float value
    """
    assert -1e10 <= value <= 1e10

@settings(verbosity=Verbosity.verbose)
#@settings(max_examples=) # TODO check and test
@given(st.text(alphabet=st.characters(blacklist_categories=["Cs", "Cc"]), min_size=1, max_size=100))
def test_strings(value):
    """
    This test function generates non-control-character strings of lengths between 1 and 100 and checks their lengths.
    To generate string values, you can use the text strategy. You can specify an alphabet and a minimum or
    maximum size for the string.
    :param value:
    """
    assert 1 <= len(value) <= 100


@given(st.lists(st.integers(), min_size=0, max_size=20))
def test_lists(value):
    """
    This function tests lists of integers, ensuring they fall within the specified size range.
    To generate lists, use the lists strategy. You can specify the elements' strategy, minimum size,
     and maximum size of the list.
    :param value: a list value
    """
    assert 0 <= len(value) <= 20


@given(st.lists(st.integers()))
def test_lists_of_elements(value):
    """
    Generates lists of elements, where each element is generated based on a given strategy.
    This test verifies that the generated object is a list and that each element within the list is an integer.
    :param value: a list value
    """
    assert isinstance(value, list)  # Check if it is a list
    for item in value:
        assert isinstance(item, int)  # Check if all items are integers


@given(st.dates())
def test_dates(value):
    """
    To generate date values, use the dates strategy. This will generate dates between the year 1 and 9999.
    This function verifies that the generated dates are within the valid range of Python date objects.
    :param value:
    """
    assert datetime.date.min <= value <= datetime.date.max


@settings(verbosity=Verbosity.verbose)
@given(st.text())
def test_operation_text(value):
    """
    Checks that the generated value is a string, demonstrating the generation of potentially wide-ranging Unicode text.
    :param value: a text value
    """
    assert isinstance(value, str)  # Check if it is a string
    assert operation_text(value) == f'This is the input text: {value}'


@given(st.binary())
def test_binary(data):
    assert isinstance(data, bytes)


@given(st.booleans())
def test_booleans(value):
    assert value in [True, False]


class MyObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@given(st.builds(MyObject, x=st.integers(), y=st.integers()))
def test_builds(obj):
    assert isinstance(obj, MyObject)


@given(st.characters())
def test_characters(value):
    """
    characters - Generates unicode characters.
    :param value: a character value
    """
    assert isinstance(value, str) and len(value) == 1


@given(st.complex_numbers())
def test_complex_numbers(value):
    assert isinstance(value, complex)


@st.composite
def list_of_integers(draw):
    integer_list = draw(st.lists(st.integers()))
    return integer_list


@given(list_of_integers())
def test_composite(value):
    assert all(isinstance(x, int) for x in value)


@st.composite
def list_of_integers(draw):
    """
    composite - Creates a strategy by composing simpler strategies.
    :param draw: an input
    """
    integer_list = draw(st.lists(st.integers()))
    return integer_list


@given(list_of_integers())  # use previous function
def test_composite(value):
    """
    composite - Creates a strategy by composing simpler strategies.
    :param value: a composite custom input
    """
    assert all(isinstance(x, int) for x in value)


@given(st.data())
def test_data(data):
    """
    data - Provides a DataObject for drawing more values interactively.
    :param data:
    """
    value = data.draw(st.integers())
    assert isinstance(value, int)


@given(st.dates())
def test_dates(value):
    assert isinstance(value, datetime.date)


@given(st.datetimes())
def test_datetimes(value):
    assert isinstance(value, datetime.datetime)


@given(st.decimals())
def test_decimals(value):
    assert isinstance(value, decimal.Decimal)


@given(st.dictionaries(keys=st.text(), values=st.integers()))
def test_dictionaries(value):
    """
    dictionaries - Generates dictionaries with keys and values generated by other strategies.
    :param value: a dict value
    """
    assert isinstance(value, dict)  # Ensure it's a dictionary
    for key, val in value.items():
        assert isinstance(key, str)  # Key check
        assert isinstance(val, int)  # Value check


@settings(verbosity=Verbosity.verbose)
@given(st.emails())
def test_emails(value):
    """
    emails - Generates valid email addresses.
    :param value: an email string
    """
    assert isinstance(value, str)  # Check if it's a string
    assert "@" in value  # An email should contain a '@'
    assert "." in value  # An email should contain a '.'


@settings(verbosity=Verbosity.verbose)
@given(st.fixed_dictionaries({'name': st.text(), 'age': st.integers(min_value=0)}))
def test_fixed_dictionaries(value):
    """
    fixed_dictionaries - Generates dictionaries with fixed keys and strategies for their values.
    :param value: a dict value
    """
    assert isinstance(value, dict) and 'name' in value and 'age' in value
    assert isinstance(value['name'], str)
    assert isinstance(value['age'], int) and value['age'] >= 0


@settings(verbosity=Verbosity.verbose)
@given(st.floats(allow_nan=False, allow_infinity=False))
def test_floats(value):
    """
    floats - Generates floating-point numbers.
    :param value: a float value
    """
    assert isinstance(value, float)  # Check type
    assert not (math.isnan(value) or math.isinf(value))  # Validate constraints


@given(st.floats(allow_nan=False, allow_infinity=False), st.floats(allow_nan=False, allow_infinity=False))
def test_add_floats(num1, num2):
    """
    Generates floating-point numbers to be summed up.
    :param num1: a float value 1
    :param num2: a float value 2
    """
    assert add(num1, num2) == num1 + num2


@given(st.decimals(allow_nan=False, allow_infinity=False), st.decimals(allow_nan=False, allow_infinity=False))
def test_subtract_decimals(num1, num2):
    """
    Generates decimal floating-point numbers to be subtracted.
    :param num1: a decimal value 1
    :param num2: a decimal value 2
    """
    assert subtract(num1, num2) == num1 - num2


@given(st.fractions())
def test_fractions(value):
    assert isinstance(value, Fraction)  # Check type


@given(st.from_regex(r'^\d{3}-\d{2}-\d{4}$'))
def test_from_regex(value):
    assert isinstance(value, str) and re.match(r'^\d{3}-\d{2}-\d{4}$', value)


@given(st.from_type(List[int]))
def test_from_type(value):
    """
    This test generates lists of integers, verifying that all elements are integers.
    :param value: a type value
    """
    assert isinstance(value, list)
    for item in value:
        assert isinstance(item, int)


@given(st.frozensets(elements=st.integers()))
def test_frozensets(value):
    """
    Generates immutable sets.
    This test confirms that generated values are indeed frozen sets and contain integers.
    :param value: an immutable set of elements
    """
    assert isinstance(value, frozenset)


@given(st.functions())
def test_functions(value):
    """
    Generates callable functions.
    This function checks that the generated object is a callable function.
    :param value: an immutable set of elements
    """
    assert callable(value)


@settings(verbosity=Verbosity.verbose)
@given(st.ip_addresses())
def test_ip_addresses(value):
    """
    Generates IP addresses.
    This test verifies that the generated value is either an IPv4 or IPv6 address.
    :param value:
    """
    assert isinstance(value, (IPv4Address, IPv6Address))


@given(st.iterables(elements=st.integers()))
def test_iterables(value):
    """
    Generates arbitrary iterables.
    This test checks that the generated value is an iterable containing integers.
    :param value:
    """
    assert hasattr(value, '__iter__')  # Check if value is iterable
    for item in value:
        assert isinstance(item, int)  # Check if items are integers


@settings(verbosity=Verbosity.verbose)
@given(st.one_of(st.integers(), st.text()))
def test_one_of(value):
    """
    Chooses from one of the provided strategies.
    This test checks that the generated value is either an integer or a string, depending on which strategy
    one_of picks during each test run.
    :param value: an integer or string value
    """
    assert isinstance(value, (int, str))  # Check if the value is an integer or string


@given(st.randoms())
def test_randoms(value):
    """
    Provides a strategy that generates random.Random instances.
    Verifies that the generated value is an instance of random.Random and then uses it to generate a random integer.
    :param value: a random value
    """
    assert isinstance(value, random.Random)  # Check if value is a Random instance
    # Demonstrate using the random instance
    assert isinstance(value.randint(1, 10), int)


@given(st.sets(st.integers()))
def test_sets(value):
    """
    Generates sets of unique elements.
    Confirms that the generated value is a set and checks if all elements in the set are integers.
    :param value: a set on integers
    """
    assert isinstance(value, set)  # Check if it is a set
    for item in value:
        assert isinstance(item, int)  # Check if all items are integers


@settings(verbosity=Verbosity.verbose)
@given(st.lists(st.integers()), st.slices(size=100))
def test_slices(lst, slc):
    """
    Generates slice objects, which can be used to index lists or other indexable structures.
    This test checks that the generated object is a valid slice and can be used to slice a list.
    :param lst: a list
    :param slc: a slice
    """
    assert isinstance(slc, slice)  # Check if it is a slice object
    # Use the slice on the list to ensure it works without error
    assert isinstance(lst[slc], list)  # Check if slicing returns a list


@given(st.timedeltas())
def test_timedeltas(value):
    """
    Generates datetime.timedelta objects.
    Confirms that the generated object is a timedelta, suitable for representing differences in time.
    :param value: a timedelta value
    """
    assert isinstance(value, datetime.timedelta)  # Check if it is a timedelta object


@given(st.times())
def test_times(value):
    """
    Ensures that the generated value is a time object, representing a specific time of day without any date association.
    :param value: a time value
    """
    assert isinstance(value, datetime.time)  # Check if it is a time object


@given(st.timezones())
def test_timezones(value):
    """
    Generates timezone-aware or naive datetime objects.
    This test check that the generated object is either a timezone object or None, reflecting the possible
    generation of naive datetime objects.
    :param value: a timezone value
    """
    assert any([value is None, hasattr(value, 'utcoffset')]), "Must be a timezone or None"


@given(st.tuples(st.integers(), st.text()))
def test_tuples(value):
    """
    Generates tuples with elements based on the strategies provided.
    This test confirms that the generated object is a tuple with an integer and a string, demonstrating the
    combination of different data types.
    :param value: a tuple[int, str]
    """
    assert isinstance(value, tuple)  # Check if it is a tuple
    assert isinstance(value[0], int) and isinstance(value[1], str)


@settings(verbosity=Verbosity.verbose)
@given(st.uuids())
def test_uuids(value):
    """
    Generates UUID objects.
    This test verifies that the generated value is a UUID, a unique identifier that can be used in
    various applications requiring distinct values.
    :param value: an uuid value
    """
    assert isinstance(value, uuid.UUID)  # Check if it is a UUID
