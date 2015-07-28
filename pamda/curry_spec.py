from collections import namedtuple

CurrySpec = namedtuple('CurrySpec', 'arg_names arg_defaults')
ArgValues = namedtuple('ArgValues', 'args kwargs')


def num_args(arg_values):
    return len(arg_values.args) + len(arg_values.kwargs)


def args_overlap(arg_values1, arg_values2):
    return dict_overlap(arg_values1.kwargs, arg_values2.kwargs)


def dict_overlap(dict1, dict2):
    return len(dict1.keys() & dict2.keys()) > 0
