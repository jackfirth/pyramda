from .greater import greater
from pyramda.private.asserts import assert_equal


def greater_nocurry_test():
    assert_equal(greater(5, 3), 5)
    assert_equal(greater(5, 7), 7)


def greater_curry_test():
    min5 = greater(5)
    assert_equal(min5(3), 5)
    assert_equal(min5(7), 7)
