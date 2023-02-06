import os

os.system('cls')

print()
# Write your code here:

N = int(input())

ls = []    
    
for inputs in range(N):
        
    line = input()
        
    line_lwrcase = line.lower()   
      
    order = line_lwrcase.split()
             
    if order[0] == 'insert' :
        
        ls.insert( int(order[1]), int(order[2]) )
        #print(ls)
    
    elif order[0] == 'print' :
        
        print(ls)
        
    elif order[0] == 'remove' :
        
        ls.remove( int(order[1]) )
        #print(ls)
    
    elif order[0] == 'sort' :
        
        ls.sort()
        #print(ls)
    
    
    elif order[0] == 'append' :
        
        ls.append( int(order[1]) )
        #print(ls)
    
    elif order[0] == 'pop' :
        
        ls.pop( )
        #print(ls)
         
    elif order[0] == 'reverse' :
        
        ls.reverse()
        #print(ls)
       
    else:
        print('This order not found on the program')  
        
     

# The end of your code. 
print(), print()
