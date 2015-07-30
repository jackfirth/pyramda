from .all_satisfy import all_satisfy


def positive(x):
    return x > 0


def all_satisfy_nocurry_test():
    assert all_satisfy(positive, [1, 2, 3])
    assert not all_satisfy(positive, [1, -2, 3])


def all_satisfy_curry_test():
    assert all_satisfy(positive)([1, 2, 3])
    assert not all_satisfy(positive)([1, -2, 3])
