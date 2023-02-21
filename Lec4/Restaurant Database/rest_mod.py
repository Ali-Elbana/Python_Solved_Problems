
import csv

admin_pass = "123"

menu_ls = [ ]

order_ls = { }

""" -------------------------------------------------------------------------------- """

with open( "menu.csv", "r", newline='' ) as menu :
        
        menu_items = csv.DictReader( menu )

        for i, menu_row in enumerate(menu_items) :
        
            menu_ls.append( menu_row )
    
""" -------------------------------------------------------------------------------- """

def print_menu():
    
    global menu_ls
    
    print()
    
    with open( "menu.csv", "r", newline='' ) as menu :
        
        menu_items = csv.DictReader( menu )

        for i, menu_row in enumerate(menu_items) :
            
            print( f"{i+1}-{menu_row['Item'].capitalize()}" ) 
            
            #menu_ls.append( menu_row )
          
""" -------------------------------------------------------------------------------- """

def select_mode():
    
    print()
    print( "1-Admin mode." )
    print( "2-Client mode." )
    print( "3-Exit." )

""" -------------------------------------------------------------------------------- """

def get_ModeChoice():
    
    modeChoice = int( input( "\nPlease enter your choice: " ) )
   
    if modeChoice != 1 and modeChoice != 2 and modeChoice != 3 :
        
        print( "Please enter the number of the available choices." )
   
    return modeChoice

""" -------------------------------------------------------------------------------- """

def print_adminChoices() :
    
    print()
    print( "1-Show Menu." )
    print( "2-Edit Menu." )
    print( "3-Exit." )

""" -------------------------------------------------------------------------------- """

def get_adminChoice():
    
    adminChoice = int( input( "\nPlease enter your choice: " ) )
   
    if adminChoice != 1 and adminChoice != 2 and adminChoice != 3 :
        
        print( "Please enter the number of the available choices." )
   
    return adminChoice

""" -------------------------------------------------------------------------------- """

def admin_mode():
    
    global admin_pass
    
    print("-------------------------Admin Mode-------------------------")
    
    entered_pass = str( input( "\nEnter the password: " ) )
    
    if entered_pass != admin_pass :
        
        print( "Incorrect password" )
        
    else :
        
        showMenu        = 1
        editMenu        = 2
        exit_adminMode  = 3
        entered_choice  = None
        
        while( entered_choice != exit_adminMode ) :
        
            print_adminChoices()
        
            entered_choice = get_adminChoice()
        
            if entered_choice == showMenu :
                
                print_menu()
        
            elif entered_choice == editMenu :
                    
                edit_menu()
           
""" -------------------------------------------------------------------------------- """

def edit_menu():
    
    append      = 1
    modify      = 2
    remove      = 3
    exit_edit   = 4   
    
    entered_choice  = None
  
    while( entered_choice != exit_edit ) :
    
        print_editMenu()      
    
        entered_choice = get_editChoice()
     
        if entered_choice == append :
            
            editMenu_append()
    
        elif entered_choice == modify :
                
            editMenu_modify()
        
        elif entered_choice == remove :
                
            editMenu_remove()
           
""" -------------------------------------------------------------------------------- """

def print_editMenu():
    
    print()
    print("1-Append item to the menu.")
    print("2-Modify the menu.")
    print("3-Remove item from the menu.")    
    print("4-Exit.") 
    
""" -------------------------------------------------------------------------------- """

def get_editChoice():
    
    editChoice = int( input( "\nPlease enter your choice: " ) )
   
    if editChoice != 1 and editChoice != 2 and editChoice != 3 and editChoice != 4 :
        
        print( "Please enter the number of the available choices." )
   
    return editChoice

""" -------------------------------------------------------------------------------- """

def editMenu_append():
    
    appended_item       = str( input("\nPlease enter the item you want to add: ") )
    appended_quantity   = int( input("\nEnter the item quantity: ") )
    appended_price      = int( input("\nEnter the item price: ") )
    
    menu_ls.append( {   'Item'    : appended_item , 
                        'Quantity': appended_quantity ,
                        'Price'   : appended_price
                    } )
    
    with open( "menu.csv", "a", newline='' ) as menu :
        
        fieldnames = [ 'Item', 'Quantity', 'Price' ]
        
        writer = csv.DictWriter( menu, fieldnames=fieldnames )
        
        writer.writerow( {'Item'    : appended_item , 
                          'Quantity': appended_quantity ,
                          'Price'   : appended_price
                          } )   

""" -------------------------------------------------------------------------------- """

def editMenu_modify():
    
    global menu_ls
    
    item_indx = int( input("\nPlease enter the index of the item you want to modify: ") )
    
    item_indx -= 1
    
    if item_indx < 0 or item_indx > (len(menu_ls) - 1) :
        
        print("Item not found")
        
    else :
        
        item_name       = 1
        item_quantity   = 2
        item_price      = 3
        exit_modify     = 4
        entered_choice  = None
        
        while( entered_choice != exit_modify ) :
        
            print_modifyMenu()
        
            entered_choice = get_modifyChoice()
        
            if entered_choice == item_name :
                
                modify_itemName( item_indx )
        
            elif entered_choice == item_quantity :
                    
                modify_itemQuantity( item_indx )
           
            elif entered_choice == item_price :
                    
                modify_itemPrice( item_indx )
           
        with open( "menu.csv", "w", newline='' ) as menu :
        
            fieldnames = [ 'Item', 'Quantity', 'Price' ]
            
            writer = csv.DictWriter( menu, fieldnames=fieldnames )
            
            writer.writeheader()
            
            for row in menu_ls :
                
                writer.writerow( {  'Item'    : row['Item']     , 
                                    'Quantity': row['Quantity'] ,
                                    'Price'   : row['Price']
                            } )  

