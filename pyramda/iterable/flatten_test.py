from .flatten import flatten


def test_flattens_all_nested_lists():
    assert flatten([1, 2, [3, 4], 5, [6, [7, 8, [9, [10, 11], 12]]]]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def test_curry_flattens_all_nested_lists():
    assert flatten()([1, 2, [3, 4], 5, [6, [7, 8, [9, [10, 11], 12]]]]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def test_flatten_returns_non_iterable_as_is():
    assert flatten(1) == [1]


def test_curry_flatten_returns_non_iterable_as_is():
    assert flatten()(1) == [1]


def test_flatten_does_not_split_string_into_a_list_of_characters():
    assert flatten('Hello World') == ['Hello World']


def test_curry_flatten_does_not_split_string_into_a_list_of_characters():
    assert flatten()('Hello World') == ['Hello World']


def test_flatten_does_not_get_stuck_in_infinite_recursion_with_strings():
    assert flatten(
        [1, 2, ['Hello', 'World'], 5, [6, [7, 8, [9, [10, 11], 12]]]]) == [1, 2, 'Hello', 'World',
                                                                           5, 6, 7, 8, 9, 10, 11, 12
                                                                           ]


def test_curry_flatten_does_not_get_stuck_in_infinite_recursion_with_strings():
    assert flatten()(
        [1, 2, ['Hello', 'World'], 5,
         [6, [7, 8, [9, [10, 11], 12]]]]) == [1, 2, 'Hello', 'World',
                                              5, 6, 7, 8, 9, 10, 11, 12
                                              ]
