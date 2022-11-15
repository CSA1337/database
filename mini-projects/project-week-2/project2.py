from os import system, name

products = []
order = {}
orders = []
location = "/home/samx/Desktop/mini-projects/project-week-2/products.txt"

def load_products():
    file = open(location, 'r')
    for line in file.readlines():
        products.append(line.rstrip("\n"))

def error():
    print("Error! Invalid input. Try again...")
    
def write_product():
    with open (location, 'w') as file:
        for product in products:
            file.write(product)
            file.write("\n")

def main():
    while True:
        try:
            clear()
            main_banner()
            print("0 - Exit\n1 - Product Menu\n2 - Order Menu")
            choice = int(input("\nOption: "))
            if choice not in range(0, 3):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            quit()
        elif choice == 1:
            clear()
            product_banner()
            product_menu()
        elif choice == 2:
            clear()
            order_banner()
            order_menu()

def product_menu():
    while True:
        try:
            print("\n\n0 - Main menu\n1 - All Product\n2 - New Product")
            print("3 - Update Product\n4 - Delete_Product")
            choice = int(input("Option: "))
            if choice not in range(0,5):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            main()
        elif choice == 1:
            print_product()
        elif choice == 2:
            create_product()
        elif choice == 3:
            print_product()
            update_product()
            print("Product has been updated...")
        elif choice == 4:
            print_product()
            delete_product()
            print("Product has been deleted...")
            product_menu()

def print_product():
    print("+=======================+")
    print("|   ALL   PRODUCTS      |")
    print("+=======================+")
    for x in range(len(products)):
        print(f"[{x}] - ", products[x])
    print("+=======================+")

def create_product():
    product_name = input("\nProduct Name: ")
    products.append(product_name.title())
    write_product()

def update_product():
    while True:
        try:
            Choice = int(input("Which product you like to update: "))
            products[Choice]
            product = input("Enter updated product: ")
            products[Choice] = product.title()
            break
        except:
            error()
            continue
    write_product()

def delete_product():
    while True:
        try:
            choice = int(input("Which product you like to delete: "))
        except:
            error()
            continue
        del products[choice]
        break
    write_product()

def order_menu():
    while True:
        try:
            print("\n\n0 - Main menu\n1 - All Orders\n2 - New Order")
            print("3 - Order Status\n4 - Update order\n5 - Delete Order")
            choice = int(input("\nOption: "))
            if choice not in range(0,6):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            main()
        elif choice == 1:
            order_list()
        elif choice == 2:
            create_order()
            print("Order has been added...")
        elif choice == 3:
            order_list()
            order_status()
            print("Status has been Updated...")
        elif choice == 4:
            order_list()
            update_order()
            print("Order has been Updated...")
        elif choice == 5:
            order_list()
            delete_order()
            print("Order has been deleted...")

def order_list():
    print("+=======================+")
    print("|   ALL   Orders      |")
    print("+=======================+")
    for x in range(len(orders)):
        print(f"[{x}] - ", orders[x])
    print("+=======================+")

def create_order():
    while True:
        name = input("Customer Name: ")
        if name.isalpha() == True:
            order["customer_name"] = name.title()
            break
        else:
            print("Invalid input!!!")
            continue
    address = input("Customer Address: ")
    order["customer_address"] = address
    while True:
        number = input("Customer Phone: ")
        if len(number) == 11 and number.isdigit() == True:
            order["customer_number"] = number
            break
        else:
            print("Invalid input. Try again.")
            continue
    order["order_status"] = "Received"
    orders.append(order)

def update_order():
    while True:
        try:
            option = int(input("Option: "))
            order = orders[option]
            break
        except:
            error()
            continue
    for key, value in order.items():
        print(f"Key: {key}, Value: {value}")
        new_value = input("Enter New Value: ")
        if new_value.strip() == '':
            continue
        else:
            order[key] = new_value

def delete_order():
    while True:
        try:
            option = int(input("Which order you want to delete: "))
            order = orders[option]
            break
        except:
            error()
            continue
    orders.remove(order)

def order_status():
    while True:
        try:
            option = int(input("Option: "))
            orders[option]
        except:
            error()
            continue
        else:
            while True:
                status = ["Received", "Preparing", "Shipped","Delivered"]
                print("\n0 - Received\n1 - Preparing\n2 - Shipped\n3 - Delivered")
                status_update = int(input("Choice: "))
                order = orders[option]
                if status_update not in range(0,4):
                    error()
                    continue
                else:
                    order["order_status"] = status[status_update]
                    break
            break

def main_banner():
    print("""
███╗   ███╗ █████╗ ██╗███╗   ██╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔══██╗██║████╗  ██║    ████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║███████║██║██╔██╗ ██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                          
    """)

def product_banner():
    print("""
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝    ████╗ ████║██╔════╝████╗  ██║██║   ██║
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║       ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║       ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║       ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝       ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                     
    """)

def order_banner():
    print("""
 ██████╗ ██████╗ ███████╗██████╗ ███████╗██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
██║   ██║██████╔╝█████╗  ██║  ██║█████╗  ██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║   ██║██╔══██╗██╔══╝  ██║  ██║██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
╚██████╔╝██║  ██║███████╗██████╔╝███████╗██║  ██║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                           
    """)

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

load_products()
main()