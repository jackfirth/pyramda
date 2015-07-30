from pyramda.function.curry import curry


@curry
def mean(xs):
    return sum(xs) / len(xs)
