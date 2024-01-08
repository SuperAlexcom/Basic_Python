from Date import Date
from random import choice

class Person(Date):
    __job = "Unemployed"
    def __init__(self, _name = "Tom", _age = 1):
        self.__name = _name
        self.__age = _age
        Date.__init__(self)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newAge):
        if newAge in range(1, 101):
            self.__age = newAge
        else:
            print("Unacceptable value")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    # Set a job for person
    def FindAJob(self):
        jobs = ["Programmer", "Designer", "Builder"]
        self.__job = choice(jobs)

    def __str__(self):
        return "Name: {}\n" \
               "Age: {}\n" \
               "Profession: {}\n" \
               "Birthday: {}.{}.{}" \
            .format(self.__name, self.__age, self.__job, self.day, self.month, self.year)
