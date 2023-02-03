import os

os.system('cls')

print()
# Write your code here:
 
input_str = input( "Please enter the sentence: " )

char_list = list( input_str )

char_list.reverse()

print( "The sentence after mirroring is", end = ' ' )  
  
for chars in char_list :
    
    print( chars, end = '' )
    
# The end of your code. 
print(), print()


'''
Another solution:

input_str = input( "Please enter the sentence: " )

rev_str = ''

for char in input_str :

    rev_str = char + rev_str

print( f"The sentence after mirroring is { rev_str }" )

'''