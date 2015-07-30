from .divide import divide
from pyramda.private.asserts import assert_equal


def divide_nocurry_test():
    assert_equal(divide(10, 5), 2)


def divide_curry_test():
    assert_equal(divide(10)(5), 2)
