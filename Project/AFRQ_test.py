"""
AFRQ: Counting Disease Carriers Unit Tests

Containing 4 unit tests in total, 1 positive unit tests and 3 negative unit test
"""

import unittest
import AFRQ


class TestAfrq(unittest.TestCase):
    """
    Set up the expected outputs and run the function with positive and negative
    unit tests of the AFRQ algorithm
    """
    def setUp(self):
        """
        Set up the expected outputs and call the AFRQ function for the postive
        unit test
        """
        self.expected1 = [0.532, 0.75, 0.914]
        self.result1 = AFRQ.afrq([0.1, 0.25, 0.5])

    def testAfrqPositive1(self):
        """
        Testing if the positive test case sucessfully passed
        """
        self.assertListEqual(self.result1, self.expected1)

    def testAfrqNegative1(self):
        """
        Testing if the first negative test case sucessfully passed
        """
        with self.assertRaises(ValueError):
            AFRQ.afrq([-1, 2])

    def testAfrqNegative2(self):
        """
        Testing if the second negative test case sucessfully passed
        """
        with self.assertRaises(TypeError):
            AFRQ.afrq(["str", "string"])

    def testAfrqNegative3(self):
        """
        Testing if the third negative test case sucessfully passed
        """
        with self.assertRaises(IndexError):
            AFRQ.afrq([])

if __name__ == '__main__':
    """
    Starting the unit tests
    """
    unittest.main()
