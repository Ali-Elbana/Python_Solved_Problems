import os

os.system('cls')

print()
# Write your code here:


class Capt_str :
    
    def __init__( self, your_str ):
        
        self.lenght     = len( your_str )
        self.captlize
        self.your_str   = your_str

    def captlize( self ):
        
        my_str = self.your_str
        
        my_str_ls = []
        
        for letter in my_str :
            
            if 97 <= ord(letter) <= 122:
                my_str_ls.append( chr( ord(letter) - 32 ) )
            else:
                my_str_ls.append(letter)

        return ''.join(my_str_ls)


name = Capt_str('ali adel')

print( name.captlize() )


# The end of your code. 
print(), print()

