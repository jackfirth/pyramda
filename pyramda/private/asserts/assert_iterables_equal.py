from .assert_equal import assert_equal, EqualAssertionError
from collections import Iterable


def is_iterable(v):
    return isinstance(v, Iterable)


def iterables_equal(iterable1, iterable2):
    return iterable1 == iterable2 or (
        is_iterable(iterable1) and
        is_iterable(iterable2) and
        all(map(iterables_equal, iterable1, iterable2))
    )


def assert_iterables_equal(actual_iterable, expected_iterable):
    if not iterables_equal(actual_iterable, expected_iterable):
        raise EqualAssertionError(actual_iterable, expected_iterable)
