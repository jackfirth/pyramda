from .curry import curry
import builtins


isinstance = curry(lambda type, v: builtins.isinstance(v, type))
