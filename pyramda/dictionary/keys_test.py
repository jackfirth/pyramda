from .keys import keys
from pyramda.private.asserts import assert_iterables_equal


test_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}


def keys_test():
    assert_iterables_equal(keys(test_dict), set(["a", "c", "b"]))
