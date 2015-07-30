from pyramda.function.curry import curry


@curry
def any_satisfy(p, xs):
    return any(map(p, xs))
