from .both import both


def positive(x):
    return x > 0


def less_than_ten(x):
    return x < 10


def both_nocurry_test():
    assert both(positive, less_than_ten, 5)
    assert not both(positive, less_than_ten, 10)
    assert not both(positive, less_than_ten, 0)


def both_curry_test():
    between_zero_and_ten = both(positive, less_than_ten)
    assert between_zero_and_ten(5)
    assert not between_zero_and_ten(10)
    assert not between_zero_and_ten(0)
