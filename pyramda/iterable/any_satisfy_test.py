from .any_satisfy import any_satisfy


def positive(x):
    return x > 0


def any_satisfy_nocurry_test():
    assert any_satisfy(positive, [-1, -2, 3])
    assert not any_satisfy(positive, [-1, -2, -3])


def any_satisfy_curry_test():
    assert any_satisfy(positive)([-1, -2, 3])
    assert not any_satisfy(positive)([-1, -2, -3])
