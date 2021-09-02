"""average_of_numbers in list"""

from functools import reduce

def average_of_numbers(L_1):
    """this is average method"""
    return reduce(lambda a, b: a + b, L_1) / len(L_1)

L_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
RESULT = average_of_numbers(L_1)
print("average is", round(RESULT, 2))
