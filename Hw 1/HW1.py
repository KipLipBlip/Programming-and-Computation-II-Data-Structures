# HW1
#Due Date: 09/11/2020, 11:59PM
"""                                   
### Collaboration Statement:
    I worked on this subfunction (separateChars) alone, using only this semester's course materials
"""

def rectangle(perimeter,area):
    """
        Returns the longest side of the rectangle with given perimeter and area 
        if both sides are integer lengths

        Doctest:
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
    areas = []

    # Starting at 1 going until half the area
    for i in range(1, int( area / 2 )):

        # If the area divided by the iterable is an integer
        if type(area // i) == int:

            # Ensure the quotient == the area
            if ( area // i ) * i == area:

                # Add possible area values
                areas.append([i,area // i])
        else:
            return -1

    # Find which area combo results in the correct perimeter
    for j in range(len(areas)):

        # Find the perimeter of the combo and comapre it to the given perimeter
        if (areas[j][0] * 2) + (areas[j][1] * 2) == perimeter:

            # This combo matches the perimeter, at index j, return longest side
            if areas[j][0] > areas[j][1]:
                return areas[j][0]

            else:
                return areas[j][1]
    else:
        return -1

def separateChars(aStr):
    '''
        Separate Special Characters
        ~~~~
        This function takes string and splits it over special non-alphanumeric characters, appending each split to a list index

        Doctest:
            >>> aStr = 'Hey m:y fr{end 54$ sp|it'
            >>> separateChars(aStr)
            ['Hey', 'm', ':', 'y', 'fr', '{', 'end', '54', '$', 'sp', '|', 'it']
            
        ### Collaboration Statement:
            I worked on this subfunction (separateChars) alone, using only this semester's course materials
    '''
    # Define all special characters
    newStr = ''

    # Iterate through all indices in given list
    for i in range(len(aStr)):

        if aStr[i].isalnum() == False:
            newStr += ' '
            newStr += aStr[i]
            newStr += ' '
        elif aStr[i].isalnum() == True:
            newStr += aStr[i]

    return newStr.split()

def translate(dict_words, txt):
    """
        Translates all words in the input string that have an entry in the given translation dictionary

        Doctest:
            >>> myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} 
            >>> text = '1 UP, 2 down / left right forward' 
            >>> translate(myDict, text)
            '2 down 2 up right left forward'
            >>> text
            '1 UP, 2 down / left right forward'
            >>> translate({'a':'b'}, text)
            '1 up 2 down left right forward'
    """
    # Find any special characters and put them at their own index
    txt = separateChars(txt)

    newStr = ''

    for i in range(len(txt)):

        # Check if the word (regardless of case) matches anything in the dictionary
        if txt[i] in dict_words:
            newStr += dict_words[txt[i]]

        elif txt[i].lower() in dict_words:
            newStr += dict_words[txt[i].lower()]

        elif txt[i].upper() in dict_words:
            newStr += dict_words[txt[i].upper()]

        # Do not add something that is non-alnum and not in the dict
        elif txt[i].isalnum() == False:
            pass

        # If nothing is found in the dictionary, add back original index but make sure its lowercase
        else:
            newStr += txt[i].lower()

        # Add a space unless at the last index 
        if i + 1 != len(txt):
            newStr += ' '

    # Fix double space issues
    newStr = newStr.replace('  ', ' ')

    return newStr

def successors(file):
    """
        Opens a text file and creates a dictionary whose keys are words from the text file 
        and whose values are lists of words that immediately follow the key word.

        Doctest:
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
    # Ensure the string ends in .txt & input type check
    if type(file) != str or str(file[-4] + file[-3] + file[-2] + file[-1]) != '.txt':
        return None
        
    try:
        # Open the file and read the contents
        with open(file) as f:       # with ensures the file is properly closed after its suite finishes, even if an error ocurred
            contents = f.read()     # use the read() function to read the entire file, contents has the data as string
            
            # Split string over spaces and special characters
            lst = separateChars(contents)

            # Initialize dictionary with first string in file
            dictionary = { '.' : [ lst[0] ] }
            
            for i in range(len(lst)):

                # If the key is not already in the dictionary, add it
                if lst[i] not in dictionary:

                    dictionary[lst[i]] = []

            for k in range(len(lst)):
                
                try:
                    dictionary[lst[k]].append(lst[k+1])

                except IndexError:
                    pass

            # Delete the last key, it will always be empty
            dictionary.pop(lst[-1], None)

            return dictionary

    # Check for file not found error
    except FileNotFoundError:
        return None

def sumDigits(num):
    """
        Returns the sum of the digits of a positive integer.

        Doctest:
            >>> sumDigits(1001)
            2
            >>> sumDigits(59872)
            31
    """
    # Ignore input if negative
    if num < 0:
        return None

    sum = 0

    # Convert num to str to index and get length of digits
    num = str(num)

    # Add every digit in number
    for i in range(len(num)):
        sum += int(num[i])

    return sum

def hailstone(num):
    """
        Returns the hailstone sequence starting at the given number until termination when 
        num is 1.

        - If a number is odd, mult. by 3 and add 1
        - If a number is even, divide by 2
        - The input number is always the first number in the sequence
        - The sequence stops when the number is 1

        Doctest:
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
    # Invalid input
    if num < 1 or type(num) != int:
        return None

    lst = [num]

    # Loop until we get 1
    while lst[-1] != 1:

        # Check even / odd
        if lst[-1] % 2 == 0:
            lst.append(int(lst[-1] / 2))

        else:
            lst.append(int((lst[-1] * 3) + 1))

    return lst

def common(aList1, aList2):
    """
        Returns a list containing only the elements that are common between the two lists
        in ascending order, without duplicates.

        Doctest:
            >>> common([12,3,5,8,90,11,44,66,8,9,34,56,-1,0,5,3333,3,2,1],[12,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,44])
            [1, 3, 12, 44]
            >>> common([1,2,3],[4,5,6])
            []
            >>> common(1, [3.5]) is None
            True
    """

    if type(aList1) != list or type(aList2) != list:
        return None  

    common = []

    # Iterate through both lists
    for i in range(len(aList1)):

        for j in range(len(aList2)):

            # If they have an index with the same value that is not already in the common list, append it
            if aList1[i] == aList2[j] and aList1[i] not in common:

                common.append( aList2[j] )

    # Sort in ascending value
    
    # Put all types in their own list
    numLst = []
    strLst = []
    boolLst = []
    listLst = []

    # Iterate through common 
    for k in range(len(common)):
        
        if type(common[k]) == int or type(common[k]) == float:
            numLst.append(common[k])
        if type(common[k]) == str:
            strLst.append(common[k])
        if type(common[k]) == bool:
            boolLst.append(common[k])
        if type(common[k]) == list:
            listLst.append(common[k])

    # Sort numbers
    numLst = sorted(numLst)

    # Add lists together
    return numLst + strLst + boolLst + listLst

if __name__ == "__main__":

    print(common([12,3,5,8,90,11,44,[1],66,8,9,34,56,False,-1,0,5,3333,3,2,1,'hey', 'e', 129],[12,'e',False,3,3,3,'hey',3,3,[1],3,3,3,3,3,3,3,3,1,1,44]))
    import doctest
    doctest.testmod()