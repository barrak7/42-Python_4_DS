from abc import ABC, abstractmethod


class Character(ABC):
    '''A class which initializes a character with a name and a state.
    The state is set to True by default.

    It also has an abstract method which allows for the state to be sat to False.'''

    def __init__(self, first_name, is_alive=True) -> None:
        '''Simply construct the first_name and is_alive values as provided.
        is_alive variable does have a default value of True.'''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        '''An abstract method which every child can have a different implementation of.'''
        pass


class Stark(Character):
    '''A child class which inherits from the class Character.'''

    def __init__(self, first_name, is_alive=True) -> None:
        '''Child's constructor calls the parent's init function.'''
        super().__init__(first_name, is_alive)

    def die(self):
        '''Spark's own implementation of the die function as it is an abstract method in the Parent class.'''
        self.is_alive = False
