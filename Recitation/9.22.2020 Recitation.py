'''
    09/22 Recitation Activity 

    Implement the Keyboard class that takes in a sequence of Buttons in a 
    Python list and stores these Buttons in a dictionary where the keys 
    will be integers that represent the position
 	on the Keyboard, and the values will be the respective Button objects. 
	Complete each method according to its description. 
	Use the doctest as a reference for the behavior of a Keyboard object
'''

class Button:
    '''
        A Button takes an integer and a string that represents a character in a keyboard
        >>> x = Button(3, 'A')
        >>> y = Button(8, 't')
        >>> x
        A
        >>> print(x)
        Button A at position 3
        >>> y*3
        'ttt'
    '''

    def __init__(self, position, button):

        self.position = position
        self.key = button

    def __repr__(self): 
        return str(self.button)

    def __str__(self):
        return 'Button {} at position {}'.format(self.button, self.position)

    def __mul__(self, other):
        return self.button * other

    __rmul__ = __mul__

    @property
    def pressed(self):
        return self.position

class Keyboard:
    """
        >>> b1 = Button(0, "H")
        >>> b2 = Button(1, "i")
        >>> b3 = Button(3, "m")
        >>> b4 = Button(4, "o")
        >>> b5 = Button(5, " ")
        >>> k = Keyboard([b1, b2, b3, b4, b5])
        >>> k.buttons[0].key
        'H'
        >>> k.press(1)
        'i'
        >>> k._type([0, 1])
        'Hi'
        >>> k._type([1, 0])
        'iH'
        >>> k._type([0, 1, 5, 3, 4, 3])
        'Hi mom'
        >>> b1.pressed
        3
        >>> b2.pressed
        4
    """

    def __init__(self, button_list):
        
        self.buttons = {}
        for i in button_list:
            self.buttons[i.key] = i
        
    def press(self, info):
        """ 
            Parameters:
                info: position of the button pressed
            Returns:
                Button's output
        """

        return self.buttons[info]


    def _type(self, typing):
        """ 
            Parameters:
              typing: list of positions of buttons pressed
            Returns:
               Total output
        """
        # YOUR CODE STARTS HERE 
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()