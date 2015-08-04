from collections import namedtuple

CurrySpec = namedtuple('CurrySpec', 'arg_names arg_defaults')
ArgValues = namedtuple('ArgValues', 'args kwargs')


def num_args(arg_values):
    return len(arg_values.args) + len(arg_values.kwargs)


def num_positional_args(arg_values):
    return len(arg_values.args)


def num_curry_spec_args(curry_spec):
    return len(curry_spec.arg_names)


def num_curry_spec_default_args(curry_spec):
    return len(curry_spec.arg_defaults)


def num_default_overriding_args(curry_spec, arg_values):
    default_arg_names = set(curry_spec.arg_defaults.keys())
    kwarg_names = set(arg_values.kwargs.keys())
    return len(default_arg_names & kwarg_names)
