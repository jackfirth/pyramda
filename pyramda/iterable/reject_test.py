from . import reject


def test_reject_filters_out_unwanted_items_in_iterable():
    assert reject(lambda x: x % 2 == 1, [1, 2, 3, 4]) == [2, 4]


def test_curry_reject_filters_out_unwanted_items_in_iterable():
    assert reject(lambda x: x % 2 == 1)([1, 2, 3, 4]) == [2, 4]


def test_reject_does_not_remove_duplicates():
    assert reject(lambda x: x % 2 == 1, [1, 2, 3, 4, 4]) == [2, 4, 4]


def test_curry_reject_does_not_remove_duplicates():
    assert reject(lambda x: x % 2 == 1)([1, 2, 3, 4, 4]) == [2, 4, 4]
