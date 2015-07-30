from .equal import equal


def equal_nocurry_test():
    assert equal("foo", "foo")


def equal_curry_test():
    assert equal("foo")("foo")
