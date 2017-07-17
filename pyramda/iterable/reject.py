from pyramda.function.curry import curry
from . import filter


@curry
def reject(f, xs):
    """
    Acts as a compliment of `filter`

    :param f: function
    :param xs: Iterable. A sequence, a container which supports iteration or an iterator
    :return: list
    """
    return list(set(xs) - set(filter(f, xs)))
