from pyramda.function.curry import curry


@curry
def dec(x):
    return x - 1
