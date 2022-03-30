'''
Created on Jun 22, 2017

@author: SummitWorks
'''
class Account(object):
    def __init__(self, holder, number, balance,credit_line=1500): 
        self.Holder = holder 
        self.Number = number 
        self.Balance = balance
        self.CreditLine = credit_line

    def deposit(self, amount): 
        
        self.Balance= self.Balance + amount

    def withdraw(self, amount): 
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            return True

    def balance(self): 
        return self.Balance

    def transfer(self, target, amount):
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            target.Balance=target.Balance+amount
            
            
a1=Account("Maruthi",123,1000)
a2=Account("Hein Long",567,1200)
a1.deposit(200)
print(a1.Balance)
a1.withdraw(100)
print(a1.Balance)

a1.transfer(a2, 400)
print(a1.Balance)
print(a2.Balance)