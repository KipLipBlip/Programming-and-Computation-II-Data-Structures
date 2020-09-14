# LAB2
#Due Date: 09/18/2020, 11:59PM
"""                                   
### Collaboration Statement:
             
"""

## Section 1
class VendingMachine:
    '''
        >>> x=VendingMachine()
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.restock(215, 9)
        'Invalid item'
        >>> x.isStocked
        True
        >>> x.restock(156, 1)
        'Current item stock: 4'
        >>> x.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Please deposit $1.5'
        >>> x.purchase(156,2)
        'Please deposit $3.0'
        >>> x.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> x.deposit(3)
        'Balance: $3'
        >>> x.purchase(156,3)
        'Please deposit $1.5'
        >>> x.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.deposit(300)
        'Balance: $300'
        >>> x.purchase(876)
        'Invalid item'
        >>> x.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> x.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> x.purchase(156,3)
        'Please deposit $4.5'
        >>> x.deposit(4.5)
        'Balance: $4.5'
        >>> x.purchase(156,3)
        'Item dispensed'
        >>> x.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Item out of stock'
        >>> x.deposit(6)
        'Balance: $6'
        >>> x.purchase(254,3)
        'Item dispensed'
        >>> x.deposit(9)
        'Balance: $9'
        >>> x.purchase(879,3)
        'Item dispensed'
        >>> x.isStocked
        False
        >>> x.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> x.purchase(156,2)
        'Machine out of stock'
        >>> y=VendingMachine()
        >>> x.setPrice(156, 2.5)
        >>> x.getStock
        {156: [2.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> y.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        pass



    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        pass
        


    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        pass


    def restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        pass


    #--- YOUR CODE STARTS HERE
   
    def isStocked(self):
        pass
        

    #--- YOUR CODE STARTS HERE

    def getStock(self):
        pass


    def setPrice(self, item, new_price):
        #--- YOUR CODE STARTS HERE
        pass
       




## Section 2
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ## * YOU MAY IMPLEMENT SPECIAL METHODS TO SIMPLIFY LINE METHODS


        

class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        pass



    #--- YOUR CODE STARTS HERE
    def getDistance(self):
        pass
        
    #--- YOUR CODE STARTS HERE
    def getSlope(self):
        pass


    #--- YOUR CODE CONTINUES HERE
