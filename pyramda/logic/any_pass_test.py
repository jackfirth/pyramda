from .any_pass import any_pass


def positive(x):
    return x > 0


def negative(x):
    return x < 0


def any_pass_nocurry_test():
    assert not any_pass([], "foo")
    assert any_pass([positive, negative], 5)
    assert any_pass([positive, negative], -5)
    assert not any_pass([positive, negative], 0)


def any_pass_curry_test():
    nonzero = any_pass([positive, negative])
    assert nonzero(5)
    assert nonzero(-5)
    assert not nonzero(0)
