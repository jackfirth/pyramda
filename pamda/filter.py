from .curry import curry


filter = curry(lambda p, xs: [x for x in xs if p(x)])
