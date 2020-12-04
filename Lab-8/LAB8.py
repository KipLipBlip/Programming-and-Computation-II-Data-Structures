#Lab #8
#Due Date: 12/05/2020, 11:59PM 
'''                                 
# Collaboration Statement:   
        I completed this assignment alone, using only this semester's material
'''

def sumMatrices(matrix1, matrix2):
    '''
        >>> sumMatrices([[2, 1], [-3, 6]], [[1, 3], [4, -1]])
        [[3, 4], [1, 5]]
        >>> sumMatrices([[3, 1], [2, 7]], [[4, 2], [5, 7]])
        [[7, 3], [7, 14]]

    '''
    # Nest a loop to sum numbers of the inner list, as specified there will only be a two by two matrix
    return [ [ matrix1[i][j] + matrix2[i][j] for j in range(2) ] for i in range(2) ]


def digitSum(num):
    '''
        >>> digitSum(15)(555)
        True
        >>> digitSum(22)(2578)
        True
        >>> digitSum(258)(1011010101010)
        False
    '''
    return lambda n: True if num == sum( [ int(str(n)[i]) for i in range(len(str(n)))] ) else False


def repeat(itr, n):
    '''
    >>> numList1 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeat(numList1, 2)
    9
    >>> numList2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeat(numList2, 3)
    8
    >>> repeat(numList1, 2)
    8
    >>> numList3 = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeat(numList3, 3)
    2
    >>> repeat(numList3, 3)
    5
    '''
    # Initialize
    t = 1
    i = next(itr)
    j = next(itr)

    # Loop while its not the first index / StopIteration
    while n > 1:

        # Check if they're equal
        if i == j:
            t += 1
        else:
            t = 1

        # Check num of iterations
        if t == n:
            return i

        # Iterate
        i = j
        j = next(itr)

    return next(itr)


def genAccum(seq, fn):
    '''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    '''
    t = 1
    i = iter(seq)

    # Initally iterate & yield
    u = next(i)
    yield u

    # Continue until no more length, reassign var and yield
    while t <= len(seq):

        u = fn(u, next(i))
        yield u