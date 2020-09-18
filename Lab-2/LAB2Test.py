import unittest
from LAB2 import *

class VendingMachineTestCases(unittest.TestCase):

    def test_init(self):
        ''' Correctly initializing values '''

        s = { 156 : [1.5, 3], 254 : [2.0, 3], 384 : [2.5, 3], 879 : [3.0, 3]}
        x = VendingMachine()

        self.assertEqual(x.balance, 0, 'Failed balance init')
        self.assertEqual(x.stock, s, 'Failed stock init')

    def test_getStock(self):
        ''' Correctly retrieving stock '''

        s = { 156 : [1.5, 3], 254 : [2.0, 3], 384 : [2.5, 3], 879 : [3.0, 3]}
        x = VendingMachine()

        self.assertEqual( x.getStock, s, 'Failed getStock check' )

    def test_restock(self):
        ''' Correctly restocking items / rejecting invalid items '''
        x = VendingMachine()

        self.assertEqual( x.restock(215, 9), 'Invalid item', 'Failed invalid restock item' )
        self.assertEqual( x.restock(156, 1), 'Current item stock: 4', 'Failed 156 restock')

        s = {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        self.assertEqual( x.getStock, s, 'Failed to get stock after restock')
        
    def test_isStocked(self):
        x = VendingMachine()

        self.assertEqual(x.isStocked, True, 'Failed stocked test')

    def test_session(self):

        '>>> x=VendingMachine()'
        x = VendingMachine()

        # Variable
        stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        '>>> x.getStock'
        '{156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}'
        self.assertEqual( x.getStock, stock, '1. Failed to get stock' )

        '>>> x.restock(215, 9)'
        'Invalid item'
        self.assertEqual( x.restock(215,9), 'Invalid item', '2. Failed to restock invalid item')

        '>>> x.isStocked'
        'True'
        self.assertEqual( x.isStocked, True, '3. Failed isStocked bool test')

        '>>> x.restock(156, 1)'
        'Current item stock: 4'
        self.assertEqual( x.restock(156, 1), 'Current item stock: 4', '4. Failed 156 restock' )

        # Variable
        stock = {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        '>>> x.getStock'
        '{156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}'
        self.assertEqual( x.getStock, stock, '5. Failed to get stock after 156 restock' )

        '>>> x.purchase(156)'
        'Please deposit $1.5'
        self.assertEqual( x.purchase(156), 'Please deposit $1.5', '6. Failed purchase attempt with 0 balance')

        '>>> x.purchase(156,2)'
        'Please deposit $3.0'
        self.assertEqual( x.purchase(156, 2), 'Please deposit $3.0', '7. Failed purchase attempt with 0 balance')

        '>>> x.purchase(156,23)'
        'Current 156 stock: 4, try again'
        self.assertEqual( x.purchase(156, 23), 'Current 156 stock: 4, try again', '8. Failed purchase more than stock')

        '>>> x.deposit(3)'
        'Balance: $3'
        self.assertEqual( x.deposit(3), 'Balance: $3', '9. Failed to deposit $3' )

        '>>> x.purchase(156,3)'
        'Please deposit $1.5'
        self.assertEqual( x.purchase(156, 3), 'Please deposit $1.5', '10. Failed to purchase item w/o enough balance, nonzero balance')

        '>>> x.purchase(156)'
        'Item dispensed, take your $1.5 back'
        self.assertEqual( x.purchase(156), 'Item dispensed, take your $1.5 back', '11. Failed to purchase item and dispense money')

        # Variable
        stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        '>>> x.getStock'
        '{156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}'
        self.assertEqual( x.getStock, stock, '12. Failed to get stock after purchase' )

        '>>> x.deposit(300)'
        'Balance: $300'
        self.assertEqual( x.deposit(300), 'Balance: $300', '13. Failed to deposit $300')

        '>>> x.purchase(876)'
        'Invalid item'
        self.assertEqual( x.purchase(876), 'Invalid item', '14. Failed purchase invalid item')

        '>>> x.purchase(384,3)'
        'Item dispensed, take your $292.5 back'
        self.assertEqual( x.purchase(384, 3), 'Item dispensed, take your $292.5 back', '15. Failed purchase 384 and give change')

        '>>> x.purchase(156,10)'
        'Current 156 stock: 3, try again'
        self.assertEqual( x.purchase(156, 10), 'Current 156 stock: 3, try again', '16. Failed to purchase w/ invalid stock')

        '>>> x.purchase(156,3)'
        'Please deposit $4.5'
        self.assertEqual( x.purchase(156, 3), 'Please deposit $4.5', '17. Failed to purchase w/ no balance')

        '>>> x.deposit(4.5)'
        'Balance: $4.5'
        self.assertEqual( x.deposit(4.5), 'Balance: $4.5', '18. Failed to deposit $4.5' )

        '>>> x.purchase(156,3)'
        'Item dispensed'
        self.assertEqual( x.purchase(156, 3), 'Item dispensed', '19. Cleared stock on 156')

        # Variable
        stock = {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}

        '>>> x.getStock'
        '{156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}'
        self.assertEqual( x.getStock, stock, '20. Failed to get stock after purchase' )

        '>>> x.purchase(156)'
        'Item out of stock'
        self.assertEqual( x.purchase(156), 'Item out of stock', '21. Failed to purchase out of stock item')

        '>>> x.deposit(6)'
        'Balance: $6'
        self.assertEqual( x.deposit(6), 'Balance: $6', '22. Failed to deposit $6')

        '>>> x.purchase(254,3)'
        'Item dispensed'
        self.assertEqual( x.purchase(254, 3), 'Item dispensed', '23. Failed to purchase 254')

        '>>> x.deposit(9)'
        'Balance: $9'
        self.assertEqual( x.deposit(9), 'Balance: $9', '24. Failed to deposit $9')

        '>>> x.purchase(879,3)'
        'Item dispensed'
        self.assertEqual( x.purchase(879, 3), 'Item dispensed', '25. Failed to purchase 879')

        '>>> x.isStocked'
        'False'
        self.assertEqual( x.isStocked, False, '26. Failed isStocked test')

        '>>> x.deposit(5)'
        'Machine out of stock. Take your $5 back'
        self.assertEqual( x.deposit(5), 'Machine out of stock. Take your $5 back', '27. Machine out of stock deposit')

        '>>> x.purchase(156,2)'
        'Machine out of stock'
        self.assertEqual( x.purchase(156, 2), 'Machine out of stock', '28. Machine out of stock purchase')

        '>>> y=VendingMachine()'
        y = VendingMachine()

        '>>> x.setPrice(156, 2.5)'
        self.assertIsNone( x.setPrice(156, 2.5), '1.1. Failed to set price of x156' )

        # Variable
        stock = {156: [2.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}

        '>>> x.getStock'
        '{156: [2.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}'
        self.assertEqual( x.getStock, stock, '2.1. Failed to get stock after price change' )

        # Variable
        stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        '>>> y.getStock'
        '{156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}'
        self.assertEqual( y.getStock, stock, '3.1. Failed to get stock for new object' )

class LineAndPointTestCases(unittest.TestCase):

    def test_Point2D(self):
        ''' Point 2D Test Cases'''

        z = Point2D(-7,-9)

        self.assertEqual( z.x, -7, 'Failed to set x')
        self.assertEqual( z.y, -9, 'Failed to set y')

        z = Point2D(1, 5.6)

        self.assertEqual( z.x, 1, 'Failed to set x')
        self.assertEqual( z.y, 5.6, 'Failed to set y')

    def test_Line(self):

        '>>> p1 = Point2D(-7, -9)'
        '>>> p2 = Point2D(1, 5.6)'
        '>>> line1 = Line(p1, p2)'
        line1 = Line( Point2D(-7,-9), Point2D(1, 5.6) )

        '>>> line1.getDistance'
        '16.648'
        self.assertEqual( line1.getDistance, 16.648, 'Failed to get distance: line1')

        '>>> line1.getSlope'
        '1.825'
        self.assertEqual( line1.getSlope, 1.825, 'Failed to get slope: line1')

        '>>> line1'
        'y = 1.825x + 3.775'
        self.assertEqual( str(line1), 'y = 1.825x + 3.775', 'Failed to get Equation: line1' )

        '>>> line2 = line1*4'
        line2 = line1*4

        '>>> line2.getDistance'
        '66.592'
        self.assertEqual( line2.getDistance, 66.592, 'Failed to get distance: line2')

        '>>> line2.getSlope'
        '1.825'
        self.assertEqual( line2.getSlope, 1.825, 'Failed to get slope: line2')

        '>>> line2'
        'y = 1.825x + 15.1'
        self.assertEqual( str(line2), 'y = 1.825x + 15.1', 'Failed to get equation: line2')

        '>>> line1'
        'y = 1.825x + 3.775'
        self.assertEqual( str(line1), 'y = 1.825x + 3.775', 'Failed to get Equation: line1' )

        '>>> line3 = 4*line1'
        line3 = 4*line1

        '>>> line3'
        'y = 1.825x + 15.1'
        self.assertEqual( str(line1), 'y = 1.825x + 3.775', 'Failed to get Equation: line1' )

        '>>> line1==line2'
        'False'
        self.assertEqual( line1 == line3, False, 'Failed line comparison 1&3')

        '>>> line3==line2'
        'True'
        self.assertEqual( line2 == line3, True, 'Failed line comparison 2&3')

        '>>> line5=Line(Point2D(6,48),Point2D(9,21))'
        line5 = Line( Point2D(6,48), Point2D(9,21) )

        '>>> line5'
        'y = -9.0x + 102.0'
        self.assertEqual( str(line5), 'y = -9.0x + 102.0', 'Failed to get Equation: line5' )

        '>>> line5==9'
        'False'
        self.assertEqual( line5 == 9, False, 'Failed false comparison: line5')

        '>>> line6=Line(Point2D(2,6), Point2D(2,3))'
        line6 = Line( Point2D(2,6), Point2D(2,3) )

        '>>> line6.getDistance'
        '3.0'
        self.assertEqual( line6.getDistance, 3.0, 'Failed to get distance: line6')

        '>>> line6.getSlope'
        'inf'
        self.assertEqual( line6.getSlope, 'inf', 'Failed to get inf slope: line6')

        '>>> line6'
        'Undefined'
        self.assertEqual( str(line6), 'Undefined', 'Failed to return an undef line: line6')

        '>>> line7=Line(Point2D(6,5), Point2D(9,5))'
        line7 = Line( Point2D(6,5), Point2D(9,5) )

        '>>> line7.getSlope'
        '0.0'
        self.assertEqual( line7.getSlope, 0.0, 'Failed to get inf slope: line6')

        '>>> line7'
        'y = 5.0'
        self.assertEqual( str(line7), 'y = 5.0', 'Failed to get equation: line7')

    def test_piazzaCases(self):
        '>>> x = Line(Point2D(5.65, -7.65), Point2D(-9, 45.3))'
        x = Line(Point2D(5.65, -7.65), Point2D(-9, 45.3))

        '>>> x.getDistance'
        '54.939'
        self.assertEqual( x.getDistance, 54.939, 'Failed x.getDistance')

        '>>> x.getSlope'
        '-3.614'
        self.assertEqual( x.getSlope, -3.614, 'Failed x.getSlope')

        '>>> x'
        'y = -3.614x + 12.769'
        self.assertEqual( str(x), 'y = -3.614x + 12.769', 'Failed x equation')

        '>>> x==[1,2,3]'
        'False'
        self.assertEqual( x==[1,2,3], False, 'Failed x __eq__')

        '>>> y=56*x'
        y=56*x
        
        '>>> y'
        'y = -3.614x + 715.07'
        self.assertEqual( str(y), 'y = -3.614x + 715.07', 'Failed to class vs variable')

        '>>> x = Line(Point2D(99, -7.65), Point2D(99, 45.3))'
        x = Line(Point2D(99, -7.65), Point2D(99, 45.3))

        '>>> x'
        'Undefined'
        self.assertEqual( str(x), 'Undefined', 'Failed undefined line')

        '>>> x = Line(Point2D(99, -7.65), Point2D(-99, 7.65))'
        x = Line(Point2D(99, -7.65), Point2D(-99, 7.65))

        '>>> x'
        'y = -0.077x - 0.027'
        self.assertEqual( str(x), 'y = -0.077x - 0.027', 'Failed to get x equation')

        '>>> x = Line(Point2D(99, -7.65), Point2D(-99, -7.65))'
        x = Line(Point2D(99, -7.65), Point2D(-99, -7.65))

        '>>> x'
        'y = - 7.65'
        self.assertEqual( str(x), 'y = - 7.65', 'Failed to get x equation')

if __name__ == '__main__':
	unittest.main(exit=False)
