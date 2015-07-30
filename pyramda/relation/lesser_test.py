from .lesser import lesser
from pyramda.private.asserts import assert_equal


def lesser_nocurry_test():
    assert_equal(lesser(5, 3), 3)
    assert_equal(lesser(5, 7), 5)


def lesser_curry_test():
    max5 = lesser(5)
    assert_equal(max5(3), 3)
    assert_equal(max5(7), 5)
