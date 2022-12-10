from datetime import datetime
from Customer import *


class Billing:
    global c_money, total_to_pay, order, customer, bill
    order = Order()
    customer = Customer()

    def __init__(self):
        pass

    def customer_money(self):
        self.c_money = 0
        self.c_money = customer.pay()
        return self.c_money

    def payment_and_billing(self):
        bill = Billing()
        while True:
            order.print_orders

            if order.total_amount() == 0:
                print("You don't have any orders.\n")
                break
            else:
                print(f"Total amount to be paid: {order.total_amount()}")
                # bill.customer_money()
                bill.total_payment()
                bill.print_reciept()
                break

    def total_payment(self):
        bill = Billing()
        self.payment = bill.customer_money()
        if order.total_amount() > self.payment:
            print("Sorry. Your money is not enough to pay for the orders.")
        else:
            self.total_to_pay = 0
            self.total_to_pay = self.total_to_pay + order.total_amount()
            self.change = 0
            self.change = self.payment - self.total_to_pay
            print(f"Your change is P {self.change}")

    def print_reciept(self):
        customer.customer_name_input()
        print("\n\n----------------Please claim you receipt--------------------\n\n")
        print("^"*60)
        print('\033[1m', "\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')

        dt_string = datetime.datetime.now()
        print("\t\t", dt_string)
        print(f"\nCustomer name: {customer.name.capitalize()}")
        order.print_orders()
        print(f"Total: P {self.total_to_pay}")
        print(f"Change: P {self.change}")
        print("\n\n" + "-"*60)
        print("\tThis invoice/reciept shall be valid for five(5)\n\t\tyears from the date atp.")
        print("\n\n---------------------  Thank you!  -------------------------")
        print("☕︎"*30, "\n\n")
        print("^"*60, "\n\n")
        order.write_to_file()
