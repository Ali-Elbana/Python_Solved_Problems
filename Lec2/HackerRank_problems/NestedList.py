import os

os.system('cls')

print(), print()
# Write your code here:

if __name__ == '__main__':
    
    ls = [  ]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        std_grades = [ name, score ]
        
        ls.append( std_grades )
        
    gardes_ls = []

    for grade in ls:
        
        gardes_ls.append( grade[1] )  
        
    gardes_set = set( gardes_ls )      
        
    min_garde = min(gardes_set)     
        
    gardes_set.remove( min_garde )    
        
    min_garde2 = min(gardes_set)       
            
    students = []   
        
    for grade in ls:
        
        if grade[1] == min_garde2 :
            
            students.append( grade[0] )     

    students.sort() 

    for names in students :
        
        print(names) 
            
        
# The end of your code. 
print(), print()





