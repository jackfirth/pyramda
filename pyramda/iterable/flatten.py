from collections import Iterable
from past.builtins import basestring

from pyramda.function.curry import curry


@curry
def flatten(xs, depth):
    """
    Flatten a nested  sequence. A sequence could be a nested list of lists
    or tuples or a combination of both

    :param xs: Iterable. Nested lists or tuples
    :param depth: int or None. Recursion depth.
    :return: list.
    """

    def _flatten(x, d):
        for item in x:
            if isinstance(
                    item, Iterable) and not isinstance(
                    item, basestring) and (
                    d is None or d >= 1):
                for i in flatten(item, d - 1 if d else None):
                    yield i
            else:
                yield item

    return list(
        _flatten(
            xs,
            depth)) if (
        isinstance(
            xs,
            Iterable) and not isinstance(
            xs,
            basestring)) else xs
