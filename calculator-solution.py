def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def divide(x, y):
    if x==0 or y==0:
        return print("Invalid value for denominator, cant't divide by 0!")
    return x/y


def multiply(x, y):
    return x*y


def square(x):
    return x**3


def power(x, y):
    return x**y

import math
def sqrt(x):
    return math.sqrt(x)
