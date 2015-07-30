from .pick import pick
from pyramda.private.asserts import assert_dicts_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

expected_dict = {
    "b": 2,
    "d": 4
}


def pick_nocurry_test():
    assert_dicts_equal(pick(["b", "d"], test_dict), expected_dict)


def pick_curry_test():
    pickBD = pick(["b", "d"])
    assert_dicts_equal(pickBD(test_dict), expected_dict)
