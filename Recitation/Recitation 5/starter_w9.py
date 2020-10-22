############### Coding question 1

def isMinHeap(aTree):
    '''
    >>> isMinHeap([1,4,7,6,9,10,8])
    True
    >>> isMinHeap([1,3,2,4,6,9,5,15,10,13,8,14,11,12,7])
    True
    >>> isMinHeap([2,3,5,4,6,9,7,15,10,13,8,14,11,12])
    True
    >>> isMinHeap([93, 15, 87, 7, 15, 5])
    False
    >>> isMinHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    False
    >>> isMinHeap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    False
    >>> isMinHeap([2, 3, 4, 6, 7, 5, 8, 9])
    True
    >>> isMinHeap([3, 6, 4, 9, 7, 5, 8])
    True
    >>> isMinHeap([4, 6, 5, 9, 7, 8])
    True
    >>> isMinHeap([82 ,2, 3, 4, 6, 7, 5, 8, 9])
    False
    '''
    # Assume each root has two branches
    
    if len(aTree) % 2 != 0:

        for i in range(len(aTree)):

            if aTree[-1] < aTree[-3]:

                # Swap root & branch
                temp = aTree[-3]
                aTree[-3] = aTree[-1]
                aTree[-1] = temp

            if aTree[-1] < aTree[-2]:

                # Swap root & branch
                temp = aTree[-2]
                aTree[-2] = aTree[-1]
                aTree[-1] = temp

            # Check again then remove if good

            if aTree[-1] < aTree[-3] and aTree[-2] < aTree[-3]:
                pass

############### Coding question 2

# Pre-Order: Root-Left-Right
# In-Order: Left-Root-Right (ascending order of value)
# Post Order: Left-Right-Root

def tree(root_value, subtrees=[]):
    '''
        >>> tree(5)
        [5, [], []]
        >>> tree(5,[[5, [], []], [6, [], []]])
        [5, [5, [], []], [6, [], []]]
        >>> tree(5,[[5, [], []]])
        [5, [5, [], []], []]
    '''
    if subtrees==[]:
        return [root_value] + [[],[]]
    if len(subtrees)==1:
        return [root_value] + list(subtrees) +[[]]
    return [root_value] + list(subtrees)

def subtrees(tree):
    pass

def root(tree):
	pass


def isLeaf(tree):
	pass

def sprout(t, values):
	pass