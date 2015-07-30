from .curry import curry


@curry
def apply(f, args):
    return f(*args)
