from collections import Iterable
from pyramda.isinstance import isinstance
from pyramda.function.curry import curry
from builtins import str


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
        if isinstance(Iterable, items) and not is_leaf(items):
            for item in items:
                for i in _flatten_until(item):
                    yield i
        else:
            yield items

    return list(_flatten_until(xs))

flatten = flatten_until(isinstance(str))
