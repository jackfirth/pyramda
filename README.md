# pyramda [![Build Status](https://travis-ci.org/jackfirth/pyramda.svg?branch=master)](https://travis-ci.org/jackfirth/pyramda)
Python package supporting heavy functional programming through currying and function composition. Translation of the Ramda library from javascript to python. Currently only Python 3 is supported.

```python
>>> from pyramda import map, inc
>>> inc(1)
2
>>> map(inc, [1, 2, 3]
[2, 3, 4]
>>> incEach = map(inc)
>>> incEach([1, 2, 3])
[2, 3, 4]
```

### Provided functions

Function

```
apply :: (a -> ... -> z) -> (a, ...) -> z
compose :: (y -> z) ... (a -> b) -> a -> z
curry :: (a b ... -> z) -> a -> b -> ... -> z
```

Iterable

```
all_satisfy :: Predicate a -> [a] -> Boolean
filter :: Predicate a -> [a] -> [a]
map :: (a -> b) -> [a] -> [b]
reduce :: (a -> b -> b) -> a -> [b] -> a
```

Math

```
add :: Number -> Number -> Number
dec :: Number -> Number
divide :: Number -> Number -> Number
inc :: Number -> Number
mean :: [Number] -> Number
modulo :: Number -> Number -> Number
multiply :: Number -> Number -> Number
negate :: Number -> Number
product :: [Number] -> Number
subtract :: Number -> Number -> Number
sum :: [Number] -> Number
```

Other

```
equal :: a -> b -> Boolean
getattr :: attr : String -> Object { attr :: a | * } -> a
getitem :: key : k -> Collection { key :: v | * } -> v
isinstance :: Class -> Predicate a
```
