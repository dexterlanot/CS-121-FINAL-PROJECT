from datetime import datetime
from Customer import *

class Billing:
    global c_money, total_to_pay, order, customer
    order = Order()
    customer = Customer()

    def __init__(self):
        pass

    def get_payment(self):
        order.print_orders
        print(f"Total amount to be paid: {order.total_amount()}")
        self.c_money = customer.pay()

    def total_payment(self):
            if order.total_amount() > self.c_money:
                print("Sorry. Your money is not enough to pay for the orders.")
            else:
                self.total_to_pay = 0
                self.total_to_pay = self.total_to_pay + order.total_amount()

    def get_change(self):
        self.change = 0
        self.change = self.c_money - self.total_to_pay
        print (f"Your change is P {self.change}")

    def print_reciept(self):
        customer.customer_name_input()
        print("\n\n----------------Please claim you receipt--------------------\n\n")
        print("^"*60)
        print('\033[1m',"\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
        
        dt_string = datetime.now()
        print("\t\t", dt_string)	
        print(f"\nCustomer name: {customer.name.capitalize()}")
        order.print_orders()
        print(f"Total: P {self.total_to_pay}")
        print (f"Change: P {self.change}")
        print ("\n\n" + "-"*60)
        print ("\tThis invoice/reciept shall be valid for five(5)\n\t\tyears from the date atp.")
        print("\n\n---------------------  Thank you!  -------------------------")
        print("☕︎"*30, "\n\n")
        print("^"*60, "\n\n")