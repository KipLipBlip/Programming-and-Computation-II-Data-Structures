import unittest 
import Module_2_Practice 

class CountOddTestCases(unittest.TestCase):
    '''
        Tests for Module 2 Practive
        https://docs.python.org/3/library/unittest.html 
    '''

    def error_msg_check(self):
        ''' Determine if the function returns 'Error' correctly '''

        print('Testing Input Error')

        self.assertEqual( countOdd( 'test' ),           'Error', '\tFailed: Str input\n' )
        self.assertEqual( countOdd( True ),             'Error', '\tFailed: Bool input\n' )
        self.assertEqual( countOdd( {'test':'test'} ),  'Error', '\tFailed: Dict input\n' )
        self.assertEqual( countOdd( 5.34 ),             'Error', '\tFailed: Float input\n' )
        self.assertEqual( countOdd( 5 ),                'Error', '\tFailed: Int input\n' )


    # def test_for_integer_input(self):
    #     '''Are even digists correctly computed in a positive number?'''
    #     self.assertEqual(countEven(15),0, "Failed test for 15")
    #     self.assertEqual(countEven(246589913),4, "Failed test for 246589913")
    #     self.assertEqual(   countOdd([1,3,5,7]),    4,  'Failed Tes' )


    # def test_for_negative_input(self):
    #     '''Is function returning None for negative numbers?'''    #Condition not included in the m2.py
    #     self.assertEqual(countEven(-15),None, "Failed test for -15")
    #     self.assertEqual(countEven(-246589913),None, "Failed test for -246589913")
    #     self.assertEqual(countEven(-55599910),None, "Failed test for -55599910")

    # def test_for_invalid_input(self):
    #     '''Is function returning None for invalid input?''' #Condition not included in the m2.py
    #     self.assertEqual(countEven([1,5]),None, "Failed test for [1,5]")
    #     self.assertEqual(countEven("246589913"),None, "Failed test for '246589913'")      



if __name__ == '__main__':
	unittest.main(exit=False)