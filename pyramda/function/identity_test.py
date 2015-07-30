from .identity import identity
from pyramda.private.asserts import assert_equal


def identity_test():
    assert_equal(identity(3), 3)
