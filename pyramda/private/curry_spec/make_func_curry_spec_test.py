from .make_func_curry_spec import make_func_curry_spec
from .curry_spec import CurrySpec
from ..asserts import assert_equal


def f(x, y, z=3):
    return x + y + z


def make_func_curry_spec_test():
    f_spec = make_func_curry_spec(f)
    assert_equal(f_spec, CurrySpec(['x', 'y', 'z'], {'z': 3}))
