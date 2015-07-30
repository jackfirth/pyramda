from pyramda.function.curry import curry


@curry
def modulo(x, y):
    return x % y
