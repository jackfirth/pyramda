from .min import min
from pyramda.private.asserts import assert_equal


def min_test():
    assert_equal(min([3, 1, 4, 2]), 1)
