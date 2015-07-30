from .isinstance import isinstance


def isinstance_nocurry_test():
    assert isinstance(str, "foo")


def isinstance_curry_test():
    assert isinstance(str)("foo")
