import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class SearchByCategoryTest(unittest.TestCase):
    def test_find_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", 19.95),
            DigitalVideoDisc("Die Hard", "Action", 15.0),
        ]
        result = search_by_category(items, "Animation")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])


if __name__ == "__main__":
    unittest.main()
