from .all_pass import all_pass


def positive(x):
    return x > 0


def less_than_ten(x):
    return x < 10


def all_pass_nocurry_test():
    assert all_pass([], "foo")
    assert all_pass([positive, less_than_ten], 5)
    assert not all_pass([positive, less_than_ten], 10)
    assert not all_pass([positive, less_than_ten], 0)


def all_pass_curry_test():
    between_zero_and_ten = all_pass([positive, less_than_ten])
    assert between_zero_and_ten(5)
    assert not between_zero_and_ten(10)
    assert not between_zero_and_ten(0)
