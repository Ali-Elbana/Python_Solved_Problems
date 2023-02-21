import os
import emp_mod as EMP

def main():
    
    # Clear the terminal screen:
    os.system('cls')
    
    # The available choices numbers:
    add_emp         = 1
    print_EmpData   = 2
    del_emp         = 3
    exit_todo       = 4
    entered_choice  = None
    
    while( entered_choice != exit_todo ) :
        
        EMP.print_menu()
        
        entered_choice = int( EMP.get_choice() )
        
        if entered_choice == add_emp :
            
            EMP.add_emp()
    
        elif entered_choice == print_EmpData :
                
            EMP.print_EmpData()
                
        elif entered_choice == del_emp :
                
            EMP.delete_emp()
                  
if __name__ == '__main__' :

    print()
    # Write your code here:
        
    main()

    # The end of your code. 
    print(), print()


