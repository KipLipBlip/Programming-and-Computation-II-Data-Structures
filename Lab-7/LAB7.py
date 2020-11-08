#Lab #7
#Due Date: 11/14/2020, 11:59PM 
'''                                 
# Collaboration Statement:   

'''



class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> len(x)
        2
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        pass
        

    def enqueue(self, value):
        # YOUR CODE STARTS HERE
        pass
        


    def dequeue(self):
        # YOUR CODE STARTS HERE
        pass
        

    def __len__(self):
        # YOUR CODE STARTS HERE
        pass





class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        '''
            Method uses an instance of the Queue class to process nodes
            
            >>> g1 = {'A': ['B','D','G'],
            ... 'B': ['A','E','F'],
            ... 'C': ['F'],
            ... 'D': ['A','F'],
            ... 'E': ['B','G'],
            ... 'F': ['B','C','D'],
            ... 'G': ['A','E']}
            >>> g=Graph(g1)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'G', 'E', 'F', 'C']
        '''
        # YOUR CODE STARTS HERE
        pass








# ---------------- EXTRA CREDIT -------------- #
def bubbleSort(numList):
    '''
        >>> bubbleSort([9,3,5,4,1,67,78])
        ({1: [3, 5, 4, 1, 9, 67, 78], 2: [3, 4, 1, 5, 9, 67, 78], 3: [3, 1, 4, 5, 9, 67, 78], 4: [1, 3, 4, 5, 9, 67, 78], 5: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
        >>> bubbleSort([3,6,8,9])
        ({1: [3, 6, 8, 9]}, [3, 6, 8, 9])
        >>> bubbleSort([3,6,-1,9,12])
        ({1: [3, -1, 6, 9, 12], 2: [-1, 3, 6, 9, 12], 3: [-1, 3, 6, 9, 12]}, [-1, 3, 6, 9, 12])
    '''
    # YOUR CODE STARTS HERE
    pass