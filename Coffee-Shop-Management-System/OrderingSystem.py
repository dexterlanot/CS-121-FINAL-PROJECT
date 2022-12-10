from enum import Enum
import Employees
import datetime

class Size(Enum):
    SMALL = "16 oz"
    LARGE = "22 oz"


class Price(Enum):
    SMALL = 39
    LARGE = 49


class Order:
    global order, order_amount, bev_price, bev_order, bev_quantity, total
    order_amount = []
    bev_price = []
    bev_order = []
    bev_quantity = []

    def __init__(self):
        hot_coffee = ["Cafe Latte", "Cafe Mocha", "Cappuccino", "Americano",
                      "Steamed Milk", "Espresso", "Hazelnut", "House Decaf", "Espresso Decaf"]
        cold_coffee = ["Iced Latte", "Iced Cappuccino", "Iced Flat White", "Iced Americano Black", "Iced Mocha", "Iced Cortado",
                       "Cold Brew with whipped milk", "Strawberry Mint Iced Tea", "Strawberry Lemonade", "Lemon Ginger Iced Tea"]
        milk_tea = ["Almond Milk Tea", "Chocolate Milk Tea", "Fruit Magic Tea", "Coffee Milk Tea", "Ginger Milk Tea",
                    "Hawaiian Fruit Tea", "Lavender Milk Tea", "Taro Milk Tea", "Jack Fruit Tea", "Honey Lemon Tea"]

        shop_products = {"Hot Coffee": hot_coffee,
                         "Cold Coffee": cold_coffee, "Milk Tea": milk_tea}
        self.shop_products = shop_products

    def hot_coffee_menu(self):
        print("-"*60)
        print("[A] ☕︎ Hot Coffee")
        print("-"*60)

        for iteration, x in enumerate(self.shop_products["Hot Coffee"]):
            print(iteration+1, x.ljust(10))

    def cold_coffee_menu(self):
        print("-"*60)
        print("[B] ☕︎ Cold Coffee")
        print("-"*60)

        for iteration, x in enumerate(self.shop_products["Cold Coffee"]):
            print(iteration+1, x)

    def milk_tea_menu(self):
        print("-"*60)
        print("[C] ☕︎ Milk Tea")
        print("-"*60)

        for iteration, x in enumerate(self.shop_products["Milk Tea"]):
            print(iteration+1, x)

    def print_shop_menu(self):
        print("-"*60)
        print('\033[1m', "\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
        print("-"*60)
        print('\033[1m', "Menu\t\t\t\t", Size.SMALL.value, "- P", Price.SMALL.value,
              "|", Size.LARGE.value, "- P", Price.LARGE.value, '\033[0m')
        order = Order()
        order.hot_coffee_menu()
        order.cold_coffee_menu()
        order.milk_tea_menu()

    def hot_coffee_order(self):
        print("-"*60)
        try:
            self.choice = int(input("Your order is: "))
        except ValueError:
            print("Invalid input!")
        print("-"*60)
        self.order_product = self.shop_products["Hot Coffee"][self.choice-1]
        print("\nYou selected",
              self.shop_products["Hot Coffee"][self.choice-1])
        self.to_pay = 0
        self.coffee_choice = 0
        self.coffee_choice = int(input("What size do you want? [1] Small or [2] Large -> "))

        if self.coffee_choice == 1:
            self.size = Size.SMALL.value
            print("You selected", Size.SMALL.value)
            self.quantity = int(input("Quantity: "))
            self.to_pay = self.quantity*Price.SMALL.value

        elif self.coffee_choice == 2:
            self.size = Size.LARGE.value
            print("You selected", Size.LARGE.value)
            self.quantity = int(input("Quantity: "))
            self.to_pay = self.quantity*Price.LARGE.value
        else:
            print("Invalid input!")

        print("-"*60)
        print("You ordered: ")
        print("-"*60)
        print("Order: ", self.order_product)
        print("Quantity: ", self.quantity)
        print("Payment: P", self.to_pay)
        print("-"*60)

        bev_order.append(self.order_product)
        bev_quantity.append(self.quantity)
        bev_price.append(self.to_pay)
        order_amount.append(self.to_pay)

    def cold_coffee_order(self):
        print("-"*60)
        try:
            self.choice = int(input("Your order is: "))
        except ValueError:
            print("Invalid input!")
        print("-"*60)
        self.order_product = self.shop_products["Cold Coffee"][self.choice-1]
        print("\nYou selected",
              self.shop_products["Cold Coffee"][self.choice-1])
        self.to_pay = 0
        self.coffee_choice = 0
        self.coffee_choice = int(input("What size do you want? [1] Small or [2] Large -> "))

        if self.coffee_choice == 1:
            self.size = Size.SMALL.value
            print("You selected", Size.SMALL.value)
            self.quantity = int(input("Quantity: "))
            self.to_pay = self.quantity*Price.SMALL.value

        elif self.coffee_choice == 2:
            self.size = Size.LARGE.value
            print("You selected", Size.LARGE.value)
            self.quantity = int(input("Quantity: "))
            self.to_pay = self.quantity*Price.LARGE.value
        else:
            print("Invalid input!")

        print("-"*60)
        print("You ordered: ")
        print("-"*60)
        print("Order: ", self.order_product)
        print("Quantity: ", self.quantity)
        print("Payment: P", self.to_pay)
        print("-"*60)

        bev_order.append(self.order_product)
        bev_quantity.append(self.quantity)
        bev_price.append(self.to_pay)
        order_amount.append(self.to_pay)

    def milk_tea_order(self):

        print("-"*60)
        try:
            self.choice = int(input("Your order is: "))
        except ValueError:
            print("Invalid input!")

        print("-"*60)
        self.order_product = self.shop_products["Milk Tea"][self.choice-1]
        print("\nYou selected", self.shop_products["Milk Tea"][self.choice-1])
        self.to_pay = 0
        self.coffee_choice = 0
        self.coffee_choice = int(
            input("What size do you want? [1] Small or [2] Large -> "))

        if self.coffee_choice == 1:
            self.size = Size.SMALL.value
            print("You selected", Size.SMALL.value)
            self.quantity = int(input("Quantity: "))
            self.to_pay = self.quantity*Price.SMALL.value

        elif self.coffee_choice == 2:
            self.size = Size.LARGE.value
            print("You selected", Size.LARGE.value)
            self.quantity = int(input("Quantity: "))
            self.to_pay = self.quantity*Price.LARGE.value
        else:
            print("Invalid input!")

        print("-"*60)
        print("You ordered: ")
        print("-"*60)
        print("Order: ", self.order_product)
        print("Quantity: ", self.quantity)
        print("Payment: P", self.to_pay)
        print("-"*60)

        bev_order.append(self.order_product)
        bev_quantity.append(self.quantity)
        bev_price.append(self.to_pay)
        order_amount.append(self.to_pay)

    def get_order(self):
        order = Order()

        print("-"*60)
        while True:
            try:
                self.inquiry = input("\nWhat do you want? \n[A] Hot Coffee, [B] Cold Coffee, [C] Milk Tea \nor [D] Exit -> ")
            except ValueError:
                print("Invalid input! Only choose from A, B, and C")
            self.inquiry = self.inquiry.upper()

            if self.inquiry == 'A':
                print()
                order.hot_coffee_menu()
                order.hot_coffee_order()
            elif self.inquiry == 'B':
                order.cold_coffee_menu()
                order.cold_coffee_order()
            elif self.inquiry == 'C':
                order.milk_tea_menu()
                order.milk_tea_order()
            elif self.inquiry == 'D':
                break
            else:
                print("Oops... It's not in the menu.")
                pass
            barista = Employees.Barista()
            crew = Employees.ServiceCrew()
            while True:
                self.more_order = int(input("Do you want to order more? [1] Yes, [2] No -> "))
                if self.more_order == 1:
                    break
                elif self.more_order == 2:
                    order.print_orders()
                    barista.make_bev()
                    crew.assist_to_cashier()
                    break
                else:
                    break
    
    def clear_orders(self):
        order = Order()
        bev_order.clear()
        bev_quantity.clear()
        bev_price.clear()
        order_amount.clear()

    def total_amount(self):
        self.total = 0
        for price in order_amount:
            self.total = self.total + price
        return self.total

    def print_orders(self):
        print('\n'+"-"*60)
        print("{:38}{:15}{:10}".format("Beverage order/s", "Qty", "Price"))
        print("-"*60)

        for x in range(len(bev_order)):
            print("{:30}{:10}{:15}".format(
                bev_order[x], bev_quantity[x], bev_price[x]))

        print("-"*60)

    def write_to_file(self):
        order = Order()
        date_time = datetime.datetime.now()
        file = open("order_record.txt", "a")
        file.write("-"*60 + "\n")
        file.write(f"\t\t\t\t{date_time.year} / {date_time.day} / {date_time.month}  {date_time.hour}:{date_time.minute}:{date_time.second}")
        file.write('\n' + "-"*60 + '\n')
        file.write("{:33}{:20}{:10}".format(
            "Beverage order/s", "Qty", "Price"))
        file.write('\n'+"-"*60)
        for x in range(len(bev_order)):
            file.write("\n{:35}{:20}{:15}".format(
                bev_order[x], str(bev_quantity[x]), str(bev_price[x])))
        file.write("\n" + "-"*60)
        file.write(f"\nTotal: {order.total_amount()}\n")
        file.close()
