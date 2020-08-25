#Lab #0
#Due Date: 08/28/2020, 11:59PM

'''
Written by: Dominic Assia

### Collaboration Statement:
    I worked on this assignment alone, using only this semester's course materials
'''

def sumSquares(aList):
    '''
        >>> sumSquares(5)
        >>> sumSquares('5') is None
        True
        >>> sumSquares(6.15)
        >>> sumSquares([1,5,-3,5,9,8,14,-25])
        277
        >>> sumSquares(['14',5,-3,5,9.0,8,14,7,'Hello'])
        326
    '''

    # Check if the function is called with a list as input
    if isinstance(aList, list):

        # Initialize sum to zero
        x = 0

        # Iterate through each index of the list
        for i in range(len(aList)):

            # Check index type, int or float
            if type(aList[i]) == float or type(aList[i]) == int:

                # Check if index is positive 
                if aList[i] >= 0:

                    # Check if index is divisible by 3 or 7
                    if aList[i] % 7 == 0 or aList[i] % 3 == 0:

                        # square the index and add to sum
                        x += ( aList[i] * aList[i] )

        # Return the sum as an int
        return int(x)

    # If input is not a list, return none
    else:
        return None

# # Uncomment next 3 lines if not running doctest in the command line
# if __name__ == "__main__":

#    import doctest
#    doctest.testmod()
