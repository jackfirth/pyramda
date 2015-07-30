from pyramda.function.curry import curry
from pyramda.function.always import always
from pyramda.iterable.reduce import reduce
from .either import either


@curry
def any_pass(ps, v):
    return reduce(either, always(False), ps)(v)
