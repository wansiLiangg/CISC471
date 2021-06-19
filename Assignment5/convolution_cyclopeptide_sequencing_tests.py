'''
CISC 471 HW5
Part1.2 Convolution Cyclopeptide Sequencing Unit Tests 
'''

import unittest
import convolution_cyclopeptide_sequencing as ccs

class TestListElements(unittest.TestCase):
    def setUp(self):
        #Positive unit tests
        self.expected1 = [99, 71, 137, 57, 72, 57]
        self.result1 = ccs.convolutionCyclopeptideSequencing([57, 57, 71, 99, 129, 137, 170, 186, 194, 208, 228, 265, 285, 299, 307, 323, 356, 364, 394, 422, 493], 20, 60)

        self.expected2 = [71, 147, 113, 129]
        self.result2 = ccs.convolutionCyclopeptideSequencing([0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460], 5, 10)

        #Negative unit test
        self.expected3 = "No sequence is found"
        self.result3 = ccs.convolutionCyclopeptideSequencing([38, 51, 400, 375, 624], 5, 10)

    #Positive unit tests
    def testPositive1(self):
        self.assertCountEqual(self.result1, self.expected1)

    def testPositive2(self):
        self.assertCountEqual(self.result2, self.expected2)

    #Negative unit test
    def testNegative(self):
        self.assertCountEqual(self.result3, self.expected3)

if __name__ == '__main__':
    unittest.main()
