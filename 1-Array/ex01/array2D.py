import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''A function which takes a 2d list and slices it from "start" to "end".

    It then prints the original shape and the new shape. It returns the new array.'''

    if not isinstance(family, list) or not isinstance(start, int) or not isinstance(end, int):
        print("AssertionError: Invalid arguments provided!")
        return

    family = np.array(family)
    try:
        new = family[start:][end:]
    except:
        print("AssertionError: Start or End not compatible with the shape of the array")
        return

    print(f"My shape is : {family.shape}")
    print(f"My new shape is : {new.shape}")
    return new.tolist()


### TEST ###
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
