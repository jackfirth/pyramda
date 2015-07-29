from inspect import getargspec
from .curry_spec import CurrySpec, CurrySpecVarargError
from ..accepts_varargs import accepts_varargs


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
    if accepts_varargs(f):
        raise CurrySpecVarargError(f)
    return CurrySpec(func_arg_names(f), func_arg_defaults(f))
