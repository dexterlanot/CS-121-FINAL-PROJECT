from OrderingSystem import *
from Employees import *


class Customer:

    def __init__(self):
        pass

    def customer_name_input(self):
        try:
            self.name = input("\nWhat is your name? -> ")
        except ValueError:
            print("Invalid input!\n")
        return self.name

    def pay(self):
        try:
            self.c_money = int(input("Enter amount to pay: "))
        except ValueError:
            print("Invalid input!\n")
        return self.c_money

    def customer_menu(self):
        assist = Employees.ServiceCrew()
        cashier = Employees.Cashier()
        customer = Customer()
        while True:
            print("-"*60)
            print('\033[1m', "\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
            print("-"*60)
            print("Customer Panel")
            print("-"*60)
            print("[1] - Order")
            print("[2] - Pay order")
            print("[3] - Cancel order")
            print("[4] - Exit")
            print("-"*60)

            order = Order()
            try:
                do = int(input("Enter your choice -> "))
            except ValueError:
                print("Invalid input!")
                break

            if do == 1:
                assist.assist_customer()
                order.get_order()

            elif do == 2:
                cashier.assist_customer_to_pay()
                cashier.get_payment()
            elif do == 3:
                order = Order()
                order.print_orders()
                try:
                    self.cancel = int(
                        input("Do you want to cancel your orders? \n[1] Yes, [2] No -> "))
                except ValueError:
                    print("Invalid input!\n")
                if self.cancel == 1:
                    order.clear_orders()
                    print("Your order/s are now cancelled...\n")
                elif self.cancel == 2:
                    print("Proceed to paying your order bill...\n")
                    pass
            elif do == 4:
                order.clear_orders()
                break
            else:
                print("Invalid input!")
                break