""" -------------------------------------------------------------------------------- """

def print_modifyMenu():
    
    print()
    print("1-Modify item name.")
    print("2-Modify item quantity.")
    print("3-Modify item price.")    
    print("4-Exit.") 

""" -------------------------------------------------------------------------------- """

def get_modifyChoice():
    
    modifyChoice = int( input( "\nPlease enter your choice: " ) )
   
    if modifyChoice != 1 and modifyChoice != 2 and modifyChoice != 3 and modifyChoice != 4 :
        
        print( "Please enter the number of the available choices." )
   
    return modifyChoice
    
""" -------------------------------------------------------------------------------- """

def modify_itemName( indx ):
    
    global menu_ls
    
    new_name = str( input( "\nPlease enter the new item name: "  ) )
    
    menu_ls[indx]["Item"] = new_name
    
""" -------------------------------------------------------------------------------- """

def modify_itemQuantity( indx ):
    
    global menu_ls
    
    new_quantity = int( input( "\nPlease enter the new item quantity: "  ) )
    
    menu_ls[indx]["Quantity"] = new_quantity
  
""" -------------------------------------------------------------------------------- """

def modify_itemPrice( indx ):
    
    global menu_ls
    
    new_price = int( input( "\nPlease enter the new item price: "  ) )
    
    menu_ls[indx]["Price"] = new_price
  
""" -------------------------------------------------------------------------------- """

def editMenu_remove():
    
    global menu_ls
    
    item_indx = int( input("\nPlease enter the index of the item you want to remove: ") )
    
    item_indx -= 1
    
    if item_indx < 0 or item_indx > len(menu_ls) :
        
        print("Item not found")
        
    else :

        menu_ls.pop( item_indx )

        with open( "menu.csv", "w", newline='' ) as menu :
        
            fieldnames = [ 'Item', 'Quantity', 'Price' ]
            
            writer = csv.DictWriter( menu, fieldnames=fieldnames )
            
            writer.writeheader()
            
            for row in menu_ls :
                
                writer.writerow( {  'Item'    : row['Item']     , 
                                    'Quantity': row['Quantity'] ,
                                    'Price'   : row['Price']
                            } )  

""" -------------------------------------------------------------------------------- """

def client_mode():
    
    print("-------------------------Client Mode-------------------------")
    
    print_menu()
    
    get_order()
    
    print_receipt()
    
    clear_receipt()
    
""" -------------------------------------------------------------------------------- """

def get_order() :
    
    global menu_ls
    global order_ls

    found_flag          = False
    underQuantity_flag  = False
    
    add_again : str = None
    
    while( add_again != 'N' and add_again != 'n' ) :
       
        entred_order    = str( input("\nEnter the ordered item: ") ).lower()
        entred_quantity = int( input("\nEnter the order's quantity: ") )
        
        order_ls = { "Item": entred_order, "Quantity": entred_quantity, "Price": 0 }
        
        for menu in menu_ls :

            if order_ls["Item"] in menu["Item"] :
            
                found_flag = True
            
                if order_ls["Quantity"] <= int( menu["Quantity"] ) :  
                    
                    menu["Quantity"] = int( menu["Quantity"] ) - int( order_ls["Quantity"] )
                    
                    order_ls["Price"] = order_ls["Quantity"] * int( menu["Price"] )
                    
                    underQuantity_flag = True
                    
                    break
                                            
        if found_flag == False :
            
            print( "\nItem not found on the menu." ) 
            
        if underQuantity_flag == False :
            
            print( "\nOrdered quantity not available." ) 
        
        with open( "receipt.csv", "a", newline='' ) as receipt :
            
            fieldnames = [ 'Item', 'Quantity', 'Price' ]
            
            writer = csv.DictWriter( receipt, fieldnames=fieldnames )
            
            writer.writerow( order_ls )
        
        with open( "menu.csv", "w", newline='' ) as menu :
        
            fieldnames = [ 'Item', 'Quantity', 'Price' ]
            
            writer = csv.DictWriter( menu, fieldnames=fieldnames )
            
            writer.writeheader()
            
            for row in menu_ls :
                
                writer.writerow( {  'Item'    : row['Item']     , 
                                    'Quantity': row['Quantity'] ,
                                    'Price'   : row['Price']
                            } )  

        add_again = str( input( "Add another item ? [Y/N] ? " ) )
        
        if add_again != 'y' and add_again != 'Y' and add_again != 'n' and add_again != 'N' :
            
            print( "Not from the available choices." )
            
""" -------------------------------------------------------------------------------- """

def print_receipt():
    
    total_price = 0
    
    print()
    
    print("You ordered: ")
    
    with open( "receipt.csv", "r", newline='' ) as receipt :
        
        receipt_items = csv.DictReader( receipt )

        for i, row in enumerate(receipt_items) :
            
            total_price += int( row['Price'] )
            
            print( f"{i+1}-{row['Item'].capitalize()} \t Quantity: {row['Quantity']} \t Price: {row['Price']}" ) 
            
    print(f"\nTotal price = {total_price} EGP")     
         
""" -------------------------------------------------------------------------------- """
           
def clear_receipt() :
    
    with open( "receipt.csv", "w", newline='' ) as receipt :
       
       receipt.truncate()

       fieldnames = [ 'Item', 'Quantity', 'Price' ]
            
       writer = csv.DictWriter( receipt, fieldnames=fieldnames )
            
       writer.writeheader()
             
        
""" -------------------------------------------------------------------------------- """
  