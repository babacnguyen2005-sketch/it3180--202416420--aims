import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("B", "Test", 20.0))
        self.cart.add_dvd(DigitalVideoDisc("A", "Test", 10.0))
        self.cart.add_dvd(DigitalVideoDisc("C", "Test", 30.0))

    def test_sort_by_title(self):
        titles = [dvd.title for dvd in self.cart.sort_by_title()]
        self.assertEqual(titles, ["A", "B", "C"])

    def test_sort_by_cost(self):
        costs = [dvd.cost for dvd in self.cart.sort_by_cost()]
        self.assertEqual(costs, [10.0, 20.0, 30.0])


if __name__ == "__main__":
    unittest.main()
