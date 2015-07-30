from pyramda.function.curry import curry


@curry
def find(p, xs):
    for found in (x for x in xs if p(x)):
        return found
