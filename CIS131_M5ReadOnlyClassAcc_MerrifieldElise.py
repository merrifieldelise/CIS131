'''
Script: Account Class with Read-Only Properties
Action: Modify 'account' class to read only for name and balance, test
Author: Elise Merrifield
Date: 02/23/2026
'''
#import decimal
from decimal import Decimal

#set up class
class Account:
    '''Account class for bank account balance.'''

    def __init__(self, name, balance):
        '''initialize an account object'''

        #If balance is less than 0.00, raise and exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        '''Deposit money into account.'''
        #raise an exception if amount less than 0.00
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        self._balance += amount


#test class account for read only
account1 = Account('John Green', Decimal('50.00'))
print(account1._balance)
account1.balance = Decimal('25.00')
print(account1._balance)
print(account1._name)
account1.name = "Pam"
print(account1._name)

account1.deposit(Decimal('30'))
print(account1._balance)