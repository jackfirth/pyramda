from pyramda.function.curry import curry
from pyramda.logic import complement
from . import filter


@curry
def reject(p, xs):
    """
    Acts as a complement  of `filter`

    :param p: predicate
    :param xs: Iterable. A sequence, a container which supports iteration or an iterator
    :return: list
    """
    return filter(complement(p), xs)
