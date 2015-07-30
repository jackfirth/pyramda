from .mean import mean
from pyramda.private.asserts import assert_equal


def mean_test():
    assert_equal(mean([3, 5, 7]), 5)
