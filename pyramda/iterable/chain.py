from pyramda.function.curry import curry
from .map import map
from .reduce import reduce


@curry
def chain(f, xs):
    return reduce(lambda a, b: a + b, [], map(f, xs))
