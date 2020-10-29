#Lab #5
#Due Date: 10/31/2020, 11:59PM 
'''                                  
# Collaboration Statement:
    I worked on this assignment alone using only this semester's material
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.numChildren(x.root)
        2
        >>> x.numChildren(x.root.left)
        2
        >>> x.numChildren(x.root.right)
        1
        >>> x.getMin
        2
        >>> x.getMax
        11
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.isEmpty()
        False

        # BFS
        #   Level Search
        # DFS
        #   PreOrder
        #       root-left-right
        #   InOrder
        #       left-root-right
        #   PostOrder
        #       left-right-root
    '''

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def isEmpty(self):
        ''' Tests to see whether the tree is empty or not '''
        return self.root == None

    @property
    def getMin(self):
        ''' Gets the minimum value in the tree '''

        # Check for empty tree
        if self.root is None:
            return None

        # Traverse the list and return the min value        
        return min(self.bfs())

    @property
    def getMax(self):
        ''' Gets the maximum value in the tree '''

        # Check for empty tree
        if self.root is None:
            return None

        # Traverse the list and return the min value        
        return max(self.bfs())

    def getHeight(self, node):
        ''' Gets the height of a node in the tree '''

        if node.left is None and node.right is None:

            # Base case: This is a leaf, nothing below this

            return 0

        elif node.right is None and node.left is not None:

            # There is a left node but no right node

            return 1 + self.getHeight(node.left)

        elif node.left is None and node.right is not None:

            # There is a right node but no left node

            return 1 + self.getHeight(node.right)

        elif node.left is not None and node.right is not None:

            # There is a left node and a right node

            return 1 + max( self.getHeight(node.left), self.getHeight(node.right) )

    def __contains__(self, value):
        ''' Checks if a value is present in the tree '''

        # Check for empty tree
        if self.root is None:
            return None

        # Traverse the list and return the min value        
        return value in self.bfs()

    def numChildren(self, node):
        ''' Gets the number of children node_object has '''

        i = 0

        # Check for empty tree
        if self.root is None:
            return None

        # Check left & right node
        if node.left != None:
            i+=1
        if node.right != None:
            i+=1
        
        return i

    def bfs(self):
        ''' Level Search '''

        # Check for empty tree
        if self.root is None:
            return None
        
        # Create queue and add root
        q = Queue()
        visited = []
        q.enqueue(self.root)

        while not q.isEmpty():
            node = q.dequeue()
            visited.append(node.value)

            # Check the left side
            if node.left is not None:
                q.enqueue((node.left))

            # Check the right side
            if node.right is not None:
                q.enqueue((node.right))

        return visited

