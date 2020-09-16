from logging import setLoggerClass
import unittest
from LAB2 import VendingMachine

class VendingMachineTestCases(unittest.TestCase):
    ''' Tests various cases for VendingMachine in Lab 2 '''

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

        self.assertEqual( x.getStock(), s, 'Failed getStock check' )

    def test_restock(self):
        ''' Correctly restocking items / rejecting invalid items '''
        x = VendingMachine()

        self.assertEqual( x.restock(215, 9), 'Invalid item', 'Failed invalid restock item' )
        self.assertEqual( x.restock(156, 1), 'Current item stock: 4', 'Failed 156 restock')

        s = {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        self.assertEqual( x.getStock(), s, 'Failed to get stock after restock')
        
    def test_isStocked(self):
        x = VendingMachine()

        self.assertEqual(x.isStocked(), True, 'Failed stocked test')

    def test_session(self):
        ''' Contains everything in the docstring '''

        x = VendingMachine()
        stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        self.assertEqual( x.getStock(), stock, '1. Failed to get stock' )

        self.assertEqual( x.restock(215,9), 'Invalid item', '2. Failed to restock invalid item')

        self.assertEqual( x.isStocked(), True, '3. Failed isStocked bool test')

        self.assertEqual( x.restock(156, 1), 'Current item stock: 4', '4. Failed 156 restock' )

        stock = {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        self.assertEqual( x.getStock(), stock, '5. Failed to get stock after 156 restock' )

        self.assertEqual( x.purchase(156), 'Please deposit $1.5', '6. Failed purchase attempt with 0 balance')

        self.assertEqual( x.purchase(156, 2), 'Please deposit $3.0', '7. Failed purchase attempt with 0 balance')

        self.assertEqual( x.purchase(156, 23), 'Current 156 stock: 4, try again', '8. Failed purchase more than stock')

        self.assertEqual( x.deposit(3), 'Balance: $3', '9. Failed to deposit $3' )

        self.assertEqual( x.purchase(156, 3), 'Please deposit $1.5', '10. Failed to purchase item w/o enough balance, nonzero balance')

        self.assertEqual( x.purchase(156), 'Item dispensed, take your $1.5 back', '11. Failed to purchase item and dispense money')

        stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}

        self.assertEqual( x.getStock(), stock, '12. Failed to get stock after purchase' )

        self.assertEqual( x.deposit(300), 'Balance: $300', '13. Failed to deposit $300')

        self.assertEqual( x.purchase(876), 'Invalid item', '14. Failed purchase invalid item')

        self.assertEqual( x.purchase(384, 3), 'Item dispensed, take your $292.5 back', '15. Failed purchase 384 and give change')


'''             
        >>> x.purchase(384,3)
        
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

if __name__ == '__main__':
	unittest.main(exit=False)
