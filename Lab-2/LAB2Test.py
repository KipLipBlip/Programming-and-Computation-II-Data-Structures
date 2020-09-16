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
        
    '''
        >>> x.isStocked
        True
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

if __name__ == '__main__':
	unittest.main(exit=False)
