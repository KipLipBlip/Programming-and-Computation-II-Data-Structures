# 09/29/2020: Module 3 Review Session

import datetime
import random

class Person:
    def __init__(self, name, birthdate,ssn):
        self.name = name
        self.birthdate = birthdate
        self.__ssn=ssn


    @property   
    def getSSN(self):
        return self.__ssn

    def setID(self, new_ssn):
        self.__ssn=new_ssn
        return self.__ssn

    @property
    def age(self):
        month, day, year = self.birthdate.split("/")
        today = datetime.date.today()
        age = today.year - int(year)
        if today < datetime.date(today.year, int(month), int(day)):
            age -= 1

        return age

class Account:

    INTEREST = 0

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
        self.__id = self.__createID()

    def __createID(self):
        # Account id
        return random.randint(10000, 99999)

    @property   
    def getID(self):
        return self.__id

    def setID(self, new_id):
        self.__id=new_id
        return self.__id

    def deposit(self, amount):
        if isinstance(amount, Check):
            if not amount.cashed and amount.payTo == self.holdername:
                self.balance += amount.checkAmount
                amount.cashed = True
                return self.balance
            else:
                return 'Invalid operation'
        elif isinstance(amount, (int, float)):
            self.balance = self.balance + amount
            return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Not enough funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):

    WITHDRAW_FEE = 1
    INTEREST = 0.01
 
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder)
        self.balance = balance

    def withdraw(self, amount):
        return Account.withdraw(self, amount + CheckingAccount.WITHDRAW_FEE)


class SavingsAccount(Account):

    DEPOSIT_FEE = 1
    WITHDRAW_FEE = 2
    INTEREST = 0.03
    CASH_REWARD = 100
    MIN_BALANCE = 250
    
    def __init__(self,account_holder, balance):
        super().__init__(account_holder)
        if self.balance < 500:
            return 'Not enough funds'
        self.balance = balance + SavingsAccount.CASH_REWARD

    def deposit(self, amount):
        return Account.deposit(self, amount + SavingsAccount.DEPOSIT_FEE)

    def withdraw(self, amount):
        if amount + SavingsAccount.WITHDRAW_FEE > self.balance - SavingsAccount.MIN_BALANCE:
            return 'Not enough funds'
        return Account.withdraw(self, amount + SavingsAccount.WITHDRAW_FEE)


class Check(Account):

    def __init__(self, account_holder, amount, payTo):
        super().__init__(account_holder)
        self.checkAmount = amount
        self.payTo = payTo
        self.cashed = False
        self.fee = 0

    def __str__(self):
        return f'Pay to {self.payTo}: ${self.amount + self.fee}'

    def __repr__(self):
        return f'Cashed: {self.cashed}'

class Bank:
    def __init__(self):
        """Creates an instance of Bank with no accounts"""
        self.accounts = []

    def openAccount(self, holder, amount, account_type=Account):
        """Open an account_type for holder and deposit amount."""
        account = account_type(holder, amount)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def payInterest(self):
        """Pay interest to all accounts."""
        for account in self.accounts:
            account.deposit(account.balance * account.INTEREST)