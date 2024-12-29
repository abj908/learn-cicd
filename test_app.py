import unittest
from app import add_numbers, subtract_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_subtract_numbers(self):  # New test
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(0, 3), -3)

if __name__ == "__main__":
    unittest.main()
