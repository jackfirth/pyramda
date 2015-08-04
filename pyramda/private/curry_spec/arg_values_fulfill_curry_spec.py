from ..min_index import min_index
from .curry_spec import \
    num_args, \
    num_curry_spec_args, \
    num_curry_spec_default_args, \
    num_default_overriding_args, \
    num_positional_args
from .check_arg_values_valid import check_arg_values_valid


def has_extra_kwargs(curry_spec, kwargs):
    return len(set(kwargs.keys()) - set(curry_spec.arg_names)) > 0


def arg_values_fulfill_curry_spec(curry_spec, arg_values):
    check_arg_values_valid(curry_spec, arg_values)
    if has_extra_kwargs(curry_spec, arg_values.kwargs):
        return False

    n_args = num_args(arg_values)
    n_curry_args = num_curry_spec_args(curry_spec)
    n_curry_default_args = num_curry_spec_default_args(curry_spec)
    n_default_overriding_args = num_default_overriding_args(
        curry_spec,
        arg_values
    )

    n_min_curry_args = n_curry_args - n_curry_default_args

    return (
        n_min_curry_args <= n_args - n_default_overriding_args <= n_curry_args
    )
