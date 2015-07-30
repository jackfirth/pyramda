from pyramda.function.curry import curry


@curry
def lt(y, x):
    return x < y


@curry
def gt(y, x):
    return x > y


@curry
def lte(y, x):
    return x <= y


@curry
def gte(y, x):
    return x >= y
