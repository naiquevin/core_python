#!/usr/bin/env python

import unittest
import exercises.sequences

class TestSequencesExercise(unittest.TestCase):

    def test_sort_numlist_desc(self):
        self.assertEqual([34, 10, 5, 3, 1, 0], exercises.sequences.sort_numlist_desc([10, 3, 5, 0, 1, 34]))

    def test_sort_string_desc(self):
        self.assertEqual('xvsfdca', exercises.sequences.sort_string_desc('advfcxs'))

    def test_idcheck(self):
        self.assertTrue(exercises.sequences.idcheck('abc'))
        self.assertTrue(exercises.sequences.idcheck('a'))
        self.assertFalse(exercises.sequences.idcheck('3cf'))
        self.assertFalse(exercises.sequences.idcheck('while'))
        self.assertTrue(exercises.sequences.idcheck('True')) # True is not a keyword. WTF!!

    def test_string_cmp(self):
        self.assertTrue(exercises.sequences.string_cmp('hello4', 'hello4'))
        self.assertTrue(exercises.sequences.string_cmp('55WorlD', '55woRLd'))

    def test_is_palindrome(self):
        self.assertTrue(exercises.sequences.is_palindrome('abcdefghhgfedcba'))
        self.assertTrue(exercises.sequences.is_palindrome('pqrqp'))
        self.assertFalse(exercises.sequences.is_palindrome('wxyz'))        

    def test_make_palindrome(self):
        self.assertEquals('helloolleh', exercises.sequences.make_palindrome('hello'))

    def test_mimic_strip(self):
        self.assertEquals('stripme!', exercises.sequences.mimic_strip('  stripme! '))
        self.assertEquals('Hello World!', exercises.sequences.mimic_strip(' Hello World!   '))
        self.assertEquals('', exercises.sequences.mimic_strip('    '))

    def test_textify_numbers(self):
        self.assertEquals('eight-nine', exercises.sequences.textify_numbers(89))
        self.assertEquals('two-seven-zero', exercises.sequences.textify_numbers(270))

    def test_minutes_to_hours(self):
        self.assertEquals('2 hours and 30 minutes', exercises.sequences.minutes_to_hours(150))
        self.assertEquals('0 hours and 23 minutes', exercises.sequences.minutes_to_hours(23))
        self.assertEquals('1 hour and 0 minutes', exercises.sequences.minutes_to_hours(60))

    def test_rochambeau(self):
        cases = [
            ("rock", "paper", "computer wins!!"),
            ("paper", "rock", "you win!!"),
            ("rock", "scissors", "you win!!"),
            ("scissors", "rock", "computer wins!!"),
            ("paper", "scissors", "computer wins!!"),
            ("scissors", "paper", "you win!!"),
            ("rock", "rock", "its a draw!!"),
            ("paper", "paper", "its a draw!!"),
            ("scissors", "scissors", "its a draw!!")
            ]
        for user, computer, exp_result in cases:
            r = exercises.sequences.Rochambeau()
            result = r.find_winner(user, computer)
            self.assertEquals(exp_result, result)

    def test_dateconvertor(self):
        # days upto year end
        days = exercises.sequences.DateConvertor.days_upto_year_end(20, 1, 1992)
        self.assertEquals(346, days)
        days = exercises.sequences.DateConvertor.days_upto_year_end(20, 1, 1993)
        self.assertEquals(345, days)
        days = exercises.sequences.DateConvertor.days_upto_year_end(20, 12, 1992)
        self.assertEquals(11, days)
        days = exercises.sequences.DateConvertor.days_from_year_start(20, 3, 2000)
        self.assertEquals(80, days)
        days = exercises.sequences.DateConvertor.days_from_year_start(20, 3, 2003)
        self.assertEquals(79, days)
        d = exercises.sequences.DateConvertor("12/12/2000", "20/2/2003")
        from datetime import datetime
        actual = (datetime.strptime('2003-2-20', "%Y-%m-%d")- datetime.strptime('2000-12-12',"%Y-%m-%d")).days
        self.assertEquals(actual,d.days_between())        
