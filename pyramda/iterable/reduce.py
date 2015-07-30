from pyramda.function.curry import curry
from functools import reduce as uncurried_reduce


@curry
def reduce(operator, init, vs):
    return uncurried_reduce(operator, vs, init)
