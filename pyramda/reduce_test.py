from .reduce import reduce
from .private.asserts import assert_equal


def string_append(s1, s2):
    return s1 + s2


def reduce_nocurry_test():
    assert_equal(reduce(string_append, "", ["aa", "bb", "cc"]), "aabbcc")


def reduce_curry_test():
    assert_equal(reduce(string_append, "")(["aa", "bb", "cc"]), "aabbcc")
