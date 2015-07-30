from .curry import *
from .curry import CurrySpec
from pyramda.private.asserts import assert_equal, assert_not_equal


def f(x, y, z=3):
    return x + y + z


def run_f_curry_cases(fc):
    assert_equal(fc(1, 1, 1), 3)
    assert_equal(fc(1, 1), 5)
    assert_equal(fc(1)(1), 5)
    assert_equal(fc(1)(1, 1), 3)
    assert_equal(fc(x=1, y=1, z=1), 3)
    assert_equal(fc(x=1, y=1), 5)
    assert_equal(fc(1)(y=1, z=1), 3)
    assert_equal(fc(1)(y=1), 5)
    assert_equal(fc(z=10)(1, 1), 12)
    assert_equal(fc(y=10)(1), 14)


def curry_by_spec_test():
    curry_spec = CurrySpec(['x', 'y', 'z'], {'z': 3})
    fc = curry_by_spec(curry_spec, f)
    run_f_curry_cases(fc)


def curry_test():
    fc = curry(f)
    run_f_curry_cases(fc)
