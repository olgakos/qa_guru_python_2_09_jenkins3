from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Kos'
    email: str = 'test@test.com'
    user_number: str = '0123456789'
    birth_day: str = '01'
    birth_month: str = 'January'
    birth_year: str = '2000'
    subjects: Tuple[Subject] = (Subject.History,)
    current_address: str = 'St.Petegburg'
    hobbies: Tuple[Hobby] = (Hobby.Reading,)
    picture_file: str = 'siegfriedsassoon.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


student = User(name='Olga', gender=Gender.Female)
