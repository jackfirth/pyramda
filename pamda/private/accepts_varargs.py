from inspect import getargspec


def argspec_has_varargs(argspec):
    return argspec.varargs is not None or argspec.keywords is not None


def accepts_varargs(f):
    return argspec_has_varargs(getargspec(f))
