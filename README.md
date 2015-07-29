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
