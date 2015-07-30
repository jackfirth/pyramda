from .drop import drop
from pyramda.private.asserts import assert_iterables_equal


def drop_nocurry_test():
    assert_iterables_equal(drop(2, [1, 2, 3, 4]), [3, 4])


def drop_curry_test():
    assert_iterables_equal(drop(2)([1, 2, 3, 4]), [3, 4])
