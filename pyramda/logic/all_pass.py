from pyramda.function.curry import curry
from pyramda.function.always import always
from pyramda.iterable.reduce import reduce
from .both import both


@curry
def all_pass(ps, v):
    return reduce(both, always(True), ps)(v)
