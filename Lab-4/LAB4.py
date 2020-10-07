# LAB4
#Due Date: 10/10/2020, 11:59PM
"""                                   
### Collaboration Statement: I worked on this assignment alone, using only this semester's materials
"""

# For lab 4: modify add with while loop.. ascending order

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
        ''' Put before the head, update the head '''
        newNode = Node(value)
        self.count += 1

        # Head is None
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        
        # There is already a head node, change the head value, and assign the previous head to next
        else:

            previous = None
            current = self.head

            while current is not None and current.value <= value:

                # Iterate
                previous = current
                current = current.next

            # Havent gone anywhere
            if current == self.head:

                newNode.next = self.head
                self.head = newNode

            # End of the list
            elif current is None:

                # Just append the value
                self.append(value)
                self.count -= 1
            
            # Sanwiched between two values
            else:
                ''' [prev] -> [current] -> [curr.next] '''

                # Check values
                # if previous.value <= value and current.value >= value:

                newNode.next = current
                previous.next = newNode


    def pop(self):
        ''' Delete the last value '''

        if self.isEmpty():
            return None

        # Only one node, going to be empty
        if len(self) == 1:
            self.head = None
            self.tail = None

        # Starter values
        current = self.head
        previous = None

        # While not at end and searching value is not value found (don't messesarily need to go to end)
        while current is not None and current != self.tail:
            
            previous = current
            current = current.next

        # Remove previous tail link
        previous.next = None

        # Update tail
        self.tail = previous

        # Decrement the count
        self.count -= 1

        return current.value


    def append(self, value):
        ''' Add to the end of the list '''
        newNode = Node(value)
        self.count += 1

        # Check if the list is empty
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        
        # Change the last node's next from none to the newNode, add the newNode to tail
        else:
            self.tail.next = newNode
            self.tail = newNode


    def __contains__(self, value):
        ''' Search for item inside '''

        # Initialize starter value
        current = self.head

        # Move through all the elements in the list
        while current:

            # If the value matches, return True
            if current.value == value:
                return True

            # Update to the next node
            current = current.next

        # Not found
        return False


    def __delitem__(self, value):
        ''' Delete an item '''

        # Empty case
        if self.isEmpty():
            print('List is empty')
            return None

        # Only one node, going to be empty
        if len(self) == 1:
            self.head = None
            self.tail = None

        # General case, more than one element
        else:
            # Get current and previous (nothing before the head)
            current = self.head
            previous = None

            # While not at end and searching value is not value found (don't messesarily need to go to end)
            while current is not None and current.value != value:
                
                previous = current
                current = current.next

            # Item is not in the list
            if current is None:
                print('Value not found')
                return None

            # The value is the head
            elif previous is None:
                self.head = current.next
                # Break the link
                current.next = None

            # The node we del is the tail, next is the last item in the list
            elif current.next is None:
                # Remove tail, break the link
                previous.next = None

                # Reassign tail
                self.tail = previous

            # Most general: in the middle of the list
            else:

                previous.next = current.next
                # Break current to next link
                current.next = None

        # Decrement the count
        self.count -= 1