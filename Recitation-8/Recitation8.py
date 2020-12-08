# Complete for Recitation 9: 12/8/2020

def missing(n):
    '''
    A sequence S contains n−1 unique integers in the range [1,n], 
    that is, there is one number from this range that is not in S. 
    Design an O(n) time algorithm for finding that number. LINEAR

    >>> missing([1, 2, 4, 6, 3, 7, 8, 5])
    9
    >>> missing([6,3,5,4,2])
    1
    '''

    for i in range(1,len(n)+2):

        if i not in n:

            return i
