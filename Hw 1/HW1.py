# HW1
#Due Date: 09/11/2020, 11:59PM
"""                                   
### Collaboration Statement:
             
"""
def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10) # From a 2x5 rectangle
        5
        >>> rectangle(12, 5) # From a 1x5 rectangle
        5
        >>> rectangle(25, 25) # A 2.5x10, but one side is not an integer
        -1
        >>> rectangle(50, 100) # From a 5x20 rectangle
        20
        >>> rectangle(11, 5)
        -1
        >>> rectangle(11, 4)
        -1
    """
    #- YOUR CODE STARTS HERE
    pass



def translate(dict_words, txt):
    """
        >>> myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} 
        >>> text = '1 UP, 2 down / left right forward' 
        >>> translate(myDict, text)
        '2 down 2 up right left forward'
        >>> text
        '1 UP, 2 down / left right forward'
        >>> translate({'a':'b'}, text)
        '1 up 2 down left right forward'
    """

    #- YOUR CODE STARTS HERE
    pass



def successors(file):
    """
        >>> expected = {'.': ['He', 'But', '(', ')'], 'He': ['will'], 'will': ['be', 'see'], 'be': ['the'], 'the': ['president', 'company', 'importance'], 'president': ['of', '.'], 'of': ['the', 'it', 'these'], 'company': [';'], ';': ['right'], 'right': ['now'], 'now': ['he'], 'he': ['is', ',', 'will'], 'is': ['a', 'no'], 'a': ['vice'], 'vice': ['president'], 'But': ['he'], ',': ['himself', 'is'], 'himself': [','], 'no': ['sure'], 'sure': ['of'], 'it': ['.'], '(': ['Later'], 'Later': ['he'], 'see': ['the'], 'importance': ['of'], 'these': ['3'], '3': ['.']}
        >>> returnedDict = successors('article.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['the']
        ['president', 'company', 'importance']
        >>> returnedDict['will']
        ['be', 'see']
        >>> returnedDict['3']
        ['.']
        >>> returnedDict['.']
        ['He', 'But', '(', ')']
        >>> successors('article.tt') is None
        True
        >>> successors(2.3) is None
        True
    """
    # --- YOU INPUT VALIDATION STARTS HERE




    # Open the file and read the contents
    with open(file) as f:   #with ensures the file is properly closed after its suite finishes, even if an error ocurred
        contents = f.read() # use the read() function to read the entire file, contents has the data as string


    # --- YOU CODE STARTS HERE
    pass



def sumDigits(num):
    """
        >>> sumDigits(1001)
        2
        >>> sumDigits(59872)
        31

    """
    #- YOUR CODE STARTS HERE
    pass



def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(3.5)
        >>> hailstone(0)
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    
    #- YOUR CODE STARTS HERE
    pass


def common(aList1, aList2):
    """
        >>> common([12,3,5,8,90,11,44,66,8,9,34,56,-1,0,5,3333,3,2,1],[12,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,44])
        [1, 3, 12, 44]
        >>> common([1,2,3],[4,5,6])
        []
        >>> common(1, [3.5]) is None
        True
    """
    #- YOU CODE STARTS HERE
