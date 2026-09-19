# Database models ??

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    #password_hash = Column(String(256), nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"<User {self.name!r}>"

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    user = Column(String(20))
    # type: full art, holo, reverse holo, regular, ex
    # number out of number
    pokedex_id = Column(Integer)
    first_num = Column(Integer)
    second_num = Column(Integer)
    # set: chaos rising, scarlet violet, etc. These have symbols too
    set_name = Column(String(70))
    count = Column(Integer)
    # image - add a web scraper that searches for the images based on the information

    def __init__(self, name=None, user=None, poke_id=0, first=0, second=0, count=1, set_name=None):
        self.name = name
        self.user = user
        self.count = count
        self.pokedex_id = poke_id
        self.first_num = first
        self.second_num = second
        self.set_name = set_name

    def __repr__(self):
        return f"<Card {self.name!r} {self.first_num}/{self.second_num}>"
