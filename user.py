from login import *
from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def usertype(self):
        pass

    def verification(self):
        pass


class Player(User):
    def usertype(self):
        print("This user is a player")


class Admin(User):
    def usertype(self):
        print("This user is an Administrator")
