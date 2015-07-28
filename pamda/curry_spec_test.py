from curry_spec import *


def curry_spec_creation_test():
    assert CurrySpec(['x', 'y', 'z'] {'y': 5}) isinstance CurrySpec


def num_args_test():
    assert num_args(ArgValues([1, 2], {'foo': 5, 'bar': 7, 'baz': 10})) == 3


def args_overlap_test():
    assert args_overlap(ArgValues([], {'foo': 1}), ArgValues([], {'foo': 10}))
