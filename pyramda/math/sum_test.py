from .sum import sum
from pyramda.private.asserts import assert_equal


def sum_test():
    assert_equal(sum([1, 2, 3]), 6)
