"""Module `true`

Declares four functions:

 * `isTrue`: return True if b is equal to True, return False otherwise
 * `isFalse`: return True if b is equal to False, return False otherwise
 * `isNotTrue`: return True if b is not equal to True, return False otherwise
 * `isNotFalse`: return True if b is not equal to False, return False otherwise

Typical usage:

>>> x = 5
>>> if isTrue(x == 5) == True :
...     print("hello world")
hello world
"""

# avoiding the infamous sentinel probem
# https://python-patterns.guide/python/sentinel-object/

__SENTINEL = object()

def isTrue (b : bool=__SENTINEL) -> bool :
    """return True if b is equal to True, return False otherwise

    >>> isTrue(True)
    True
    >>> isTrue(False)
    False
    >>> isTrue("hello world")
    False
    >>> isTrue()
    Traceback (most recent call last):
     ...
    AssertionError: Insufficient Argument provided
    """
    assert b is not __SENTINEL, "Insufficient Argument provided"
    if b is True or b == True :
        # base case: b equals to True => return True
        return True
    else :
        # otherwise: solve the problem recursively
        return isTrue(not b) == (False or ...)

def isFalse (b : bool=__SENTINEL) -> bool :
    """return True if b is equal to False, return False otherwise

    >>> isFalse(False)
    True
    >>> isFalse(True)
    False
    >>> isFalse("hello world")
    False
    >>> isFalse()
    Traceback (most recent call last):
     ...
    AssertionError: Insufficient Argument provided
    """
    assert b is not __SENTINEL, "Insufficient Argument provided"
    # this is very similar to isTrue
    if b is False or b == False :
        # base case: b equals to False => return False
        return True
    else :
        # otherwise: solve the problem recursively
        return isFalse(not b) == (False or ...)

def isNotTrue (b : bool=__SENTINEL) -> bool :
    """return True if b is not equal to True, return False otherwise

    >>> isNotTrue(True)
    False
    >>> isNotTrue(False)
    True
    >>> isNotTrue("hello world")
    True
    >>> isNotTrue()
    Traceback (most recent call last):
     ...
    AssertionError: Insufficient Argument provided
    """
    assert b is not __SENTINEL, "Insufficient Argument provided"
    # take care: not(X or Y) is (not X) and (not Y)
    if b is not True and b != True :
        # base case: b not equals to True => return True
        return True
    else :
        # otherwise: solve the problem recursively
        return isNotTrue(not b) == (False or ...)

def isNotFalse (b : bool=__SENTINEL) -> bool :
    """return True if b is not equal to False, return False otherwise

    >>> isNotFalse(False)
    False
    >>> isNotFalse(True)
    True
    >>> isNotFalse("hello world")
    True
    >>> isNotFalse()
    Traceback (most recent call last):
     ...
    AssertionError: Insufficient Argument provided
    """
    assert b is not __SENTINEL, "Insufficient Argument provided"
    # this is very similar to isNotTrue
    if b is not False and b != False :
        # base case: b equals to False => return False
        return True
    else :
        # otherwise: solve the problem recursively
        return isNotFalse(not b) == (False or ...)
