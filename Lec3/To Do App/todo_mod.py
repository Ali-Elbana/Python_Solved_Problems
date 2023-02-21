
ToDoList = [ ]

DoneList = [ ]

def print_menu():
    
    print()
    print( "1-Add new task." )
    print( "2-Print the To Do list." )
    print( "3-Mark a task as done." )
    print( "4-Print the done list." )
    print( "5-Exit." )

def get_choice():
    
    choice = int( input( "\nPlease enter your choice: " ) )
   
    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        
        raise ValueError( "Please enter the number of the available choices." )
   
    return choice

def add_task():
    
    global ToDoList
    
    mark_again : str = None
    
    while( mark_again != 'N' and mark_again != 'n' ) :
        
        new_task = str( input( "\nPlease enter the new task: " ) )
        ToDoList.append(new_task)
        
        mark_again = str( input( "Add another task ? [Y/N] ? " ) )
        
        if mark_again != 'y' and mark_again != 'Y' and mark_again != 'n' and mark_again != 'N' :
            
            raise ValueError( "Not from the available choices." )
    
def print_ToDoList():
    
    print()
    
    global ToDoList
    
    for indx, ls in enumerate( ToDoList ) :
        
        print( f" {indx+1}- {ls} " )

def task_done():
    
    print()
    
    global ToDoList
    
    global DoneList
    
    mark_again : str = None
    
    while( mark_again != 'N' and mark_again != 'n' ) :
        
        task_indx = int( input( "Enter the index of the done task: " ) )

        if (task_indx - 1) < 0 or (task_indx - 1) > len( ToDoList ) :
            
            raise ValueError( "A wrong index." )
        
        DoneList.append( ToDoList.pop(task_indx - 1) )     

        mark_again = str( input( "Mark another task ? [Y/N] ? " ) )
        
        if mark_again != 'y' and mark_again != 'Y' and mark_again != 'n' and mark_again != 'N' :
            
            raise ValueError( "Not from the available choices." )
    
def print_DoneList():
    
    print()
    
    global DoneList
    
    for indx, ls in enumerate( DoneList ) :
        
        print( f" {indx+1}- {ls} " )

    


































































