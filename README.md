# pamda [![Build Status](https://travis-ci.org/jackfirth/pamda.svg)](https://travis-ci.org/jackfirth/pamda)
Python package supporting heavy functional programming through currying

```python
>>> from pamda import map
>>> map(lambda x: x + 1, [1, 2, 3]
[2, 3, 4]
>>> add1Each = map(lambda x: x + 1)
>>> add1Each([1, 2, 3])
[2, 3, 4]
```

Provided functions:

```
add :: Number -> Number -> Number
compose :: (y -> z) ... (a -> b) -> a -> z
curry :: (a b ... -> z) -> a -> b -> ... -> z
equal :: a -> b -> Boolean
filter :: (a -> Boolean) -> [a] -> [a]
getattr :: attr:String -> Object { attr : a | * } -> a
getitem :: key:k -> Collection { key : v | * } -> v
isinstance :: Type -> a -> Boolean
map :: (a -> b) -> [a] -> [b]
reduce :: (a -> b -> b) -> a -> [b] -> a
```
