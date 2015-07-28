from functools import partial, wraps
from .curry_spec import *
from .assert_pred import assert_pred, true_case, false_case
from .assert_domain import assert_not_in_domain


def assert_isinstance(type, v):
    assert isinstance(v, type)


def curry_spec_creation_test():
    assert_isinstance(CurrySpec, CurrySpec(['x', 'y', 'z'], {'y': 5}))


def num_args_test():
    assert num_args(ArgValues([1, 2], {'foo': 5, 'bar': 7, 'baz': 10})) == 5


def args_overlap_test():
    assert args_overlap(ArgValues([], {'foo': 1}), ArgValues([], {'foo': 10}))


def f(x, y, z=3):
    return x + y + z


def make_func_curry_spec_test():
    f_spec = make_func_curry_spec(f)
    assert f_spec == CurrySpec(['x', 'y', 'z'], {'z': 3})


def arg_values_fulfill_curry_spec_test():
    f_spec = make_func_curry_spec(f)
    arg_values_fulfill_f_spec = wraps(arg_values_fulfill_curry_spec)(
        partial(arg_values_fulfill_curry_spec, f_spec)
    )
    assert_pred(
        arg_values_fulfill_f_spec,
        true_case(ArgValues([1, 2, 3], {})),
        true_case(ArgValues([], {'x': 1, 'y': 2, 'z': 3})),
        true_case(ArgValues([1, 2], {})),
        true_case(ArgValues([], {'x': 1, 'y': 2})),
        true_case(ArgValues([1], {'y': 5})),
        false_case(ArgValues([1], {})),
        false_case(ArgValues([], {'x': 10})),
        false_case(ArgValues([1], {'z': 10}))
    )
    assert_not_in_domain(
        arg_values_fulfill_f_spec,
        ArgValues([1], {'x': 1})
    )
