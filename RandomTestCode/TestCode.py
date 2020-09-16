# Random Code to check concepts

def onlyTwo(n):
    """
        >>> onlyTwo(8009)
        0
        >>> onlyTwo(123)
        1
        >>> onlyTwo(232)
        2
        >>> onlyTwo(2)
        1
    """
    # Set number of 2's to 0 and convert the int to a str for index check
    x = 0 
    n = str(n)

    # For the length of the str
    for i in range(len(n)):

        # Check if each index of the str is == 2
        if n[i] == '2':

            x += 1
    
    # Return the sum of all the 2's
    return x

def reverse(aList):
    """
        Write the code for the function reverse(aList) that takes a list as an argument and reverses the list. You should mutate the original list, 
        without creating any new lists. In other words, the original memory allocation for aList should reflect the changes. Do NOT return anything.
        
        >>> reverse([1, 2, 3, 4])
        [4, 3, 2, 1]
    """
    x = len(aList)

    for i in range(1, x+1):
        aList.append(aList[x-i])

    for j in range(x):
        aList.pop(0)

    return aList

def minmax(data):
    '''
    Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, 
    in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.

    >>> minmax([100,23,3,45])
    (3, 100)

    '''

    # Find the smallest number
    smallest = 1000

    for i in range(len(data)):

        if data[i] < smallest:

            smallest = data[i]

    # Find the largest number
    largest = 0

    for i in range(len(data)):

        if data[i] > largest:

            largest = data[i]
    
    return (smallest, largest)

def codesEncrypt(string):
    '''
        Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:

        codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc . . .}

        Using this example, the letter A would be assigned the symbol %, the letter a would be assigned the number 9,
        the letter B would be assigned the symbol @, and so forth. The program takes a non-empty string as a parameter 
        and it uses the dictionary to return an encrypted version of the string's contents. Each character in the 
        output should contain the code for the corresponding character in the input string. 
        
        Then, write a second program that takes the encrypted message and returns the its decrypted contents.
    '''

    codes = {   'A' : '%', 
                'a' : '9',
                'B' : '@',
                'b' : '#',
                'C' : 'g',
                'c' : 'f',
                'D' : 'W',
                'd' : 'w',
                'E' : 'R',
                'e' : '3',
                'F' : '5',
                'f' : '1',
                'G' : '6',
                'g' : '2',
                'H' : '$',
                'h' : '^',
                'I' : '!',
                'i' : '7',
                'J' : '&',
                'j' : '}',
                'K' : 't',
                'k' : 'i',
                'L' : 'I',
                'l' : 'u',
                'M' : 'q',
                'm' : 'e',
                'N' : 'Q',
                'n' : '*',
                'O' : 'r',
                'o' : 'B',
                'P' : '=',
                'p' : 'b',
                'Q' : 'j',
                'q' : '.',
                'R' : '>',
                'r' : 'J',
                'S' : 'z',
                's' : '<',
                'T' : 'Y',
                't' : 'd',
                'U' : 'A',
                'u' : 'Z',
                'V' : 'y',
                'v' : 'a',
                'W' : '[',
                'w' : 'D',
                'X' : 'V',
                'x' : 'x',
                'Y' : 'n',
                'y' : 'v',
                'Z' : '~',
                'z' : '`',
                ' ' : '-'
            }

    if string == '':
        return None

    encryptedString = ''

    # For every character in the string
    for i in range(len(string)):

        # Find the value of the character in the dictionary and append it to a new string
        encryptedString += codes[string[i]]

    return encryptedString

def codesDecrypt(encryptedString):

    codes = {   '%' : 'A', 
                '9' : 'a',
                '@' : 'B',
                '#' : 'b',
                'g' : 'C',
                'f' : 'c',
                'W' : 'D',
                'w' : 'd',
                'R' : 'E',
                '3' : 'e',
                '5' : 'F',
                '1' : 'f',
                '6' : 'G',
                '2' : 'g',
                '$' : 'H',
                '^' : 'h',
                '!' : 'I',
                '7' : 'i',
                '&' : 'J',
                '}' : 'j',
                't' : 'K',
                'i' : 'k',
                'I' : 'L',
                'u' : 'l',
                'q' : 'M',
                'e' : 'm',
                'Q' : 'N',
                '*' : 'n',
                'r' : 'O',
                'B' : 'o',
                '=' : 'P',
                'b' : 'p',
                'j' : 'Q',
                '.' : 'q',
                '>' : 'R',
                'J' : 'r',
                'z' : 'S',
                '<' : 's',
                'Y' : 'T',
                'd' : 't',
                'A' : 'U',
                'Z' : 'u',
                'y' : 'V',
                'a' : 'v',
                '[' : 'W',
                'D' : 'w',
                'V' : 'X',
                'x' : 'x',
                'n' : 'Y',
                'v' : 'y',
                '~' : 'Z',
                '`' : 'z',
                '-' : ' '
            }
    
    if encryptedString == '':
        return None

    decryptedString = ''

    # For every character in the string
    for i in range(len(encryptedString)):

        # Find the value of the character in the dictionary and append it to a new string
        decryptedString += codes[encryptedString[i]]

    return decryptedString
                        
