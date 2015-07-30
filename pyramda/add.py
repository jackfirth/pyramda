from pyramda.function.curry import curry


@curry
def add(x, y):
    return x + y
