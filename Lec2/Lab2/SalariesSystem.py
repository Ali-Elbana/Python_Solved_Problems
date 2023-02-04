import os

os.system('cls')

print()
# Write your code here:


# Is a database for the employee s names and salaries:
employees_names = [ 'Ahmed', 'Ali', 'Amr' ]

employees_salaries = [ 2000, 3000, 4000 ] 
 
# Get the employee name from the employee :
employee_name = str( input( "Please enter the employee's name: " ) )

if employee_name not in employees_names :
        
    print( 'Incorrect employee name' ) 
    
else :
     
    print( f"The employee salary is { employees_salaries[employees_names.index( employee_name )] }$" )


# The end of your code. 
print(), print()
