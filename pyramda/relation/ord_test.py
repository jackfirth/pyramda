from .ord import lt, gt, lte, gte


def lt_test():
    assert lt(3, 2)
    assert not lt(2, 3)
    assert not lt(3, 3)


def gt_test():
    assert gt(2, 3)
    assert not gt(3, 2)
    assert not gt(2, 2)


def lte_test():
    assert lte(3, 2)
    assert not lte(2, 3)
    assert lte(3, 3)


def gte_test():
    assert gte(2, 3)
    assert not gte(3, 2)
    assert gte(3, 3)
