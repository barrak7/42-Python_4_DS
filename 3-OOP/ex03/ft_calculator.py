class calculator:
    '''A simple calculator class which can be used to perform operations
    between a vector and a scalar such as add, multiply, subtract and divide.
    '''

    def __init__(self, vector: list) -> None:
        self.vector = vector

    def __add__(self, object) -> None:
        for i, element in enumerate(self.vector):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        for i, element in enumerate(self.vector):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        for i, element in enumerate(self.vector):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Can't divide by 0.")
            return
        for i, element in enumerate(self.vector):
            self.vector[i] /= object
        print(self.vector)
