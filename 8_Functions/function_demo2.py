"""
Scope
1. Local
2. Global
"""

# static value
a = 50
b = 10


def summation():
    result = a + b  # global scope
    print(result)


def subtraction():
    c = 100  # local scope
    d = 20
    result = c - d
    print(result)


summation()
