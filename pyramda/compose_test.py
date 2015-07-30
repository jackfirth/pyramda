from .compose import compose
from .private.asserts import assert_equal


def add10(x):
    return x + 10


def double(x):
    return x * 2


def sub2(x):
    return x - 2


def compose_test():
    composed = compose(
        sub2,
        double,
        add10
    )
    assert_equal(composed(100), 218)
