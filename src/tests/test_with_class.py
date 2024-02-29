from ..calc import *

"""
A simple sum test using a class
"""

class TestSum(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_add_example_with_class(self):
        assert add(1, 2) == 3

    @classmethod
    def teardown_class(cls):
        pass
