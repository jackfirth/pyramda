from pyramda.function.curry import curry


@curry
def find(p, xs):
    for found in (x for x in xs if p(x)):
        return found
    raise ValueError(
        "Expected a list such that at least one item would satisfy " +
        "{0}, got {1}".format(p, xs)
    )
