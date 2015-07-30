from .and_func import and_func


def and_func_test():
    assert and_func(True, True)
    assert not and_func(True, False)
    assert not and_func(False, True)
    assert not and_func(False, False)
