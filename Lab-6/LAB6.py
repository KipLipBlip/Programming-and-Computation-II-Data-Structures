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
        return f'{self.heap}'

    __repr__=__str__

    def __len__(self):

        # The length of the heap is 

        # YOUR CODE STARTS HERE
        pass

    @property
    def getMin(self):
        # YOUR CODE STARTS HERE
        pass
    

    def leftChild(self,index):
        # YOUR CODE STARTS HERE
        pass


    def rightChild(self,index):
        # YOUR CODE STARTS HERE
        pass


    def insert(self,item):
        # YOUR CODE STARTS HERE
        pass
            

    def deleteMin(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            x=self.heap[0]
            self.heap=[]
            return x 

        # YOUR CODE STARTS HERE
