from Date import Date
from ForService import input_int
from WrongDateException import WrongDateException
from Tests import *
import unittest


birthdays = []
filename = "birthdays"

try:
    with open(filename, 'br') as fin:
        content = fin.readlines()
        for line in content:
            line.replace(b'\n', b'')
            b = [int(i) for i in line.split()]
            birthdays.append(Date(b[0], b[1], b[2]))
except IOError:
    print("Database doesn't exist")
    print("Enter number of birthdays you want to add: ", end='')
    num = 0
    while num <= 0:
        num = input_int()
        if (num <= 0):
            print("Len of array can't be negative")
    assert num > 0, "Len of array can't be negative"

    cur = 0
    while cur < num:
        try:
            print('Input day: ', end='')
            day = input_int()

            print('Input month: ', end='')
            month = input_int()

            print('Input year: ', end='')
            year = input_int()

            if Date.IsDateCorrect(day, month, year):
                birthdays.append(Date(day, month, year))
                cur += 1
            else:
                raise WrongDateException("There is not data with given params!")
        except WrongDateException as e:
            print(e.txt)

assert len(birthdays) > 0, "Database can't be empty"

with open(filename, 'bw') as fout:
    for line in birthdays:
        fout.write(bytearray("{} {} {}\n".format(line.day, line.month, line.year), 'utf8'))
