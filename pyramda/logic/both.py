from pyramda.function.curry import curry


@curry
def both(p1, p2, v):
    return p1(v) and p2(v)
