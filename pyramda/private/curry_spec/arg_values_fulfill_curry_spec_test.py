from functools import partial, wraps
from .arg_values_fulfill_curry_spec import arg_values_fulfill_curry_spec
from .curry_spec import ArgValues
from .make_func_curry_spec import make_func_curry_spec
from ..asserts import \
    assert_pred_cases, \
    true_case, \
    false_case, \
    assert_not_in_domain


def f(x, y, z=3):
    return x + y + z


def arg_values_fulfill_curry_spec_test():
    f_spec = make_func_curry_spec(f)
    arg_values_fulfill_f_spec = wraps(arg_values_fulfill_curry_spec)(
        partial(arg_values_fulfill_curry_spec, f_spec)
    )
    assert_pred_cases(
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
