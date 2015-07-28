from .private.min_index import min_index
from .curry_spec import \
    num_args, \
    num_curry_spec_args, \
    num_curry_spec_default_args, \
    num_default_overriding_args, \
    num_positional_args


def has_extra_kwargs(curry_spec, kwargs):
    return len(kwargs.keys() - curry_spec.arg_names) > 0


def arg_values_invalid(curry_spec, arg_values):
    if not arg_values.kwargs:
        return False
    min_kwarg_index = min_index(curry_spec.arg_names, arg_values.kwargs.keys())
    return min_kwarg_index < num_positional_args(arg_values)


def arg_values_fulfill_curry_spec(curry_spec, arg_values):
    if arg_values_invalid(curry_spec, arg_values):
        template = "Keyword args {0} and positional args {1} overlap for " + \
            "arg names {2}"
        message = template.format(
            arg_values.kwargs,
            arg_values.args,
            curry_spec.arg_names
        )
        raise ValueError(message)
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
