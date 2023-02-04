import os

os.system('cls')

print()
# Write your code here:


class Dog :
    
    def __init__( self, dog_name, dog_age ):
        
        self.name   = dog_name
        self.age    = dog_age

    def bark(self):
        print('Haw Haw Haw')

    def set_age( self, dog_age ):
        self.age = dog_age


dog1 = Dog('simba', 2)

dog1.name = 'Max'

dog1.set_age( 5 )

print( dog1.name, dog1.age )



# The end of your code. 
print(), print()

