from .equals import equals


def equals_nocurry_test():
    assert equals("foo", "foo")


def equals_curry_test():
    assert equals("foo")("foo")
