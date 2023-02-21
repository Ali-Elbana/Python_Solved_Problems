import os
from rest_mod import *

def main():
    
    # Clear the terminal screen:
    os.system('cls')
    
    # The available choices numbers:
    adminMode   = 1
    clientMode  = 2
    exitMode    = 3
    
    entered_ModeChoice = None
    
    while( entered_ModeChoice != exitMode ) :
        
        select_mode()
        
        entered_ModeChoice = int( get_ModeChoice() )
        
        if entered_ModeChoice == adminMode :
            
            admin_mode()
    
        elif entered_ModeChoice == clientMode :
                
            client_mode()
                
        
if __name__ == '__main__' :

    print()
    # Write your code here:
        
    main()

    # The end of your code. 
    print(), print()


