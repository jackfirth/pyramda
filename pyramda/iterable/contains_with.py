from pyramda.function.curry import curry
from .any_satisfy import any_satisfy
from functools import partial


@curry
def contains_with(is_equal, x, xs):
    is_equal_to_x = partial(is_equal, x)
    return any_satisfy(is_equal_to_x, xs)
