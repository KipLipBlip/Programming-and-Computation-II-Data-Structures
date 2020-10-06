# LAB3
#Due Date: 10/03/2020, 11:59PM
"""                                   
### Collaboration Statement: I worked on this assignment alone, using only this semester's materials
"""

'''
    REMINDER: All functions should NOT contain any for/while loops or global variables. 
    Use recursion, otherwise no credit will be given
'''

# ** Done
def skipping(n):
    '''
        >>> skipping(4)
        6
        >>> skipping(6)
        12
        >>> skipping(11)
        36
    '''
    if n <= 0:
        return 0
    else:        
        return skipping(n-2) + n


# ** Done
def removing(aList):
    """
        >>> removing([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> removing(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> removing([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> removing([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> removing([-1,-2,-3,-4])
        []
        >>> removing([-1,5,-3,-4,5,8,9])
        [5, 8, 9]
    """
  
    # Duplicate the list
    a = aList

    # If the list is empty: Breaking condition
    if len(aList) == 0:

        return aList

    # General negative case, remove the abs -1 neighboring indices 
    elif len(a) >=2 and a[0] < 0:
        
        i = abs(a[0])
        return removing(a[i:])

    # Check last index
    elif len(a) == 1 and a[0] < 0:

        return removing(a[1:])

    # Temporarily remove the index and add it back later
    else:
        return [aList[0]] + removing(a[1:])


# ** Done
def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
        >>> neighbor(57453454324436)
        5745345432436
    """

    # Convert to str
    a = str(n)

    # Not enough characters to compare two: Breaking condition
    if len(a) == 1:
        return int(a[0])

    # Check if there are enough indicies to check
    if len(a) >= 2:

        # The neighbours are the same, remove cuurent and move on
        if a[0] == a[1]:
            return int(neighbor( a[1:] ))

        # The neighbours are not the same, remove cuurent and move on, but add current back later
        elif a[0] != a[1]:
            return int(a[0] + str(neighbor( a[1:] )))


# ** Done    
def missedChar(txt1, txt2):
    """
        >>> missedChar("owl", "howl")
        'h'
        >>> missedChar("want", "wanton")
        'on'
        >>> missedChar("rat", "radiate")
        'diae'
        >>> missedChar('at','treatise')
        'treise'
        >>> missedChar('to','encapsulation')
        'encapsulain'
        >>> missedChar('an','encapsulation')
        'encpsulatio'
    """

    # Breaking case, add back what is left of txt2
    if len(txt1) == 0 or len(txt2) == 0:
        return txt2

    # If they dont match, this is a character that we need to keep, add it back
    elif txt1[0] != txt2[0]:
        return txt2[0] + missedChar(txt1, txt2[1:])

    # Otherwise just iterate
    else:
        return missedChar(txt1[1:], txt2[1:])

