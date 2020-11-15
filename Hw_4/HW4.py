# HW4
# Due Date: 11/21/2020, 11:59PM
'''                                   
### Collaboration Statement:
        I worked on this assignment alone, using only this semeseter's materials

### Description:
        The overall cache structure will be implemented as a hash table using separate chaining for collision resolution,
        with each individual level implemented as a linked list.
'''

class Node:

    def __init__(self, content):
        ''' Constructor '''
        self.value = content
        self.next = None

    def __str__(self):
        ''' Object's string representation '''
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__

class ContentItem:
    '''
        >>> content1 = ContentItem(1000, 10, 'Content-Type: 0', '0xA')
        >>> content2 = ContentItem(1004, 50, 'Content-Type: 1', '110010')
        >>> content3 = ContentItem(1005, 18, 'Content-Type: 2', '<html><p>'CMPSC132'</p></html>')
        >>> content4 = ContentItem(1005, 18, 'another header', '111110')
        >>> hash(content1)
        0
        >>> hash(content2)
        1
        >>> hash(content3)
        2
        >>> hash(content4)
        1
    '''

    def __init__(self, cid, size, header, content):
        ''' Constructor '''
        self.cid = cid              # Stores the content id.
        self.size = size            # Stores the size of the content as a nonnegative integer.
        self.header = header        # Information stored by the ContentItem (used for hash function later).
        self.content = content      # Information stored by the ContentItem.

    def __str__(self):
        ''' Object's string representation '''
        return f'CONTENT ID: {self.cid} SIZE: {self.size} HEADER: {self.header} CONTENT: {self.content}'

    __repr__=__str__

    def __eq__(self, other):
        ''' Equality operator '''
        if isinstance(other, ContentItem):
            return self.cid == other.cid and self.size == other.size and self.header == other.header and self.content == other.content
        return False

    def __hash__(self):
        ''' Returns the hash value for this ContentItem. '''
        # Let the hash value be equal to the sum of every ASCII value in the header, modulo 3
        
        h = 0

        # Iterate through each letter of the header
        for i in range(len(self.header)):
            
            # Add ascii's value to sum
            h += ord(self.header[i])
        
        return h % 3

