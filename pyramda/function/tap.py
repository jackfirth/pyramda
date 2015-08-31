from pyramda.function.curry import curry


@curry
def tap(f, v):
    f(v)
    return v
