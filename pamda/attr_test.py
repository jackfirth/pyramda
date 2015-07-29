from .attr import attr
from .private.asserts import assert_equal


class TestObject:
    def __init__(self, val):
        self.val = val


test_object = TestObject("foo")


def attr_nocurry_test():
    assert_equal(attr("val", test_object), "foo")


def attr_curry_test():
    assert_equal(attr("val")(test_object), "foo")
