from .dec import dec
from pyramda.private.asserts import assert_equal


def dec_test():
    assert_equal(dec(5), 4)
