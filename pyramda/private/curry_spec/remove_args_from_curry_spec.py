from .curry_spec import CurrySpec
from .check_arg_values_valid import check_arg_values_valid


def remove_args_from_curry_spec(curry_spec, arg_values):
    check_arg_values_valid(curry_spec, arg_values)
    arg_names, arg_defaults = curry_spec
    args, kwargs = arg_values
    new_arg_defaults = arg_defaults.copy()
    new_arg_defaults.update(kwargs)
    new_arg_names = arg_names[len(args):]
    return CurrySpec(new_arg_names, new_arg_defaults)
