#Lab #5
#Due Date: 10/31/2020, 11:59PM 
'''                                  
# Collaboration Statement: 

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


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
    	# YOUR CODE STARTS HERE
    	pass


    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        pass


    @property
    def getMax(self): 
        i# YOUR CODE STARTS HERE
        pass


    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        pass

    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        pass


    
    def numChildren(self, node):
        # YOUR CODE STARTS HERE
        pass

        


