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

        >>> h = MinPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.insert(14)
        >>> h.insert(9)
        >>> h.insert(2)
        >>> h.insert(11)
        >>> h.insert(14)
        >>> h.insert(20)
        >>> h.insert(20)
        >>> h.insert(1)
        >>> h.insert(1)
        >>> h.insert(-1)
        >>> h.insert(0)
        >>> h.insert(0)
        
        >>> items = [6, 76.8, 0, 34, -15, 0, 34, 1, -2, -5, 1, 1, 22, 7, 9, 105.7]
        >>> h = MinPriorityQueue()
        >>> for number in items:
        ...     h.insert(number)
        >>> h
        [-15, -5, 0, 0, -2, 1, 7, 76.8, 1, 34, 1, 6, 22, 34, 9, 105.7]
        >>> h.deleteMin()
        -15
        >>> h.deleteMin()
        -5
        >>> h.deleteMin()
        -2
        >>> h
        [0, 1, 0, 9, 1, 1, 7, 76.8, 34, 34, 105.7, 6, 22]
        >>> h.insert(22.5)
        >>> h
        [0, 1, 0, 9, 1, 1, 7, 76.8, 34, 34, 105.7, 6, 22, 22.5]
        >>> h.deleteMin()
        0
        >>> h.deleteMin()
        0
        >>> h.deleteMin()
        1
        >>> h.deleteMin()
        1
        >>> h.deleteMin()
        1
        >>> h.deleteMin()
        6
        >>> h
        [7, 9, 34, 22.5, 22, 105.7, 34, 76.8]
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.heap=[]
        
    def __str__(self):
        ''' String representation of this object '''

        # Don't include the first index
        return f'{self.heap[1:]}'

    __repr__=__str__

    def __len__(self):
        ''' The number of elements in the heap '''

        # Return the length of the heap attribute, subtract 1 because we don't use list index 0
        return len(self.heap)-1

    @property
    def getMin(self):
        ''' Gets the minimum value in the heap '''
        
        # A min heap will always have the root as the minimum value
        if len(self.heap)-1 >= 1:
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

    def insert(self,item):
        ''' Inserts an item to the minimum heap '''

        # len() will initially return len(self.heap-1), so if the list is empty it will return -1, we need to fill index 0 before inserting
        if len(self.heap) <= 0:
            self.heap.append(0)

        # Insert by appending to the self.heap list
        self.heap.append(item)

        # Check to see if the min-heap property is still valid
        self.validateMinHeap()

    def deleteMin(self):
        ''' Removes the minimum element of the heap '''

        if len(self) == 0:
            return None    

        elif len(self) == 1:
            x = self.heap[0]
            self.heap = []
            return x

        # General Case (If children have the same value, go left)
        else:
            
            # Min value will be the root, index 1
            L = self.leftChild(1)
            R = self.rightChild(1)

            # Save value to return later
            value = self.getMin

            # Check if both children have the same value
            if L == R:
                
                self.heap[1] = self.heap[-1]
                self.heap.pop()
            
            elif L < R:

                self.heap[1] = self.heap[-1]
                self.heap.pop()

            elif R < L:

                self.heap[1] = self.heap[-1]
                self.heap.pop()
                
            # Run check
            self.validateMinHeap()

            return value

    def validateMinHeap(self):
        ''' Determines whether the heap is a valid min-heap, corrects by swapping if not '''

        # If the heap is empty, return True, this case will rarely be used
        if len(self.heap)-1 == 0:
            return True

        # Compare all children to their roots
        else:

            # Continue swapping until everything is in proper order
            while True:
                
                count = 0

                # Iterate through all the indices
                for k in range(1, len(self.heap)-1):

                    # Value of left and right child
                    L = self.leftChild(k)
                    R = self.rightChild(k)

                    # Avoid index error
                    if L == None and R == None:

                        # No children
                        break

                    elif L != None and R == None:

                        # Only a left child

                        if L < self.heap[k]:
                            # Swap the parent with the child, Index 2k
                            self.heap[2*k] = self.heap[k]
                            self.heap[k] = L

                            count += 1

                    elif R != None and L == None:

                        if R < self.heap[k]:

                            # Swap the parent with the child, Index 2k+1
                            self.heap[(2*k)+1] = self.heap[k]
                            self.heap[k] = R

                            count += 1

                    else:

                        # Two Children

                        if L < self.heap[k] and R < self.heap[k]:

                            # Both less than parent, choose smaller
                            if L < R:

                                # Swap the parent with the child, Index 2k
                                self.heap[2*k] = self.heap[k]
                                self.heap[k] = L

                                count += 1

                            elif R < L:

                                # Swap the parent with the child, Index 2k+1
                                self.heap[(2*k)+1] = self.heap[k]
                                self.heap[k] = R

                                count += 1

                        else:

                            # The left child is less than the parent, not valid min-heap
                            if L < self.heap[k]:

                                # Swap the parent with the child, Index 2k
                                self.heap[2*k] = self.heap[k]
                                self.heap[k] = L

                                count += 1

                            # The right child is less than the parent, not valid min-heap
                            if R < self.heap[k]:

                                # Swap the parent with the child, Index 2k+1
                                self.heap[(2*k)+1] = self.heap[k]
                                self.heap[k] = R

                                count += 1

                # Break condition
                if count == 0:
                    break

            # Return True once the while loop has finished
            return True