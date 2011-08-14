#!/usr/bin/env python
import unittest
import exercises.numbers

class TestNumbersExercise(unittest.TestCase):
    def test_calculate_product(self):
        self.assertEqual(3 * 2, exercises.numbers.calculate_product(3, 2))
        self.assertEqual(4 * 2, exercises.numbers.calculate_product(4, 2))

    def test_denominate(self):
        self.assertEqual('3 quarters 4 pennies', exercises.numbers.denominate(0.79))
        self.assertEqual('1 penny', exercises.numbers.denominate(0.01))
        self.assertEqual('1 nickel', exercises.numbers.denominate(0.05))
        self.assertEqual('1 dime 1 nickel 4 pennies', exercises.numbers.denominate(0.19))

    def test_calculate(self):
        expected = {
            '3 + 4': 7,
            '15 - 5': 10,
            '25 * 4': 100,
            '23 / 10': 2,
            '24 % 5': 4,
            '2 ** 5': 32,
            '2.3 + 4': 6.3,
            '10.0 * 4': 40.0
            }
        for i in expected:
            self.assertEqual(expected[i], exercises.numbers.calculator(i))       

if __name__ == '__main__':
    unittest.main()
    



