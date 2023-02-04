import os

os.system('cls')

print()
# Write your code here:


class Bank_Account :
    """This class is a base class for bank accounts
    that is created by passing name and balance"""
    def __init__( self, name, balance ):
        """ to initialize basic info"""
        self.name       = name
        self.balance    = balance
        self.__id       = '30008011328372' 
        
    def deposite(self, amount):
        
        if amount > 0 :
            self.balance += amount
        else:
            raise ValueError( 'You should deposite with a positive amount' )
    
    def withdraw( self, amount ):
        
        if amount <= self.balance :
            self.balance -= amount
        else:
            raise ValueError( 'The Account doesn\'t have this amount of money' )
    
    def __repr__(self) -> str:
        return f'{self.name} currently has {self.balance} in his account'

    def __add__( self, other ):
        return f'{self.name} and {other.name} both have a total of ', self.balance + other.balance


acc1 = Bank_Account('Ali', 2000_000)

print( acc1.name, acc1.balance )

acc1.withdraw( 2000_000 )

print( acc1.balance )

acc1.deposite( 2000_000 )

print( acc1.balance )

acc2 = Bank_Account('Amr', 3000_000)

acc2._Bank_Account__id = '20008011328372'

print( acc2._Bank_Account__id )

print( acc1 + acc2 )

# The end of your code. 
print(), print()

