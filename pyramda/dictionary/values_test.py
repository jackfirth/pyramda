from .values import values
from pyramda.private.asserts import assert_iterables_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}


def values_test():
    assert_iterables_equal(set(values(test_dict)), set([1, 3, 2]))
