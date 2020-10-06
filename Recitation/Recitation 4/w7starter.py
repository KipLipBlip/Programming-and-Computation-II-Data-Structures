class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count = 0


    def __str__(self):
    	temp=self.head
    	out=[]
    	while temp:
    		out.append(str(temp.value))
    		temp=temp.next
    	out=' -> '.join(out)
    	return f'Head: {self.head}\nTail: {self.tail}\nList: {out}'


    __repr__=__str__


    def isEmpty(self):
        # Head points to none
        return self.head == None


    def add(self, value):
        # Put before the head, update the head
        newNode = Node(value)
        self.count += 1

        # Head is None
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        
        # There is already a head node, change the head value, and assign the previous head to next
        else:
            newNode.next = self.head
            self.head = newNode


    def append(self, value):
        # Add to the end of the list
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

    # For lab 4: modify add with while loop.. ascending order || also implement pop, a subfunction of del ( last value )



    # ! Not efficient
    # def __len__(self):

    #     # Initialize starter value
    #     current = self.head
    #     i = 0

    #     # Move through all the elements in the list
    #     while current:
    #         # Count the node
    #         i += 1

    #         # Update to the next node
    #         current = current.next