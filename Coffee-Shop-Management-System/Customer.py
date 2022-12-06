from OrderingSystem import *
from Employees import *

class Customer:

    def __init__(self):
        pass

    def customer_name_input(self):
        self.name = input("\nWhat is your name? -> ")
        return self.name

    def pay(self):
        self.c_money = int(input("Enter amount to pay: "))
        return self.c_money

    def customer_menu(self):
        assist = Employees.ServiceCrew()
        cashier = Employees.Cashier()
        customer = Customer()
        while True:
            print("-"*60)
            print('\033[1m',"\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
            print("-"*60)
            print ("Customer Panel")
            print("-"*60)
            print ("[1] - Order")
            print ("[2] - Pay order")
            print ("[3] - Exit")
            print("-"*60)

            order = Order()
            try: do = int(input("Enter your choice -> "))
            except ValueError:
                print("Invalid input!")
                break

            if do == 1:
                assist.assist_customer()
                order.get_order()

            elif do == 2:
                cashier.assist_customer_to_pay()
                cashier.get_payment()
                cashier.print_bill()
            elif do == 3:
                break
            else:
                print("Invalid input!")
                break