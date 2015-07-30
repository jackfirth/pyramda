from .contains import contains


def contains_nocurry_test():
    assert contains(2, [1, 2, 3])
    assert not contains(0, [1, 2, 3])


def contains_curry_test():
    assert contains(2)([1, 2, 3])
    assert not contains(0)([1, 2, 3])
