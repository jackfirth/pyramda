from inspect import getargspec
from .curry_spec import CurrySpec
from ..accepts_varargs import accepts_varargs


class CurrySpecVarargError(ValueError):
    def __init__(self, f):
        name = f.__name__
        message_template = "Cannot curry var-arg or var-kwarg function {0}"
        message = message_template.format(name)
        super(CurrySpecVarargError, self).__init__(message)


def func_arg_names(f):
    return getargspec(f).args


def func_arg_defaults(f):
    argspec = getargspec(f)
    arg_names = argspec.args
    default_arg_values = argspec.defaults or []
    num_defaults = len(default_arg_values)
    default_arg_names = arg_names[-num_defaults:]
    return dict(zip(default_arg_names, default_arg_values))


def make_func_curry_spec(f):
    if accepts_varargs(f):
        raise CurrySpecVarargError(f)
    return CurrySpec(func_arg_names(f), func_arg_defaults(f))
