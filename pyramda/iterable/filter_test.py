from .filter import filter
from pyramda.private.asserts import assert_iterables_equal


def positive(x):
    return x > 0


def filter_nocurry_test():
    assert_iterables_equal(filter(positive, [2, -1, 0, 3, -2]), [2, 3])


def filter_curry_test():
    assert_iterables_equal(filter(positive)([2, -1, 0, 3, -2]), [2, 3])
