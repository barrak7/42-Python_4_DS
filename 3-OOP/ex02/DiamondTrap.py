from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True, family_name='Baratheon', eyes='Brown', hairs='dark') -> None:
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, eyes):
        self.eyes = eyes

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, hair):
        self.hairs = hair
