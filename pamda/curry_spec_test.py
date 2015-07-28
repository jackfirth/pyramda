from functools import partial, wraps
from .curry_spec import *


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


def true_case(v):
    return (v, True)


def false_case(v):
    return (v, False)


class PredicateCaseAssertionError(AssertionError):
    def __init__(self, expected, pred, v):
        name = pred.__name__
        v_str = str(v)
        message_template = "Expected predicate {0} to be {1} for input {2}"
        message = message_template.format(name, expected, v_str)
        super(PredicateCaseAssertionError, self).__init__(message)


class PredicateFalseCaseAssertionError(PredicateCaseAssertionError):
    def __init__(self, pred, v):
        super(PredicateFalseCaseAssertionError, self).__init__(False, pred, v)


class PredicateTrueCaseAssertionError(PredicateCaseAssertionError):
    def __init__(self, pred, v):
        super(PredicateTrueCaseAssertionError, self).__init__(True, pred, v)


def assert_pred(pred, *cases):
    for v, expected in cases:
        pv = pred(v)
        if pv and not expected:
            raise PredicateFalseCaseAssertionError(pred, v)
        if not pv and expected:
            raise PredicateTrueCaseAssertionError(pred, v)


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
