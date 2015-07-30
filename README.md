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

Type Synonyms

```
Predicate a = a -> Boolean
Relation a = a -> a -> Boolean
Operation a = a -> a -> a
```

Dictionary

```
getitem :: key : a -> Dictionary { key :: b | * } -> b
keys :: Dictionary a b -> [a]
map_dict :: (b -> c) -> Dictionary a b -> Dictionary a c
values :: Dictionary a b -> [b]
```

Function

```
always :: a -> b -> a
apply :: (a -> ... -> z) -> (a, ...) -> z
compose :: (y -> z) ... (a -> b) -> a -> z
curry :: (a b ... -> z) -> a -> b -> ... -> z
identity :: a -> a
```

Iterable

```
all_satisfy :: Predicate a -> Predicate [a]
any_satisfy :: Predicate a -> Predicate [a]
chain :: (a -> [b]) -> [a] -> [b]
concat :: Operation [a]
cons :: a -> [a] -> [a]
contains :: a -> Predicate [a]
contains_with :: Relation a -> a -> Predicate [a]
drop :: Number -> [a] -> [a]
filter :: Predicate a -> [a] -> [a]
find :: Predicate a -> [a] -> a
map :: (a -> b) -> [a] -> [b]
reduce :: (a -> b -> b) -> a -> [b] -> a
take :: Number -> [a] -> [a]
```

Logic

```
both :: Operation (Predicate a)
complement :: Predicate a -> Predicate a
either :: Operation (Predicate a)
```

Math

```
add :: Operation Number
dec :: Number -> Number
divide :: Operation Number
inc :: Number -> Number
mean :: [Number] -> Number
modulo :: Operation Number
multiply :: Operation Number
negate :: Number -> Number
product :: [Number] -> Number
subtract :: Operation Number
sum :: [Number] -> Number
```

Relation

```
equals :: a -> b -> Boolean
gt :: Ord a => Relation a
gte :: Ord a => Relation a
identical :: Relation a
lt :: Ord a => Relation a
lte :: Ord a => Relation a
```

Other

```
getattr :: attr : String -> Object { attr :: a | * } -> a
isinstance :: Class -> Predicate a
```
