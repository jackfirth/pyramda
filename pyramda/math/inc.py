from pyramda.function.curry import curry


@curry
def inc(x):
    return x + 1
