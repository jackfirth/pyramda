from .remove_args_from_curry_spec import remove_args_from_curry_spec
from .make_func_curry_spec import make_func_curry_spec
from .curry_spec import CurrySpec, ArgValues
from ..asserts import assert_equal


def f(x, y, z=3):
    return x + y + z


def remove_args_from_curry_spec_test():
    f_spec = make_func_curry_spec(f)
    arg_values = ArgValues([1], {'z': 10})
    removed_spec = remove_args_from_curry_spec(f_spec, arg_values)
    assert_equal(removed_spec, CurrySpec(['y', 'z'], {'z': 10}))
