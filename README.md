# pyramda [![Build Status](https://travis-ci.org/jackfirth/pyramda.svg?branch=master)](https://travis-ci.org/jackfirth/pyramda) [![Coverage Status](https://coveralls.io/repos/jackfirth/pyramda/badge.svg?branch=master&service=github)](https://coveralls.io/github/jackfirth/pyramda?branch=master)

Python package supporting heavy functional programming through currying and function composition. Translation of the Ramda library from javascript to python. Supports Python 3.4 and above.

```
pip install pyramda
```

```python
>>> from pyramda import map, inc
>>> inc(1)
2
>>> map(inc, [1, 2, 3])
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
Reduction a = [a] -> a
```

Dictionary

```
getitem :: key : a -> Dictionary { key :: b | * } -> b
item_path :: (key : a ...) -> Dictionary { key :: Dictionary { ... :: b } | * } -> b
keys :: Dictionary a b -> [a]
map_dict :: (b -> c) -> Dictionary a b -> Dictionary a c
pick :: [a] -> Dictionary a b -> Dictionary a b
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
find :: Predicate a -> Reduction a
map :: (a -> b) -> [a] -> [b]
reduce :: (a -> b -> b) -> a -> [b] -> a
take :: Number -> [a] -> [a]
```

Logic

```
all_pass :: Reduction (Predicate a)
and_func :: Operation Boolean
any_pass :: Reduction (Predicate a)
both :: Operation (Predicate a)
complement :: Predicate a -> Predicate a
either :: Operation (Predicate a)
if_else :: Predicate a -> Operation (a -> a)
not_func :: Boolean -> Boolean
or_func :: Operation Boolean
```

Math

```
add :: Operation Number
dec :: Number -> Number
divide :: Operation Number
inc :: Number -> Number
mean :: Reduction Number
modulo :: Operation Number
multiply :: Operation Number
negate :: Number -> Number
product :: Reduction Number
subtract :: Operation Number
sum :: Reduction Number
```

Relation

```
equals :: a -> b -> Boolean
greater :: Ord a => Operation a
gt :: Ord a => Relation a
gte :: Ord a => Relation a
identical :: Relation a
lesser :: Ord a => Operation a
lt :: Ord a => Relation a
lte :: Ord a => Relation a
max :: Ord a => Reduction a
min :: Ord a => Reduction a
```

Other

```
getattr :: attr : String -> Object { attr :: a | * } -> a
isinstance :: Class -> Predicate a
```
