from pyramda.function.curry import curry


@curry
def multiply(x, y):
    return x * y
