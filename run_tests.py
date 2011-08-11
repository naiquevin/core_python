import unittest
import tests.all_tests
from sys import argv

if __name__ == '__main__':
    try:
        test_ex = argv[1]
    except IndexError as e:
        test_ex = None
    testSuite = tests.all_tests.create_test_suite(test_ex);
    text_runner = unittest.TextTestRunner().run(testSuite)
