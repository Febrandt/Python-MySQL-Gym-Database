
from dataclasses import dataclass
from typing import Optional
from MySQLdb import Date


#No ID means that the data is not yet in database

@dataclass
class Member:
    name: str
    email: str
    cpf: str
    telephone: str = None
    registration_date: Date = None
    id: int = None

@dataclass
class Payment:
    member_id: int
    month: int
    year: int
    payment_status: bool
    id: int = None
