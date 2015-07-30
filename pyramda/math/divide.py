from pyramda.function.curry import curry


@curry
def divide(x, y):
    return x / y
