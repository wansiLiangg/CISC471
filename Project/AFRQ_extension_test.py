"""
AFRQ Extension Unit Tests

3 unit tests for each function
4 functions in total
"""

import unittest
import AFRQ_extension as extension

class TestCheckInput(unittest.TestCase):
    """
    Set up the expected outputs and run the function with positive and negative
    unit tests for checkInput function
    """
    def setUp(self):
        """
        Set up the expected outputs and call the checkInput function with 3
        unit tests

        First two (expected1, result1, expected2, result2) are setting up for
        negative unit tests
        The last one (expected3, result3) is setting up for the positive unit
        test
        """
        self.expected1 = [False, False]
        self.result1 = extension.checkInput(0, 5)

        self.expected2 = [False, False]
        self.result2 = extension.checkInput("string", -1)

        self.expected3 = [True, True]
        self.result3 = extension.checkInput(2, 0.04)

    def testCheckInputNegative1(self):
        """
        Testing if the first negative test case sucessfully passed
        """
        self.assertListEqual(self.result1, self.expected1)

    def testCheckInputNegative2(self):
        """
        Testing if the second negative test case sucessfully passed
        """
        self.assertListEqual(self.result2, self.expected2)

    def testCheckInputPositive(self):
        """
        Testing if the positive test case sucessfully passed
        """
        self.assertListEqual(self.result3, self.expected3)

class TestGetCoefficient(unittest.TestCase):
    """
    Set up the expected outputs and run the function with positive unit tests
    for getCoefficient function
    """
    def setUp(self):
        """
        Set up the expected outputs and call the getCoefficientt function with
        3 positve unit tests
        """
        self.expected1 = [1, 1]
        self.result1 = extension.getCoefficient(1)

        self.expected2 = [1, 4, 6, 4, 1]
        self.result2 = extension.getCoefficient(4)

        self.expected3 = [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
        self.result3 = extension.getCoefficient(10)

    def testGetCoefficientPositive1(self):
        """
        Testing if the first positve test case sucessfully passed
        """
        self.assertListEqual(self.result1, self.expected1)

    def testGetCoefficientPositive2(self):
        """
        Testing if the second positve test case sucessfully passed
        """
        self.assertListEqual(self.result2, self.expected2)

    def testGetCoefficientPositive3(self):
        """
        Testing if the third positive test case sucessfully passed
        """
        self.assertListEqual(self.result3, self.expected3)

class TestAfrqExtension(unittest.TestCase):
    """
    Set up the expected outputs and run the function with positive unit tests
    for afrqExtension function
    """
    def setUp(self):
        """
        Set up the expected outputs and call the afrqExtension function with
        3 positve unit tests
        """
        self.expected1 = 0.36
        self.result1 = extension.afrqExtension(2, 0.04)

        self.expected2 = 0.561
        self.result2 = extension.afrqExtension(4, 0.0012)

        self.expected3 = 0.51
        self.result3 = extension.afrqExtension(2, 0.09)

    def testAfrqExtensionPositive1(self):
        """
        Testing if the first positve test case sucessfully passed
        """
        self.assertEqual(self.result1, self.expected1)

    def testAfrqExtensionPositive2(self):
        """
        Testing if the second positve test case sucessfully passed
        """
        self.assertEqual(self.result2, self.expected2)

    def testAfrqExtensionPositive3(self):
        """
        Testing if the third positive test case sucessfully passed
        """
        self.assertEqual(self.result3, self.expected3)

class TestAfrqExtensionMain(unittest.TestCase):
    """
    Set up the expected outputs and run the function with positive and negative
    unit tests for afrqExtensionMain function
    """
    def setUp(self):
        """
        Set up the expected outputs and call the afrqExtensionMain function with
        the positve unit test
        """

        self.expected1 = [0.36, 0.51, 0.561]
        self.result1 = extension.afrqExtensionMain([2, 2, 4],[0.04, 0.09, 0.0012])

    def testAfrqExtensionMainNegative1(self):
        """
        Testing if the first negative test case sucessfully passed
        """
        with self.assertRaises(ValueError):
            extension.afrqExtensionMain([2, -1], [0.02, 4])

    def testAfrqExtensionMainNegative2(self):
        """
        Testing if the second negative test case sucessfully passed
        """
        with self.assertRaises(IndexError):
            extension.afrqExtensionMain([2], [0.04, 0.05])

    def testAfrqExtensionMainNegative3(self):
        """
        Testing if the third negative test case sucessfully passed
        """
        with self.assertRaises(IndexError):
            extension.afrqExtensionMain([], [])

    def testAfrqExtensionMainPositive(self):
        """
        Testing if the positive test case sucessfully passed
        """
        self.assertListEqual(self.result1, self.expected1)

if __name__ == '__main__':
    """
    Starting the unit tests
    """
    unittest.main()
