from .assert_equal import assert_equal, EqualAssertionError


def is_dict(v):
    return isinstance(v, dict)


def dicts_equal(dict1, dict2):
    return dict1 == dict2 or (
        is_dict(dict1) and
        is_dict(dict2) and
        all(map(lambda x, y: x == y, dict1.keys(), dict2.keys())) and
        all(map(dicts_equal, dict1.values(), dict2.values()))
    )


def assert_dicts_equal(actual_dict, expected_dict):
    if not dicts_equal(actual_dict, expected_dict):
        raise EqualAssertionError(actual_dict, expected_dict)
