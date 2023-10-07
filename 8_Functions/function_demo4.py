"""
parameter: are variables that we specify inside parentheses at the time of function definition.
argument: the values that are passed for the parameters when calling the function.
"""


def summation(a, b):
    return a + b


def subtraction(a, b):
    return a - b


print(summation(100, 300))

result = summation(100,20) + subtraction(100, 50)
print(result)

