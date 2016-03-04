from functools import reduce


def pipe(*funcs):
    return lambda v: reduce(lambda accum, f: f(accum), funcs, v)
