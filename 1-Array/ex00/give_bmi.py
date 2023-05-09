import numpy as np


def check_lsts(e) -> bool:
    '''check_lsts takes an object and checks whether it is of type int or float and returns Ture or False!'''

    if not isinstance(e, int) and not isinstance(e, float):
        return False
    return (True)


def give_bmi(height: list, weight: list) -> list:
    '''A function which takes two lists of identical sizes that contain heights and weights.

    It calculates the BMI of the two lists element wise using numpy and returns the result.'''

    if len(height) != len(weight) or not isinstance(height, list) or not isinstance(weight, list) or not all(map(check_lsts, height)) or not all(map(check_lsts, weight)):
        print("InsertionError: Invalid arguments provided!")
        return

    return list(np.divide(weight, np.power(height, 2)))


def sp_map(bmi: list, limit: int) -> list:
    '''A function alternative to map which iterates through each element of the list and applys a simple function to it.

    The result is stored in a list and returned.'''
    lst = []
    def x(a, l): return a > l
    for e in bmi:
        lst.append(x(e, limit))
    return lst


def apply_limit(bmi: list, limit: int):
    '''A function to check whether the elements of a bmi list are below the limit or not'''
    if not isinstance(limit, int) or not isinstance(bmi, list) or not all(map(check_lsts, bmi)):
        print("InsertionError: Invalid arguments provided!")
        return

    return sp_map(bmi, limit)


### TEST ###
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
