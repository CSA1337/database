from os import system, name
import pandas as pd
import copy
import json
from io import StringIO
from tabulate import tabulate

products = []
couriers = []
orders = []
courier = {}
order = {}


def pull_data(file_name:str) -> list:
    with open(file_name, 'r') as data:
        return json.load(data)

def save_data(list_to_save: list , file_name: str):
    with open(file_name, 'w') as data:
        json.dump(list_to_save, data, indent=4)

def load_products():
    file = open('products.txt', 'r')
    for line in file.readlines():
        products.append(line.rstrip("\n"))

def error():
    print("Error! Invalid input. Try again...")

def write_product():
    with open ('products.txt', 'w') as file:
        for product in products:
            file.write(product)
            file.write("\n")

def write_orders():
    save_data(orders, 'orders.json')

def write_couriers():
    save_data(couriers, 'couriers.json')

def main():
    while True:
        try:
            clear()
            main_banner()
            print("0 - Exit\n1 - Product Menu\n2 - Courier Menu\n3 - Order Menu")
            choice = int(input("\nOption: "))
            if choice not in range(0, 4):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            write_couriers()
            write_product()
            write_orders()
            quit()
        elif choice == 1:
            clear()
            product_banner()
            product_menu()
        elif choice == 2:
            clear()
            courier_banner()
            courier_menu()
        elif choice == 3:
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
            return
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
            return
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
    print(tabulate(orders,showindex=True,headers='keys',tablefmt='fancy_grid'))

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
            order["customer_phone"] = number
            break
        else:
            print("Invalid input. Try again.")
            continue
    order["order_status"] = "Received"
    dict_copy = copy.deepcopy(order)
    orders.append(dict_copy)

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

def courier_menu():
    while True:
        try:
            print("\n\n0 - Main menu\n1 - All Couriers\n2 - New Courier")
            print("3 - Update Courier\n4 - Delete Courier")
            choice = int(input("\nOption: "))
            if choice not in range(0,5):
                error()
                continue
        except:
            error()
            continue
        if choice == 0:
            return
        elif choice == 1:
            courier_list()
        elif choice == 2:
            create_courier()
            print("Courier has been added...")
        elif choice == 3:
            courier_list()
            update_courier()
            print("Courier has been Updated...")
        elif choice == 4:
            courier_list()
            delete_courier()
            print("Courier has been deleted...")

def courier_list():
    print(tabulate(couriers,showindex=True,headers='keys',tablefmt='fancy_grid'))

def create_courier():
    while True:
        name = input("Customer Name: ")
        if name.isalpha() == True:
            courier["customer_name"] = name.title()
            break
        else:
            print("Invalid input!!!")
            continue
    c_name = input("Courier Name: ")
    courier["courier_name"] = c_name
    address = input("Customer Address: ")
    courier["customer_address"] = address
    while True:
        number = input("Customer Phone: ")
        if len(number) == 11 and number.isdigit() == True:
            courier["customer_phone"] = number
            break
        else:
            print("Invalid input. Try again.")
            continue
    dict_copy = copy.deepcopy(courier)
    couriers.append(dict_copy)

def update_courier():
    while True:
        try:
            option = int(input("Option: "))
            courier = couriers[option]
            break
        except:
            error()
            continue
    for key, value in courier.items():
        print(f"Key: {key}, Value: {value}")
        new_value = input("Enter New Value: ")
        if new_value.strip() == '':
            continue
        else:
            courier[key] = new_value

def delete_courier():
    while True:
        try:
            option = int(input("Which courier you want to delete: "))
            courier = couriers[option]
            break
        except:
            error()
            continue
    couriers.remove(courier)

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

def courier_banner():
        print("""
 ██████╗ ██████╗ ██╗   ██╗██████╗ ██╗███████╗██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██╔════╝██╔═══██╗██║   ██║██╔══██╗██║██╔════╝██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
██║     ██║   ██║██║   ██║██████╔╝██║█████╗  ██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║     ██║   ██║██║   ██║██╔══██╗██║██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
╚██████╗╚██████╔╝╚██████╔╝██║  ██║██║███████╗██║  ██║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                               
""")

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

if __name__ == "__main__":
    load_products()
    couriers = pull_data('couriers.json')
    orders = pull_data('orders.json')
    main()