#!/usr/bin/env python
import unittest
import exercises.numbers

class TestNumbersExercise(unittest.TestCase):
    def test_calculate_product(self):
        self.assertEqual(3 * 2, exercises.numbers.calculate_product(3, 2))
        self.assertEqual(4 * 2, exercises.numbers.calculate_product(4, 2))

if __name__ == '__main__':
    unittest.main()
    



