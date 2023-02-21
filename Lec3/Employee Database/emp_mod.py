
emp_database = { }

def print_menu():
    
    print()
    print( "1-Add new employee." )
    print( "2-Print employee data." )
    print( "3-Delete employee." )
    print( "4-Exit." )

def get_choice():
    
    choice = int( input( "\nPlease enter your choice: " ) )
   
    if choice != 1 and choice != 2 and choice != 3 and choice != 4 :
        
        print( "Please enter the number of the available choices." )
   
    return choice

def add_emp():
    
    global emp_database
    
    add_again : str = None
    
    while( add_again != 'N' and add_again != 'n' ) :
        
        new_emp_id      = int( input( "\nPlease enter the new employee ID: " ) )
        
        new_emp_name    = str( input( "\nPlease enter the new employee name: " ) )
        
        new_emp_job     = str( input( "\nPlease enter the new employee job: " ) )
        
        new_emp_salary  = int( input( "\nPlease enter the new employee salary: " ) )
        
        emp_database[new_emp_id] = [ new_emp_name, new_emp_job, new_emp_salary ]
        
        add_again = str( input( "Add another employee ? [Y/N] ? " ) )
        
        if add_again != 'y' and add_again != 'Y' and add_again != 'n' and add_again != 'N' :
            
            print( "Not from the available choices." )
        
def print_EmpData():
    
    print()
    
    global emp_database
    
    print_again : str = None
    
    while( print_again != 'N' and print_again != 'n' ) :
        
        entered_id = int( input( "\nPlease enter employee ID: " ) )
    
        if entered_id not in emp_database.keys() :
            
            print( "The entered ID not found in the database." )
        
        print( f"\n The employee name is    {emp_database[entered_id][0]}" )
        print( f"\n The employee job is     {emp_database[entered_id][1]}" )
        print( f"\n The employee salary is  {emp_database[entered_id][2]}" )
    
        print_again = str( input( "Print another employee data ? [Y/N] ? " ) )
        
        if print_again != 'y' and print_again != 'Y' and print_again != 'n' and print_again != 'N' :
            
            print( "Not from the available choices." )
    
    
def delete_emp():
    
    print()
    
    global emp_database

    del_again : str = None
    
    while( del_again != 'N' and del_again != 'n' ) :
        
        entered_id = int( input( "\nPlease enter employee ID: " ) )
    
        if entered_id not in emp_database.keys() :
            
            print( "The entered ID not found in the database." )
        
        emp_database.pop( entered_id )  

        del_again = str( input( "Delete another employee ? [Y/N] ? " ) )
        
        if del_again != 'y' and del_again != 'Y' and del_again != 'n' and del_again != 'N' :
            
            print( "Not from the available choices." )
    


































































