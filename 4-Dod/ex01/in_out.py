def square(x: float) -> float:
    '''A function to calculate the square of a number.

    returns: the square of x.'''
    return (x**2)


def pow(x: float) -> float:
    '''A function which raises x to the power of itself.

    returns: x^x'''
    return x**x


def outer(x: float, function) -> object:
    def inner() -> float:
        nonlocal x
        x = function(x)
        return x
    return inner
