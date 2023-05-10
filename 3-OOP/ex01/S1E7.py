from S1E9 import Character


class Baratheon(Character):
    '''a simple class which inherits from Character.

    The __str__ and __repr__ functions are modified so that both return a string.'''

    def __init__(self, first_name, is_alive=True, family_name='Baratheon', eyes='Brown', hairs='dark') -> None:
        '''Initiate first_name and is_alive as provided.'''
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''The __str__ method which is the string representation of the class.'''
        return (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        '''The __repr__ method which is a more sophisticated  representation of the class.'''
        return (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def die(self):
        '''Function to set is_alive to False.'''
        self.is_alive = False


class Lannister(Character):
    '''A simple class which inherits from Character and has classmethod.

    The class method allows for a new Lannister object to be created through it.'''

    def __init__(self, first_name, is_alive=True, family_name='Lannister', eyes='Blue', hairs='light') -> None:
        '''Initiate first_name and is_alive as provided.'''
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''The __str__ method which is the string representation of the class.'''
        return (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        '''The __repr__ method which is a more sophisticated  representation of the class.'''
        return (f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')")

    def die(self):
        '''Function to set is_alive to False.'''
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True, family_name='Lannister', eyes='Blue', hairs='light'):
        '''A simple class method that takes the class as first argument and name as the second one.
        It takes the name and creates a new Lannister object and returns it.'''
        return (cls(first_name, is_alive, family_name, eyes, hairs))
