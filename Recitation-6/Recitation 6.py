def hash(key):
    ''' return the index of the key in the hash table'''

    asciiKey = 1
    for character in key:
        asciiKey *= ord(character)
    return asciiKey % self.size
    
