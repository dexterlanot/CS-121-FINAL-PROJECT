import Employees
from Customer import *
import OrderingSystem


class CoffeeShop:

    def show_main_menu():
        global admin
        global ctr
        ctr = 0
        customer = Customer()

        while True:
            print('\n' + "-"*60)
            print("\t  ⛾  COFFEE SHOP MANAGEMENT SYSTEM ⛾")
            print("-"*60)
            print('\033[1m', "\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
            print("-"*60)
            print("[1] - Admin")
            print("[2] - Customer")
            print("[3] - View shop menu")
            print("[4] - Exit")
            print("-"*60)

            try:
                choice = int(input("Enter your choice -> "))
            except ValueError:
                print("Invalid input!")
                continue

            if choice == 1:
                admin = Employees.Employee()
                admin.show_admin_menu()
                ctr = ctr + 1
            elif choice == 2:
                if ctr == 0:
                    print(
                        "\n-----The shop is still closed. Please come back later.------")
                else:
                    customer = Customer()
                    customer.customer_menu()

            elif choice == 3:
                if ctr == 0:
                    print(
                        "\n-----The shop is still closed. Please come back later.------")
                else:
                    order = OrderingSystem.Order()
                    order.print_shop_menu()
                    print("-"*60)
                    customer_decision = int(input("\nHave you decided what to order? [1] Yes or [2] No -> "))
                    if customer_decision == 1:
                        print("--> \"You may take your order now\" ")
                        pass
                    elif customer_decision == 2:
                        print("--> \"You can always take your time\" ")
                        pass
                    else:
                        print("Invalid input!")
                        pass

            elif choice == 4:
                print("Enjoy and goodbye! Hope to see you again...")
                break
