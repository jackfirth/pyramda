from pyramda.function.curry import curry
from . import filter


@curry
def reject(p, xs):
    """
    Acts as a complement  of `filter`

    :param p: predicate
    :param xs: Iterable. A sequence, a container which supports iteration or an iterator
    :return: list
    """
    return list(set(xs) - set(filter(p, xs)))
