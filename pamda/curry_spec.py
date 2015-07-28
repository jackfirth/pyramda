from collections import namedtuple
from inspect import getargspec
from .private.min_index import min_index

CurrySpec = namedtuple('CurrySpec', 'arg_names arg_defaults')
ArgValues = namedtuple('ArgValues', 'args kwargs')


class CurrySpecVarargError(ValueError):
    def __init__(self, f):
        name = f.__name__
        message_template = "Cannot curry var-arg or var-kwarg function {0}"
        message = message_template.format(name)
        super(CurrySpecVarargError, self).__init__(message)


def num_args(arg_values):
    return len(arg_values.args) + len(arg_values.kwargs)


def num_positional_args(arg_values):
    return len(arg_values.args)


def num_curry_spec_args(curry_spec):
    return len(curry_spec.arg_names)


def num_curry_spec_default_args(curry_spec):
    return len(curry_spec.arg_defaults)


def num_default_overriding_args(curry_spec, arg_values):
    return len(curry_spec.arg_defaults.keys() & arg_values.kwargs.keys())


def args_overlap(arg_values1, arg_values2):
    return dict_overlap(arg_values1.kwargs, arg_values2.kwargs)


def dict_overlap(dict1, dict2):
    return len(dict1.keys() & dict2.keys()) > 0


def argspec_has_varargs(argspec):
    return argspec.varargs is not None or argspec.keywords is not None


def func_accepts_varargs(f):
    return argspec_has_varargs(getargspec(f))


def func_arg_names(f):
    return getargspec(f).args


def func_arg_defaults(f):
    argspec = getargspec(f)
    arg_names = argspec.args
    default_arg_values = argspec.defaults
    num_defaults = len(default_arg_values)
    default_arg_names = arg_names[-num_defaults:]
    return dict(zip(default_arg_names, default_arg_values))


def make_func_curry_spec(f):
    if func_accepts_varargs(f):
        raise CurrySpecVarargError(f)
    return CurrySpec(func_arg_names(f), func_arg_defaults(f))


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
