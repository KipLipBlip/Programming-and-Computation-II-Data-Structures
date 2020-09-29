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
    # Break case? - No more negatives
    # n = 0
    # a = aList
    # if len(a) == 1 and a[0] >= 0:
    #     return aList

    # elif a[0] < 0 and len(a)>2:
    #     # If you can, remove the negative and the index next to it
    #     print(f'found({a[0]},{a[1]})')
    #     a.pop(0)
    #     a.pop(0)
    #     print(f'list: {a}, here and friend')
    #     return removing(a)
    # elif a[0] < 0:
    #     # There is no index next to this one, pop it and return
    #     print(f'found({a[0]})')
    #     a.pop(0)
    #     print(f'list: {a}, here and no friend')
    #     return removing(a)
    # else:
    #     # Remove the index to progress, but add it back when all is returned
    #     a.pop(0)
    #     print(f'list: {a}, move on')
    #     if len(removing(a)) == 1:
    #         return aList
    #     else:
    #         return aList + removing(a)

    a = aList

    if not a:
        # The list is empty
        return

    if ( len(a) >= 1 and a[0] >= 0 ):
        # Temporarily remove index 0 but add it back after functions give back
        return aList + removing(a)
    elif len(a) >= 2 and a[0] < 0:
        # Remove friend and neighbour and call removing
        a.pop(0)
        a.pop(0)
        if len(a) == 0:

    elif len(a) == 1 and a[0] < 0:
        a.pop(0)
        if len(a) == 0:

    return removing(a)

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
    ## YOUR CODE STARTS HERE
    pass
    


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
    ## YOUR CODE STARTS HERE
    pass

    # print(type(aList))

    # if len(aList) == 0:
    #     return aList

    # if aList[n] < 0:
    #     aList.pop(n)
    #     if len(aList) >= n+2:
    #         aList.pop(n+1)

    #     if len(aList) > n+1:
    #         return removing(a)
    # else:
    #     s = removing( aList.pop(n) )
    #     p = [ aList[n] ]
    #     p.append(s)
    #     return p
