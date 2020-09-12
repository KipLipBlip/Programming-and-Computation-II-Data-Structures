import unittest 
import 

class CountEvenTestCases(unittest.TestCase):
    """Tests for m2.py"""

    def test_for_integer_input(self):
        """Are even digists correctly computed in a positive number?"""
        self.assertEqual(countEven(15),0, "Failed test for 15")
        self.assertEqual(countEven(246589913),4, "Failed test for 246589913")
        self.assertEqual(countEven(55599910),1, "Failed test for 55599910")


    def test_for_negative_input(self):
        """Is function returning None for negative numbers?"""    #Condition not included in the m2.py
        self.assertEqual(countEven(-15),None, "Failed test for -15")
        self.assertEqual(countEven(-246589913),None, "Failed test for -246589913")
        self.assertEqual(countEven(-55599910),None, "Failed test for -55599910")

    def test_for_invalid_input(self):
        """Is function returning None for invalid input?""" #Condition not included in the m2.py
        self.assertEqual(countEven([1,5]),None, "Failed test for [1,5]")
        self.assertEqual(countEven("246589913"),None, "Failed test for '246589913'")      



if __name__ == '__main__':
	unittest.main(exit=False)