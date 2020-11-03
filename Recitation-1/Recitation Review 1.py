# Rectiation 9.15
def totalStudents(d):
    '''
    >>> totalStudents({'A':20,'B':16,'C':7,'D':5,'F':9})
    48
    '''
    return d['A'] + d['B'] + d['C'] + d['D']

import unittest
from LAB0 import sumSquares

class TestSumSquares(unittest.TestCase):
    ''' Tests for recitation sumSquares '''

    def test_for_input(self):
        ''' test for input errors '''
        self.assertEqual(sumSquares(5), None)