from .complement import complement


def positive(x):
    return x > 0


def complement_nocurry_test():
    assert complement(positive, 0)
    assert complement(positive, -5)
    assert not complement(positive, 5)


def complement_curry_test():
    nonpositive = complement(positive)
    assert nonpositive(0)
    assert nonpositive(-5)
    assert not nonpositive(5)
