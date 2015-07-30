from pyramda.function.curry import curry


@curry
def subtract(x, y):
    return x - y
