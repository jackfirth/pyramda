from pyramda.function.curry import curry
from pyramda.iterable.reduce import reduce
from .multiply import multiply


product = reduce(multiply, 1)
