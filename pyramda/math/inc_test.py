from .inc import inc
from pyramda.private.asserts import assert_equal


def inc_test():
    assert_equal(inc(5), 6)
