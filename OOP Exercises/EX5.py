import os

os.system('cls')

print()
# Write your code here:


class Employee :
    
    def __init__( self, fname, lname ):
        
        self.fname   = fname
        self.lname   = lname
        self.email   = f'{fname}.{lname}@gmail.com'
           
emp1 = Employee( "Ali", "Adel" )       

print( emp1.email )

# inheritance:
class Teacher(Employee):
    
    def __init__(self, fname, lname):
        
        super().__init__(fname, lname)
        self.email   = f'{fname}.{lname}-t@gmail.com'
        
        
tcr1 =  Teacher( 'Hany', 'Mongy' )

print( tcr1.email )


# The end of your code. 
print(), print()

