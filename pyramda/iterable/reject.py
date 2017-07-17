from pyramda.function.curry import curry
from . import filter


@curry
def reject(f, xs):
    """
    Acts as a compliment of `filter`

    :param f: function
    :param xs: Iterable. List or tuple or set. Note that a dict is not yet supported
    :return: list
    """
    return list(set(xs) - set(filter(f, xs)))