class CacheList:
    '''
        >>> content1 = ContentItem(1000, 10, 'Content-Type: 0', '0xA')
        >>> content2 = ContentItem(1004, 50, 'Content-Type: 1', '110010')
        >>> content3 = ContentItem(1005, 180, 'Content-Type: 2', '<html><p>'CMPSC132'</p></html>')
        >>> content4 = ContentItem(1006, 18, 'another header', '111110')
        >>> content5 = ContentItem(1008, 2, 'items', '11x1110')
        >>> lst=CacheList(200)
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>

        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst.put(content2, 'lru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> lst.put(content4, 'mru')
        'INSERTED: CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110'
        >>> lst
        REMAINING SPACE:122
        ITEMS:3
        LIST:
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        
        >>> lst.put(content5, 'mru')
        'INSERTED: CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110'
        >>> lst
        REMAINING SPACE:120
        ITEMS:4
        LIST:
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>

        >>> lst.put(content3, 'lru')
        'INSERTED: CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>'
        >>> lst
        REMAINING SPACE:0
        ITEMS:3
        LIST:
        [CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>]
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        <BLANKLINE>

        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        <BLANKLINE>

        >>> lst.find(1006)
        CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        <BLANKLINE>

        >>> contentExtra = ContentItem(1034, 2, 'items', 'other content')
        >>> lst.update(1008, contentExtra)
        'UPDATED: CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content'
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        >>> lst.clear()
        'Cleared cache!'
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
    '''
    def __init__(self, size):
        ''' Constructor '''
        self.head = None                # Points to the first node in the linked list (defaults to None)
        self.maxSize = size             # Maximum size that the CacheList can store
        self.remainingSize = size       # Remaining size that the CacheList can store
        self.numItems = 0               # The number of items currently in the CacheList

    def __str__(self):
        ''' Object's string representation '''
        listString = ''
        current = self.head
        while current is not None:
            listString += '[' + str(current.value) + ']\n'
            current = current.next
        return 'REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}'.format(self.remainingSize, self.numItems, listString)  

    __repr__=__str__

    def __len__(self):
        ''' Length operator '''
        return self.numItems
    
    def put(self, content, evictionPolicy):
        ''' Adds Nodes at the beginning of the list. 
        
            Adds nodes at the beginning of the list and evicts items as necessary to free up 
            space. If the content is larger than the maximum size, do not evict anything. 
            Otherwise, if there is currently not enough space for the content, evict items 
            according to the eviction policy.If the content id exists in the list prior the
            insertion, content is not added into the list and the current content is moved
            to the beginning of the list
        '''

        # If the content is larger than the maximum size, do not evict anything.

        if content.size < self.maxSize:

            # If there is enough remaining space, just add the obj, no need to evict

            if content.size <= self.remainingSize:
                
                # Check for matching ID 

                if self.find(content.cid):

                    return 'Insertion of content item id not allowed. Content already in cache.'

                else:
                    # Add the content to the beginning of the linked list

                    h = self.head
                    nn = Node(content)

                    # Check for None head
                    if h:

                        # There is a head, shift everything down
                        nn.next, self.head = self.head, nn

                        # Increment numItems and decrement remaningSize
                        self.numItems += 1
                        self.remainingSize -= nn.value.size

                    else:
                        # There is no head, this node is the head
                        self.head = nn

                        # Increment numItems and decrement remaningSize
                        self.numItems += 1
                        self.remainingSize -= nn.value.size

            else:
                # There is currently not enough space for the content, evict items according to the eviction policy.

                if evictionPolicy.lower() == 'lru':

                    # Continue eviction until enough size
                    while self.remainingSize < content.size:

                        self.lruEvict()             # Removes last item in linked list

                    self.put(content, 'lru')

                elif evictionPolicy.lower() == 'mru':

                    # Continue eviction until enough size
                    while self.remainingSize < content.size:

                        self.mruEvict()             # Removes first item in linked list

                    self.put(content, 'mru')

        else:
            return 'Insertion not allowed. Content size is too large.'
        
        # Successful insertion
        return f'INSERTED: {content}'

    def find(self, cid):
        ''' Search for content in the list. 
        
            Finds a ContentItem from the list by id, moving the ContentItem to 
            the front of the list if found.
        '''
        
        h = self.head

        # Continue while there is a neighbour
        while h != None:

            if h.value.cid == cid:

                # Move node to front
                self.remove(h.value.cid)
                h.next, self.head = self.head, h

                # Return head
                return self.head

            # Iterate
            h = h.next
        
        # Default
        return None

    def update(self, cid, content):
        ''' Updates the content in the list. 
        
            Updates a ContentItem with a given id in the list. If a match is found, 
            it is moved to the beginning of the list and the old ContentItem is entirely 
            replaced with the new ContentItem. You can assume the size of the content 
            will not change while updating it
        '''

        # Search for the given CID
        c = self.find(cid)

        if c:
            # Move to the beginning of the list

            pass

        else:
            return None

    def mruEvict(self):
        ''' Removes the first item of the list. '''

        self.remainingSize += self.head.value.size  # Increase the remaining size
        self.numItems -= 1                          # Decrement the number of items

        # Make the head the head's next value
        self.head.next, self.head = None, self.head.next
    
    def lruEvict(self):
        ''' Removes the last item of the list. '''
        
        h = self.head

        # Get the next to last node, h
        for i in range(self.numItems-2):

            h = h.next

        self.remainingSize += h.next.value.size # Increase the reamining size
        self.numItems -= 1                      # Decrement the number of items

        h.next = None                           # Remove next pointer
    
    def clear(self):
        ''' Removes all items from the list. '''

        # Remove the head and reset original values
        self.head = None

        self.numItems = 0
        self.remainingSize = self.maxSize
    
        return 'Cleared cache!'

    def remove(self, cid):
        ''' Removes item by cid 
        
        >>> content1 = ContentItem(1000, 10, 'Content-Type: 0', '0xA')
        >>> content2 = ContentItem(1004, 50, 'Content-Type: 1', '110010')
        >>> content3 = ContentItem(1005, 180, 'Content-Type: 2', '<html><p>CMPSC132</p></html>')
        >>> lst = CacheList(300)

        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst.put(content2, 'mru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> lst.put(content3, 'mru')
        'INSERTED: CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>CMPSC132</p></html>'

        >>> lst
        REMAINING SPACE:60
        ITEMS:3
        LIST:
        [CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>CMPSC132</p></html>]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>

        # Remove head
        >>> lst.remove(1005)
        >>> lst
        REMAINING SPACE:240
        ITEMS:2
        LIST:
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]

        >>> lst.put(content3, 'mru')
        'INSERTED: CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>CMPSC132</p></html>'
        >>> lst
        REMAINING SPACE:60
        ITEMS:3
        LIST:
        [CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>CMPSC132</p></html>]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>

        # Remove last
        >>> lst.remove(1000)
        >>> lst
        REMAINING SPACE:70
        ITEMS:2
        LIST:
        [CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>CMPSC132</p></html>]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        <BLANKLINE>

        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst
        REMAINING SPACE:60
        ITEMS:3
        LIST:
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        [CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>CMPSC132</p></html>]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]

        # Remove middle
        >>> lst.remove(1005)
        >>> lst
        REMAINING SPACE:110
        ITEMS:2
        LIST:
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        <BLANKLINE>

        '''

        h = self.head

        for i in range(self.numItems):

            if h.value.cid == cid:

                # This is the node

                if h == self.head:

                    # Remove the head
                    self.remainingSize += self.head.value.size      # Increase the remaining size
                    self.numItems -= 1                              # Decrement the number of items

                    # Make the head the head's next value
                    self.head = self.head.next

                elif h.next == None:

                    # This is the last node

                    j = self.head

                    for i in range(self.numItems-2):

                        j = j.next

                    self.remainingSize += j.next.value.size         # Increase the remaining size
                    self.numItems -= 1                              # Decrement the number of items

                    j.next = None

                else:

                    # Most general case

                    j = self.head

                    for i in range(self.numItems):

                        # Avoid attr error
                        if j.next:

                            if j.next.value.cid == cid:
                            
                                # Reassign left node's next to right node

                                j.next = j.next.next

                                self.remainingSize += j.next.value.size         # Increase the remaining size
                                self.numItems -= 1                              # Decrement the number of items
                        else:
                            break

                        j = j.next

            h = h.next      


