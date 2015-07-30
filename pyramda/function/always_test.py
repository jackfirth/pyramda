from .always import always
from pyramda.private.asserts import assert_equal


def always_nocurry_test():
    assert_equal(always(3, "foo"), 3)


def always_curry_test():
    always3 = always(3)
    assert_equal(always3("foo"), 3)
