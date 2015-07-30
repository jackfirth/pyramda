from .if_else import if_else
from pyramda.math.inc import inc
from pyramda.math.dec import dec
from pyramda.private.asserts import assert_equal


def positive(x):
    return x > 0


def if_else_nocurry_test():
    assert_equal(if_else(positive, inc, dec, 5), 6)
    assert_equal(if_else(positive, inc, dec, -5), -6)


def if_else_curry_test():
    inc_away_from_zero = if_else(positive, inc, dec)
    assert_equal(inc_away_from_zero(5), 6)
    assert_equal(inc_away_from_zero(-5), -6)
