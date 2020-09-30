# LAB3
#Due Date: 10/03/2020, 11:59PM
"""                                   
### Collaboration Statement: I worked on this assignment alone, using only this semester's materials
"""

'''
    REMINDER: All functions should NOT contain any for/while loops or global variables. 
    Use recursion, otherwise no credit will be given
'''

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
    """
  
    # Duplicate the list
    a = aList

    # If the list is empty: Breaking condition
    if not a:
        return

    # Remove the negative index and the one next to it.. If there are enough indices
    elif len(a) >= 2 and a[0] < 0:
        a.pop(0)
        a.pop(0)
        return removing(a)

    # Remove the negative index.. this is the last index
    elif len(a) == 1 and a[0] < 0:
        a.pop(0)
        return removing(a)

    # Temporarily remove the index and add it back later
    else:
        return aList[0] + removing(a)


def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)]
        q
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """

    a = str(n)

    # Not enough characters to compare two: Breaking condition
    if len(a) == 1:
        return a[0]

    # Check if there are enough indicies to check
    if len(a) >= 2:

        # The neighbours are the same, remove cuurent and move on
        if a[0] == a[1]:
            return neighbor( int(a[1:]) )

        # The neighbours are not the same, remove cuurent and move on, but add current back later
        elif a[0] != a[1]:
            n = str(n)
            return n[0] + neighbor( a[1:] )

    
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
    """

    # Check if the first str is in the second str
    if txt1 in txt2:    

        # If this character and the next are the same, we can remove the first one
        if txt1[0] == txt2[0] and txt1[1] == txt2[1]:
            txt1[1:]
            txt2[1:]
            return missedChar(txt1, txt2)


    # The first str is no longer in the second str: Break condition
    else:
        if len(txt2) > 0:
            return txt2


