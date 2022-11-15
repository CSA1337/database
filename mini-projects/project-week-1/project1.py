# Coded by Suleman Malik

def menu():
    banner = '''
  __  __       _         __  __                  
 |  \/  |     (_)       |  \/  |                 
 | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _ 
 | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |
 | |  | | (_| | | | | | | |  | |  __/ | | | |_| |
 |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|
                                    
    '''
    print(banner)

    print(" [1] View All product")
    print(" [2] Create product")
    print(" [3] Update product")
    print(" [4] Delete product")
    print(" [0] Exit\n")
    try:
        option = int(input(" Enter your option: "))
    except Exception as e:
        error()
    if option == 1:
        View_All_Product()
        menu()
    elif option == 2:
        Create_Product()
    elif option == 3:
        Update_Product()
    elif option == 4:
        Delete_product()
    elif option == 0:
        print(" Thanks for using the program...")
        exit()
    else:
        error()

Database = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]

def error():
    print("Error! Invalid input! Try again...")
    menu()
    
def View_All_Product():
    print("+=======================+")
    print("|   ALL   PRODUCTS      |")
    print("+=======================+")
    for x in range(len(Database)):
        print(f"[{x}] - ", Database[x])
    print("+=======================+")

def Create_Product():
    Create_Option = input("\nNew Product Name:  ")
    Database.append(Create_Option)
    print(f"Product {Create_Option} has been created.")
    menu()

def Update_Product():
    View_All_Product()
    print(len(Database))
    try:
        Update_Option = int(input("\nWhich item you want to update? "))
        if Update_Option < len(Database) and Update_Option >= 0:
            Database[Update_Option] = input("Update Name: ")
            print(f"Product {Update_Option} has been updated with new value '{Database[Update_Option]}'.")
            menu()
        else:
            error()
    except Exception as e:
        error()
        
def Delete_product():
    View_All_Product()
    Delete_Option = int(input("\nWhich item you want to delete? "))
    if Delete_Option < len(Database) and Delete_Option >= 0:
        try:
            x = Database[Delete_Option]
            del Database[Delete_Option]
            print(f"Product {x} has been deleted.")
            menu()
        except IndexError as e:
            error()
    else:
        error()


menu()
