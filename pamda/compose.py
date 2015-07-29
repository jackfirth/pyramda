from functools import reduce


def compose(*funcs):
    return lambda v: reduce(lambda accum, f: f(accum), funcs[::-1], v)
