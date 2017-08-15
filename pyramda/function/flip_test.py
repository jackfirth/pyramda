from .flip import flip


def merge_three(a, b, c):
    return [a, b, c]


def test_flip_calls_function_by_swapping_first_two_args():
    assert flip(merge_three)(1, 2, 3) == [2, 1, 3]


def test_curry_flip_calls_function_by_swapping_first_two_args():
    assert flip()(merge_three)(1, 2, 3) == [2, 1, 3]


def test_flip_returns_curried_function():
    assert flip(merge_three)(1, 2, 3) == [2, 1, 3]
    assert flip(merge_three)(1)(2)(3) == [2, 1, 3]
    assert flip(merge_three)(1, 2)(3) == [2, 1, 3]


def test_curry_flip_returns_curried_function():
    assert flip()(merge_three)(1, 2, 3) == [2, 1, 3]
    assert flip()(merge_three)(1)(2)(3) == [2, 1, 3]
    assert flip()(merge_three)(1, 2)(3) == [2, 1, 3]
    assert flip()(merge_three)(1)(2, 3) == [2, 1, 3]


def test_flip_does_not_flip_kwargs():
    assert flip(merge_three)(a=6, b=7, c=8) == [6, 7, 8]


def test_curry_flip_does_not_flip_kwargs():
    assert flip()(merge_three)(a=6, b=7, c=8) == [6, 7, 8]
