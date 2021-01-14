import unittest

from src.fizzbuzz import fizz_buzz

class TestFizzbuzz(unittest.TestCase):

    def test_number_is_divisible_by_3(self):
        self.assertEqual("Fizz", fizz_buzz(3))

    def test_number_is_divisible_by_5(self):
        self.assertEqual("Buzz", fizz_buzz(5))

    def test_number_is_divisible_by_3_number_is_divisible_5(self):
        self.assertEqual("FizzBuzz", fizz_buzz(15))

    def test_fizzbuzz_returns_input(self):
        self.assertEqual("7", fizz_buzz(7))

