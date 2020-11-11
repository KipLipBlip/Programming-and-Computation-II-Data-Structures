#Lab #7
#Due Date: 11/14/2020, 11:59PM 
'''                                 
# Collaboration Statement:   
        I worked on this assignment alone, using only this semester's materials.
'''

class Node:
    def __init__(self, value):
        ''' Constructor '''
        self.value = value  
        self.next = None 
    
    def __str__(self):
        ''' String representation of this object '''
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

        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.enqueue(4)
        >>> print(x)
        Head:Node(1)
        Tail:Node(4)
        Queue:1 -> 2 -> 3 -> 4
        >>> x.isEmpty()
        False
        >>> len(x)
        4
        >>> x.dequeue()
        1
        >>> x.dequeue()
        2
        >>> x.dequeue()
        3
        >>> x.dequeue()
        4
        >>> x.dequeue()
        >>> print(x)
        Head:None
        Tail:None
        Queue:
        >>> x.enqueue(3)
        >>> x.enqueue(2)
        >>> print(x)
        Head:Node(3)
        Tail:Node(2)
        Queue:3 -> 2
        >>> x.dequeue()
        3
        >>> print(x)
        Head:Node(2)
        Tail:Node(2)
        Queue:2
        >>> x.dequeue()
        2
        >>> print(x)
        Head:None
        Tail:None
        Queue:
    '''

    def __init__(self):
        ''' Constructor '''
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        ''' String representation of this object '''
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        ''' Tests to see whether the queue is empty '''
        # If there no length the queue is empty
        return self.count == 0
        
    def enqueue(self, value):
        ''' Adds a new item to the back of the queue '''
        
        # Create the Node
        i = Node(value)

        if self.isEmpty():
            # This is the first node in the queue: Head and Tail

            self.head = i
            self.tail = i

        else:
            # This becomes the new tail, update previous next pointer
            
            self.tail = i

            if len(self) == 1:
                # There is only a head node
                
                self.head.next = i

            else:
                # Most general case

                j = self.head.next

                # Go to the second to last node and update that .next pointer
                for k in range(len(self)-2):
                    j = j.next

                j.next = i

        # Increment the size
        self.count += 1

    def dequeue(self):
        ''' Removes an item from the front of the queue '''
        
        # Check for empty queue
        if self.isEmpty():
            return None

        else:
            # Remove current head next reference, then make new head reference
            temp = self.head
            self.head = self.head.next
            temp.next = None

            # Decrement the size
            self.count -= 1 

            # Remove head and tail pointers if empty
            if self.count == 0:
                self.tail = None
                self.head = None

            return temp.value

    def __len__(self):
        ''' The number of elements in the queue '''
        # Use size attribute
        return self.count

class Graph:

    def __init__(self, graph_repr):
        ''' Constructor '''
        self.vertList = graph_repr

    def bfs(self, start):
        '''
            Returns the breadth-first search traversal of this graph

            This method uses an instance of the Queue class to process nodes
            
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

            >>> g1 = {'A': ['B', 'D', 'G'],
            ...       'B': ['A', 'E', 'F'],
            ...       'C': ['F'],
            ...       'D': ['A', 'F'],
            ...       'E': ['B', 'G'],
            ...       'F': ['B', 'C', 'D'],
            ...       'G': ['A', 'E']}
            >>> g = Graph(g1)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'G', 'E', 'F', 'C']
            >>> g2 = {'F': ['D', 'C', 'B'],
            ...       'A': ['G', 'D', 'B'],
            ...       'B': ['F', 'A', 'E'],
            ...       'E': ['G', 'B'],
            ...       'C': ['F'],
            ...       'D': ['F', 'A'],
            ...       'G': ['A', 'E']}
            >>> g = Graph(g2)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'G', 'E', 'F', 'C']
            >>> g3 = {'B': [('E', 3), ('C', 5)],
            ...       'F': [],
            ...       'C': [('F', 2)],
            ...       'A': [('D', 3), ('B', 2)],
            ...       'D': [('C', 1)],
            ...       'E': [('F', 4)]}
            >>> g =Graph(g3)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'C', 'E', 'F']
            >>> g4 = {'Bran': ['East', 'Cap'],
            ...       'Flor': [],
            ...       'Cap':  ['Flor'],
            ...       'Apr':  ['Dec', 'Bran'],
            ...       'Dec':  ['Cap'],
            ...       'East': ['Flor']}
            >>> g = Graph(g4)
            >>> g.bfs('Apr')
            ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor']
        '''
        
        # Create a visited list
        visited = []

        # Instantiate a Queue, Enqueue the starter Node, Mark start as visited 
        Q = Queue()
        Q.enqueue(start)
        visited.append(start)

        # Continue process until there are no more unvisited nodes
        while not Q.isEmpty():

            # Initially dequeue the start
            parent = Q.dequeue()

            if len(self.vertList[parent]) == 0:
                
                break
            
            elif isinstance(self.vertList[parent][0], tuple):
                # Check for weighted graph ('node', weight)
                temp = []

                # Add the values based on weight to temp
                for i in range(len(self.vertList[parent])):
                   
                    temp.append(self.vertList[parent][i][0])

                temp.sort()

                self.vertList[parent] = temp

            else:
                # Alphabetically sort neighbours
                self.vertList[parent].sort()

            # Loop through neighbours
            for neighbour in self.vertList[parent]:

                # If neighbour hasn't been visited, add to queue
                if neighbour not in visited:

                    Q.enqueue(neighbour)
                    visited.append(neighbour)

            # Add this neighbour to visited list
            if parent not in visited:

                visited.append(parent)
                
        # Return the BFS traversal
        return visited

# ---------------- EXTRA CREDIT -------------- #
# def bubbleSort(numList):
#     '''
#         >>> bubbleSort([9,3,5,4,1,67,78])
#         ({1: [3, 5, 4, 1, 9, 67, 78], 2: [3, 4, 1, 5, 9, 67, 78], 3: [3, 1, 4, 5, 9, 67, 78], 4: [1, 3, 4, 5, 9, 67, 78], 5: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
#         >>> bubbleSort([3,6,8,9])
#         ({1: [3, 6, 8, 9]}, [3, 6, 8, 9])
#         >>> bubbleSort([3,6,-1,9,12])
#         ({1: [3, -1, 6, 9, 12], 2: [-1, 3, 6, 9, 12], 3: [-1, 3, 6, 9, 12]}, [-1, 3, 6, 9, 12])
#     '''
#     # YOUR CODE STARTS HERE
#     pass