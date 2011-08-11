import unittest
import glob

def create_test_suite(exercise=None):
    if exercise is None:
        test_file_strings = glob.glob('tests/test_*.py')
        module_strings = [str[0:len(str)-3].replace('/', '.') for str in test_file_strings]
    else:
        module_strings = ['tests.test_%s' % (exercise)]
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str in module_strings]
    testSuite = unittest.TestSuite(suites)
    return testSuite

if __name__ == '__main__':
    create_test_suite();
