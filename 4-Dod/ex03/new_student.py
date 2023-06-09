import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    id: str = field(init=False)
    login: str = field(init=False)
    active: bool = True

    def __post_init__(self):
        self.id = generate_id()
        self.login = f"{self.name[0]}{self.surname}"
