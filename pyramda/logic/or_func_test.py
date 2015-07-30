from .or_func import or_func


def or_func_test():
    assert or_func(True, True)
    assert or_func(True, False)
    assert or_func(False, True)
    assert not or_func(False, False)
