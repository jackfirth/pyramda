from pyramda.function.curry import curry
import builtins


@curry
def sum(xs):
    return builtins.sum(xs)
