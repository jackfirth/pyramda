from pyramda.function.curry import curry


map = curry(lambda f, xs: [f(x) for x in xs])
