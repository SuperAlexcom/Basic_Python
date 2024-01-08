from Date import Date
from Person import Person
from Alien import Alien

realPrint = print
def print(arg):
    realPrint(arg, end='\n----------\n')

# Creating with const values
d = Date(day=1, year=2010)
print(d)

d1 = Date(day=1, month=1, year=2000)
realPrint(d1)
realPrint()
realPrint('After using method Subtract2Days:')
d1.Subtract2Days()
print(d1)

d3 = Date(day=29,month=2,year=2001)
print(d3)

d4= Date(29,2,2000)
realPrint(d4)
d4.IncreaseYear()
realPrint()
realPrint("After using method IncreaseYear:")
realPrint(d4)
realPrint()
realPrint('After using method Subtract2Days:')
d4.Subtract2Days()
print(d4)

# Creating with entered values
#values = input('Input date in format: dd.mm.yyyy: ').split('.')
values = [1, 1, 2020]
d2 = Date(*values[0:3])
print(d2)

p1 = Person()
print(p1)

p2 = Person(_name='Kirill', _age=19)
realPrint(p2)
realPrint()
realPrint('After using method FindJob:')
p2.FindAJob()
print(p2)

a1 = Alien()
realPrint(a1)
realPrint()
realPrint('After using method FindPlanet:')
print(a1)

s = '''
====================================
= Work with accessors and mytators =
====================================
'''
realPrint(s)
realPrint('Before changing: ', p2.day)
p2.day = -2
p2.day = 100
realPrint('After bad changing: ', p2.day)
p2.day = 15
realPrint('After changing: ', p2.day)

s = '''
======================
= End of the program =
======================
'''
realPrint(s)