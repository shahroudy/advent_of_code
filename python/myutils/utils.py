import operator
from functools import reduce


def multiply(elements):
    return reduce(operator.mul, elements, 1)


# Example usage
assert multiply([1, 2, 3, 4, 5]) == 120
