from .identical import identical


def identical_nocurry_test():
    assert identical(1, 1)
    assert not identical([1], [1])


def identical_curry_test():
    assert identical(1)(1)
    assert not identical([1])([1])
