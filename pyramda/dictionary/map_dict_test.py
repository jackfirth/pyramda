from .map_dict import map_dict
from .values import values
from pyramda.math import inc
from pyramda.private.asserts import assert_dicts_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

expected_dict = {
    "a": 2,
    "b": 3,
    "c": 4
}


def map_dict_test():
    assert_dicts_equal(map_dict(inc, test_dict), expected_dict)
