# LAB4
#Due Date: 10/10/2020, 11:59PM
"""                                   
### Collaboration Statement: I worked on this assignment alone, using only this semester's materials
"""

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.pop()
        8.76
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        pass


    def pop(self):
        # --- YOUR CODE STARTS HERE
        pass