#Lab #6
#Due Date: 11/07/2020, 11:59PM 
'''                                 
# Collaboration Statement:   
        I worked on this assignment alone, using only this semester's materials
'''

class MinPriorityQueue:
    '''
        >>> h = MinPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h.heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h.leftChild(1)
        5
        >>> h.rightChild(1)
        11
        >>> h.leftChild(6)
        >>> h.rightChild(9)
        >>> h.deleteMin()
        2
        >>> h.heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.heap=[]
        
    def __str__(self):
        ''' String representation of this object '''

        return f'{self.heap}'

    __repr__=__str__

    def __len__(self):
        ''' The number of elements in the heap '''

        # Retunr the length of the heap attribute, subtract 1 because we don't use list index 0
        return len(self.heap)-1

    @property
    def getMin(self):
        ''' Gets the minimum value in the heap '''
        
        # A min heap will always have the root as the minimum value
        if self.len(self.heap) != 0:
            return self.heap[1]
            
        # Return None if the heap is empty
        else:
            return None
    
    def leftChild(self,index):
        ''' Gets the value of the left child of the node at an index '''
        
        # The left child is located at the 2k index, return this
        try:
            return self.heap[2*index]

        # If there is no index, we will get an index error, return None as specified
        except IndexError:
            return None

    def rightChild(self,index):
        ''' Gets the value of the right child of the node at an index '''

        # The right child is located at the 2k+1 index, return this
        try:
            return self.heap[(2*index)+1]

        # If there is no index, we will get an index error, return None as specified
        except IndexError:
            return None

    def parent(self,index):
        ''' Gets the value of the parent of the node at an index '''

        # The parent node is located at the k/2 index, return this
        try:
            return self.heap[index/2]

        # If there is no index, we will get an index error, return None as specified
        except IndexError:
            return None

    def insert(self,item):
        ''' Inserts an item to the minimum heap '''

        # Insert by appending to the self.heap list
        self.heap.append(item)

        # Check to see if the min-heap property is still valid, otherwise fix


    def deleteMin(self):
        ''' Removes the minimum element of the heap '''

        if len(self)==0:
            return None        
        elif len(self)==1:
            x=self.heap[0]
            self.heap=[]
            return x

        # YOUR CODE STARTS HERE

    def validateMinHeap(self):
        ''' Determines whether the heap is a valid min-heap '''

        
