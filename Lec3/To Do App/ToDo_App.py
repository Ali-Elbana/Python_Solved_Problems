import os
import todo_mod as TD

def main():
    
    # Clear the terminal screen:
    os.system('cls')
    
    # The available choices numbers:
    add_task        = 1
    print_todo      = 2
    task_done       = 3
    print_done      = 4
    exit_todo       = 5
    entered_choice  = None
    
    while( entered_choice != exit_todo ) :
        
        TD.print_menu()
        
        entered_choice = int( TD.get_choice() )
        
        if entered_choice == add_task :
            
            TD.add_task()
    
        elif entered_choice == print_todo :
                
            TD.print_ToDoList()
                
        elif entered_choice == task_done :
                
            TD.task_done()
                  
        elif entered_choice == print_done :
                
            TD.print_DoneList()
           
if __name__ == '__main__' :

    print()
    # Write your code here:
        
    main()

    # The end of your code. 
    print(), print()


