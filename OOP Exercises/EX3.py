import os

os.system('cls')

print()
# Write your code here:


class Dog :
    
    def __init__( self, name, age ):
        
        self.name   = name
        self.age    = age

    def bark(self):
        print('Haw Haw Haw')

    def set_age( self, age ):
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name( self, name : str ):
        
        if not name.isalpha():
            raise ValueError( 'Name must be alphabetical only' )
        
        self._name = name

    @name.deleter
    def del_name( self ):
        self._name = None



dog1 = Dog('simba', 2)

dog1.name = 'Rex'

print( dog1.name, dog1.age )



# The end of your code. 
print(), print()

