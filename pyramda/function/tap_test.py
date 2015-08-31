from .tap import tap
from pyramda.private.asserts import assert_equal


def tap_test():
    called = False

    def set_called(v):
        nonlocal called
        called = True

    assert_equal(tap(set_called, 42), 42)
    assert called
