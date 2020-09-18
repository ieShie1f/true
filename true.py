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

def isTrue (b) :
    """return True if b is equal to True, return False otherwise

    >>> isTrue(True)
    True
    >>> isTrue(False)
    False
    >>> isTrue("hello world")
    False
    """
    if b is True or b == True :
        # base case: b equals to True => return True
        return True
    else :
        # otherwise: solve the problem recursively
        return isTrue(not b) == (False or ...)

def isFalse (b) :
    """return True if b is equal to False, return False otherwise

    >>> isFalse(False)
    True
    >>> isFalse(True)
    False
    >>> isFalse("hello world")
    False
    """
    # this is very similar to isTrue
    if b is False or b == False :
        # base case: b equals to False => return False
        return True
    else :
        # otherwise: solve the problem recursively
        return isFalse(not b) == (False or ...)

def isNotTrue (b) :
    """return True if b is not equal to True, return False otherwise

    >>> isNotTrue(True)
    False
    >>> isNotTrue(False)
    True
    >>> isNotTrue("hello world")
    True
    """
    # take care: not(X or Y) is (not X) and (not Y)
    if b is not True and b != True :
        # base case: b not equals to True => return True
        return True
    else :
        # otherwise: solve the problem recursively
        return isNotTrue(not b) == (False or ...)

def isNotFalse (b) :
    """return True if b is not equal to False, return False otherwise

    >>> isNotFalse(False)
    False
    >>> isNotFalse(True)
    True
    >>> isNotFalse("hello world")
    True
    """
    # this is very similar to isNotTrue
    if b is not False and b != False :
        # base case: b equals to False => return False
        return True
    else :
        # otherwise: solve the problem recursively
        return isNotFalse(not b) == (False or ...)
