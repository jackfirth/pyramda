from .either import either


def positive(x):
    return x > 0


def negative(x):
    return x < 0


def either_nocurry_test():
    assert either(positive, negative, -5)
    assert either(positive, negative, 5)
    assert not either(positive, negative, 0)


def either_curry_test():
    nonzero = either(positive, negative)
    assert nonzero(-5)
    assert nonzero(5)
    assert not nonzero(0)
