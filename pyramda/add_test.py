from .add import add
from .private.asserts import assert_equal


def add_nocurry_test():
    assert_equal(add(1, 2), 3)


def add_curry_test():
    assert_equal(add(1)(2), 3)
