from .map_dict import map_dict
from .values import values
from pyramda.math import inc
from pyramda.private.asserts import assert_iterables_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}


def map_dict_test():
    incd_dict = map_dict(inc, test_dict)
    assert_iterables_equal(set(values(incd_dict)), set([2, 4, 3]))
