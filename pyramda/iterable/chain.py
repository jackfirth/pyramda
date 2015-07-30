from pyramda.function.curry import curry
from .map import map
from .concat import concat
from .reduce import reduce


@curry
def chain(f, xs):
    return reduce(concat, [], map(f, xs))
