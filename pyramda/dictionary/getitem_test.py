from .getitem import getitem
from pyramda.private.asserts import assert_equal


def getitem_nocurry_item():
    assert_equal(getitem("a", {"a": 1}), 1)


def getitem_curry_item():
    assert_equal(getitem("a")({"a": 1}))
