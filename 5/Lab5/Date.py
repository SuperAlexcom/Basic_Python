from WrongDateException import WrongDateException

bigMonths = [1, 3, 5, 7, 8, 10, 12]

class Date:
    def __init__(self, day = None, month = None, year = None):
        OK = True
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except (ValueError, TypeError):
            OK = False

        if OK and Date.IsDateCorrect(day, month, year):
            self.__day = day
            self.__month = month
            self.__year = year
            print('Object created with certain value')
        else:
            self.__day = 1
            self.__month = 1
            self.__year = 2020
            print("Value error: default value was set")

    def __del__(self):
        pass

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, newDay):
        maxDay = 0
        if self.__month in bigMonths:
            maxDay = 31
        elif self.month != 2:
            maxDay = 30
        elif Date.IsYearBisextile(self.year):
            maxDay = 29
        else:
            maxDay = 28

        if newDay in range(1, maxDay+1):
            self.__day = newDay
        else:
            print("Unacceptable value")


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, newMonth):
        if newMonth in range(1, 13):
            self.__month = newMonth
        else:
            print("Unacceptable value")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, newYear):
        if newYear in range(1970, 2020):
            self.__year = newYear
        else:
            print("Unacceptable value")

    def __str__(self):
        return "{}.{}.{}".format(self.__day,self.__month,self.__year)

    @staticmethod
    def IsYearBisextile(y):
        if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
            return True
        else:
            return False

    def IncreaseYear(self):
        self.__year += 1
        if not Date.IsYearBisextile(self.__year) and self.__month == 2 and self.__day == 29:
            self.__day = 28

    def Subtract2Days(self):
        self.__day -= 2

        if self.__day == 0 or self.__day == -1:
            if self.__month == 1:
                self.__month = 12
                self.__year -= 1
            else:
                self.__month -= 1

            if self.__month in bigMonths:
                self.__day += 31
            elif self.__month != 2:
                self.__day += 30
            elif Date.IsYearBisextile(self.year):
                self.__day += 29
            else:
                self.__day += 28

    @staticmethod
    def IsDateCorrect(day, month, year):
        return 0 < day < 32 and\
            0 < month < 13 and\
            year > 0 and\
            (month in bigMonths and day < 32 or\
             month not in bigMonths and month != 2 and day < 31 or\
                    month == 2 and Date.IsYearBisextile(year) and day < 30 or\
                    month == 2 and not Date.IsYearBisextile(year) and day < 29)