from pyramda.function.curry import curry


@curry
def and_func(a, b):
    return a and b
