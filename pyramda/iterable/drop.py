from pyramda.function.curry import curry


@curry
def drop(n, xs):
    return xs[n::]
