import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchByTitleTest(unittest.TestCase):
    def test_case_insensitive_match(self):
        items = [DigitalVideoDisc("The Lion King", "Animation", 19.95)]
        self.assertEqual(len(search_by_title(items, "lion")), 1)

    def test_no_match(self):
        items = [DigitalVideoDisc("The Lion King", "Animation", 19.95)]
        self.assertEqual(search_by_title(items, "dragon"), [])


if __name__ == "__main__":
    unittest.main()
