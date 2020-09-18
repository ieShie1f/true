# The (in)famous `true.py`

Module `true` declares four functions:

 * `isTrue(b)`: return `True` if `b` is equal to `True`, return `False` otherwise
 * `isFalse(b)`: return `True` if `b` is equal to `False`, return `False` otherwise
 * `isNotTrue(b)`: return `True` if `b` is not equal to `True`, return `False` otherwise
 * `isNotFalse(b)`: return `True` if `b` is not equal to `False`, return `False` otherwise

## Typical usage

````python
>>> from true import *
>>> x = 5
>>> if isTrue(x == 5) == True :
...     print("hello world")
hello world
````

## Installation

No installation procedure yet, coming soon.
From now on, just copy `true.py` along with the other modules that import it.
You may need to make several copies but that fine:
it allows to use `from true import *` instead of something more complicated.
