import unittest
from n.core import greet

class TestCore(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Tanish"), "Hello, Tanish")
        self.assertEqual(greet(), "Hello, World")

if __name__ == "__main__":
    unittest.main()
