import unittest
from Date import Date

class DateTestCase(unittest.TestCase):
    def setUp(self):
        self.date = Date(1,1,2020)

    def test_is_year_bisextile_method(self):
        self.assertEqual(self.date.IsYearBisextile(1600), True)
        self.assertEqual(self.date.IsYearBisextile(1700), False)

    def test_increase_year_method(self):
        self.date.year = 2000
        self.date.IncreaseYear()
        self.assertEqual(self.date.year, 2001)

if __name__ == "__main__":
    unittest.main()