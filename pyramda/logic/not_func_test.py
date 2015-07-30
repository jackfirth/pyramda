from .not_func import not_func


def not_func_test():
    assert not not_func(True)
    assert not_func(False)
