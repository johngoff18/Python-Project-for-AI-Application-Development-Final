# Write at least 2 tests in tests.py for each method
# Test for null input for frenchToEnglish
# Test for null input for englishToFrench.
# Test for null input for both methods.
# Test for the translation of the world 'Hello' and 'Bonjour'.
# Test for the translation of the world 'Bonjour' and 'Hello'.

#import unittest
import unittest
import sys
sys.path.append('../../')
from server import englishToFrench, frenchToEnglish

# define test class
class TestServer(unittest.TestCase):
    # define test methods
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench("Bonjour"), "Hello")
        self.assertEqual(englishToFrench(""), "")
        self.assertEqual(englishToFrench(None), "")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Hello"), "Bonjour")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish(""), "")
        self.assertEqual(frenchToEnglish(None), "")

# define test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestServer))
    return suite

# run test suite
if __name__ == "__main__":
    # run tests
    runner = unittest.TextTestRunner()
    runner.run(suite())