from ..min_index import min_index
from .curry_spec import num_positional_args


def arg_values_invalid(curry_spec, arg_values):
    if not arg_values.kwargs:
        return False
    min_kwarg_index = min_index(curry_spec.arg_names, arg_values.kwargs.keys())
    return min_kwarg_index < num_positional_args(arg_values)


def check_arg_values_valid(curry_spec, arg_values):
    if arg_values_invalid(curry_spec, arg_values):
        template = "Keyword args {0} and positional args {1} overlap for " + \
            "arg names {2}"
        message = template.format(
            arg_values.kwargs,
            arg_values.args,
            curry_spec.arg_names
        )
        raise ValueError(message)
