from .modulo import modulo
from pyramda.private.asserts import assert_equal


def modulo_nocurry_test():
    assert_equal(modulo(12, 5), 2)
    assert_equal(modulo(-12, 5), 3)


def modulo_curry_test():
    assert_equal(modulo(12)(5), 2)
