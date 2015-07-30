from .concat import concat
from pyramda.private.asserts import assert_iterables_equal


def concat_nocurry_test():
    assert_iterables_equal(concat([1, 2], [3, 4]), [1, 2, 3, 4])


def concat_curry_test():
    assert_iterables_equal(concat([1, 2])([3, 4]), [1, 2, 3, 4])
