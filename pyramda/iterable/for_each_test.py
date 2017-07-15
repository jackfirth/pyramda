try:
    # Python 3
    from unittest import mock
except ImportError:
    # Python 2
    import mock

from .for_each import for_each


def test_for_each_nocurry_returns_the_original_iterable():
    assert for_each(mock.MagicMock(), [1, 2, 3]) == [1, 2, 3]


def test_for_each_curry_returns_the_original_iterable():
    assert for_each(mock.MagicMock())([1, 2, 3]) == [1, 2, 3]


def test_for_each_nocurry_executed_function_for_each_item_in_the_iterable():
    m = mock.MagicMock()
    for_each(m, ([1, 2, 3])) == [1, 2, 3]
    assert len(m.mock_calls) == 3


def test_for_each_curry_executed_function_for_each_item_in_the_iterable():
    m = mock.MagicMock()
    for_each(m)([1, 2, 3]) == [1, 2, 3]
    assert len(m.mock_calls) == 3