# class Cache:
#     '''
#         >>> cache = Cache()
#         >>> content1 = ContentItem(1000, 10, 'Content-Type: 0', '0xA')
#         >>> content2 = ContentItem(1003, 13, 'Content-Type: 0', '0xD')
#         >>> content3 = ContentItem(1008, 242, 'Content-Type: 0', '0xF2')

#         >>> content4 = ContentItem(1004, 50, 'Content-Type: 1', '110010')
#         >>> content5 = ContentItem(1001, 51, 'Content-Type: 1', '110011')
#         >>> content6 = ContentItem(1007, 155, 'Content-Type: 1', '10011011')

#         >>> content7 = ContentItem(1005, 18, 'Content-Type: 2', '<html><p>'CMPSC132'</p></html>')
#         >>> content8 = ContentItem(1002, 14, 'Content-Type: 2', '<html><h2>'PSU'</h2></html>')
#         >>> content9 = ContentItem(1006, 170, 'Content-Type: 2', '<html><button>'Click Me'</button></html>')

#         >>> cache.insert(content1, 'lru')
#         'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
#         >>> cache.insert(content2, 'lru')
#         'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
#         >>> cache.insert(content3, 'lru')
#         'Insertion not allowed. Content size is too large.'

#         >>> cache.insert(content4, 'lru')
#         'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
#         >>> cache.insert(content5, 'lru')
#         'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
#         >>> cache.insert(content6, 'lru')
#         'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'

#         >>> cache.insert(content7, 'lru')
#         'INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>'
#         >>> cache.insert(content8, 'lru')
#         'INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>'
#         >>> cache.insert(content9, 'lru')
#         'INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>'
#         >>> cache
#         L1 CACHE:
#         REMAINING SPACE:177
#         ITEMS:2
#         LIST:
#         [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
#         [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
#         <BLANKLINE>
#         L2 CACHE:
#         REMAINING SPACE:45
#         ITEMS:1
#         LIST:
#         [CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011]
#         <BLANKLINE>
#         L3 CACHE:
#         REMAINING SPACE:16
#         ITEMS:2
#         LIST:
#         [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
#         [CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>]
#         <BLANKLINE>
#         <BLANKLINE>
#         >>> cache.hierarchy[0].clear()
#         'Cleared cache!'
#         >>> cache.hierarchy[1].clear()
#         'Cleared cache!'
#         >>> cache.hierarchy[2].clear()
#         'Cleared cache!'
#         >>> cache
#         L1 CACHE:
#         REMAINING SPACE:200
#         ITEMS:0
#         LIST:
#         <BLANKLINE>
#         L2 CACHE:
#         REMAINING SPACE:200
#         ITEMS:0
#         LIST:
#         <BLANKLINE>
#         L3 CACHE:
#         REMAINING SPACE:200
#         ITEMS:0
#         LIST:
#         <BLANKLINE>
#         <BLANKLINE>
#         >>> cache.insert(content1, 'mru')
#         'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
#         >>> cache.insert(content2, 'mru')
#         'INSERTED: CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD'
#         >>> cache.retrieveContent(content1)
#         CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA
#         >>> cache.retrieveContent(content2)
#         CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD
#         >>> cache.retrieveContent(content3)
#         'Cache miss!'

#         >>> cache.insert(content5, 'lru')
#         'INSERTED: CONTENT ID: 1001 SIZE: 51 HEADER: Content-Type: 1 CONTENT: 110011'
#         >>> cache.insert(content6, 'lru')
#         'INSERTED: CONTENT ID: 1007 SIZE: 155 HEADER: Content-Type: 1 CONTENT: 10011011'
#         >>> cache.insert(content4, 'lru')
#         'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'


