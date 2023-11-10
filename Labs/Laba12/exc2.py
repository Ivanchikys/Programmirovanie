#accountNumber (random) 1
#balance 1
#accountType 1
#Metod - deposit
#Metod - read 

#balance - ekz 1 
#Metod - снять со счета
#Metod - положить на счет

#Metod снять - возможно ли? если можно change balance
import random

class BankAccount:
    def __init__(self, balance = 0, accountType = 'debit'):
        self.balance = balance
        self.accountType = accountType
        self.accountNumber = ''.join([random.choice('0123456789') for _ in range(17)])

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Недостаточно средств')

    def getBalance(self):
        return self.balance
    
    def printAccountInfo(self):
        print('Номер счета: ', self.accountNumber)
        print('Баланс: ', self.balance)
        print('Тип счета: ', self.accountType)


account = BankAccount(balance = 50)        #Баланс по умолч.
account.printAccountInfo()

account.withdraw(10)                    #Снять
print(account.getBalance())

account.deposit(50)                   #Пополнить
print(account.getBalance())