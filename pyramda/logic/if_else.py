from pyramda.function.curry import curry


@curry
def if_else(p, then_func, else_func, v):
    return then_func(v) if p(v) else else_func(v)