#         >>> cache.insert(content7, 'mru')
#         'INSERTED: CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>'
#         >>> cache.insert(content8, 'mru')
#         'INSERTED: CONTENT ID: 1002 SIZE: 14 HEADER: Content-Type: 2 CONTENT: <html><h2>'PSU'</h2></html>'
#         >>> cache.insert(content9, 'mru')
#         'INSERTED: CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>'
#         >>> cache
#         L1 CACHE:
#         REMAINING SPACE:177
#         ITEMS:2
#         LIST:
#         [CONTENT ID: 1003 SIZE: 13 HEADER: Content-Type: 0 CONTENT: 0xD]
#         [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
#         <BLANKLINE>
#         L2 CACHE:
#         REMAINING SPACE:150
#         ITEMS:1
#         LIST:
#         [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
#         <BLANKLINE>
#         L3 CACHE:
#         REMAINING SPACE:12
#         ITEMS:2
#         LIST:
#         [CONTENT ID: 1006 SIZE: 170 HEADER: Content-Type: 2 CONTENT: <html><button>'Click Me'</button></html>]
#         [CONTENT ID: 1005 SIZE: 18 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>]
#         <BLANKLINE>
#         <BLANKLINE>

#         >>> cache.clear()
#         'Cache cleared!'
#         >>> contentA = ContentItem(2000, 52, 'Content-Type: 2', 'GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1')
#         >>> contentB = ContentItem(2001, 76, 'Content-Type: 2', 'GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1')
#         >>> contentC = ContentItem(2002, 11, 'Content-Type: 2', 'GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1')
#         >>> cache.insert(contentA, 'lru')
#         'INSERTED: CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1'
#         >>> cache.insert(contentB, 'lru')
#         'INSERTED: CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1'
#         >>> cache.insert(contentC, 'lru')
#         'INSERTED: CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1'
#         >>> cache.hierarchy[2]
#         REMAINING SPACE:61
#         ITEMS:3
#         LIST:
#         [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
#         [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
#         [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
#         <BLANKLINE>
#         >>> cache.retrieveContent(contentC)
#         CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1
#         >>> cache.hierarchy[2]
#         REMAINING SPACE:61
#         ITEMS:3
#         LIST:
#         [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
#         [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
#         [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
#         <BLANKLINE>
#         >>> cache.retrieveContent(contentA)
#         CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1
#         >>> cache.hierarchy[2]
#         REMAINING SPACE:61
#         ITEMS:3
#         LIST:
#         [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
#         [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
#         [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
#         <BLANKLINE>
#         >>> cache.retrieveContent(contentC)
#         CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1
#         >>> cache.hierarchy[2]
#         REMAINING SPACE:61
#         ITEMS:3
#         LIST:
#         [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
#         [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201802040nwe.htm HTTP/1.1]
#         [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
#         <BLANKLINE>
#         >>> contentD = ContentItem(2002, 11, 'Content-Type: 2', 'GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1')
#         >>> cache.insert(contentD, 'lru')
#         'Insertion of content item 2002 not allowed. Content already in cache.'
#         >>> contentE = ContentItem(2000, 52, 'Content-Type: 2', 'GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1')
#         >>> cache.updateContent(contentE)
#         'UPDATED: CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1'
#         >>> cache.hierarchy[2]
#         REMAINING SPACE:61
#         ITEMS:3
#         LIST:
#         [CONTENT ID: 2000 SIZE: 52 HEADER: Content-Type: 2 CONTENT: GET https://www.pro-football-reference.com/boxscores/201801210phi.htm HTTP/1.1]
#         [CONTENT ID: 2002 SIZE: 11 HEADER: Content-Type: 2 CONTENT: GET https://media.giphy.com/media/YN7akkfUNQvT1zEBhO/giphy-downsized.gif HTTP/1.1]
#         [CONTENT ID: 2001 SIZE: 76 HEADER: Content-Type: 2 CONTENT: GET https://giphy.com/gifs/93lCI4D0murAszeyA6/html5 HTTP/1.1]
#         <BLANKLINE>        
#     '''

#     def __init__(self):
#         self.hierarchy = [CacheList(200), CacheList(200), CacheList(200)]
#         self.size = 3
    
#     def __str__(self):
#         return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
#     __repr__=__str__


#     def clear(self):
#         for item in self.hierarchy:
#             item.clear()
#         return 'Cache cleared!'

    
#     def insert(self, content, evictionPolicy):
#         # YOUR CODE STARTS HERE
#         pass


#     def retrieveContent(self, content):
#         # YOUR CODE STARTS HERE
#         pass


#     def updateContent(self, content):
#         # YOUR CODE STARTS HERE
#         pass        