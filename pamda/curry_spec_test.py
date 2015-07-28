from functools import partial, wraps
from .curry_spec import *
from .private.assert_pred import assert_pred, true_case, false_case
from .private.assert_domain import assert_not_in_domain


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
