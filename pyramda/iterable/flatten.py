from collections import Iterable
from past.builtins import basestring

from pyramda.isinstance import isinstance
from pyramda.function.curry import curry


@curry
def flatten_until(is_leaf, xs):
    """
    Flatten a nested  sequence. A sequence could be a nested list of lists
    or tuples or a combination of both

    :param is_leaf: Predicate. Predicate to  determine whether an item
                    in the iterable `xs` is a leaf node or not.
    :param xs: Iterable. Nested lists or tuples
    :return: list.
    """

    def _flatten_until(items):
        for item in items:
            if isinstance(Iterable, item) and not is_leaf(item):
                for i in _flatten_until(item):
                    yield i
            else:
                yield item

    return list(_flatten_until(xs)) if isinstance(Iterable, xs) and not is_leaf(xs) else xs

flatten = flatten_until(isinstance(basestring))
