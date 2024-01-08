from Date import Date
from random import choice

class Alien(Date):
    def __init__(self):
        Date.__init__(self)
        self.__name = "Some creature"

    def DefinePlanet(self):
        planets = "Mars, Earth, Mercury"
        self.__planet = choice(planets)
