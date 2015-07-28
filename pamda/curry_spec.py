from collections import namedtuple
from inspect import getargspec

CurrySpec = namedtuple('CurrySpec', 'arg_names arg_defaults')
ArgValues = namedtuple('ArgValues', 'args kwargs')


class CurrySpecVarargError(ValueError):
    def __init__(self, f):
        name = f.__name__
        message_template = "Cannot curry vararg or varkwarg function {0}"
        message = message_template.format(name)
        super(CurrySpecVarargError, self).__init__(message)


def num_args(arg_values):
    return len(arg_values.args) + len(arg_values.kwargs)


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
