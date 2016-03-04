from .pipe import pipe
from pyramda.private.asserts import assert_equal


def add10(x):
    return x + 10


def double(x):
    return x * 2


def sub2(x):
    return x - 2


def pipe_test():
    piped = pipe(
        sub2,
        double,
        add10
    )
    assert_equal(piped(100), (100-2)*2+10)
