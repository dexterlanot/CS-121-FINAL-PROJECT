import json
import maskpass
import BillingSystem


class Employee:
    global emp_login_details, billing
    emp_login_details = {}
    billing = BillingSystem.Billing()

    def __init__(self):
        self.emp_id = ""
        self.password = ""

    def login(self):

        print("-"*60)
        try:
            self.emp_id = input("\nEnter login ID: ")
            self.password = maskpass.advpass(
                prompt="Enter password: ", mask='*')

            with open('emp_details.json') as json_file:
                emp_login_details = json.load(json_file)

            if self.emp_id in emp_login_details[self.emp_id]["Employee ID"]:
                if self.password in emp_login_details[self.emp_id]["Password"]:
                    print("Successful! You are now logged in!\n")
                    return True
            else:
                print("You are not logged in!")

            json_file.close()

        except KeyError:
            print("Wrong employee login details!\n")
            return False

    def introduce(self):
        print(f"My name is {self.name}.")

    def show_admin_menu(self):
        ctr = 0

        self.admin_pass = maskpass.advpass(
            prompt="\nEnter admin password: ", mask='*')

        if self.admin_pass == "lifebeginsaftercoffee":
            print("Successful!\n")
            while True:
                print("-"*60)
                print('\033[1m', "\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
                print("-"*60)
                print("Admin Panel")
                print("-"*60)
                print("[1] - Manager")
                print("[2] - Barista")
                print("[3] - Service crew")
                print("[4] - Cashier")
                print("[5] - Open Shop")
                print("[6] - Exit")
                print("-"*60)

                try:
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input!")
                    pass

                if choice == 1:
                    ctr = 0
                    manager = Manager()
                    manager.manager_menu()
                    ctr = ctr + 1
                elif choice == 2:
                    barista = Barista()
                    if barista.login() == True:
                        ctr = ctr + 2
                    else:
                        ctr = ctr - 1
                elif choice == 3:
                    crew = ServiceCrew()
                    if crew.login() == True:
                        ctr = ctr + 2
                    else:
                        ctr = ctr - 1
                elif choice == 4:
                    cashier = Cashier()
                    if cashier.login() == True:
                        ctr = ctr + 2
                    else:
                        ctr = ctr - 1
                elif choice == 5:
                    if ctr >= 4:
                        print('\n')
                        print('\033[1m'+"Cafe is now OPEN!!"+'\033[0m')
                        print('\n')
                        continue
                    else:
                        print('\n')
                        print('\033[1m'+("!"*60)+'\033[0m')
                        print(
                            '\033[1m'+"All employees are required to login before opening the shop!"+'\033[0m')
                        print('\033[1m'+("!"*60)+'\033[0m')
                        print('\n')
                elif choice == 6:
                    break
                else:
                    print("Invalid input!")
        else:
            print("Invalid password! Please enter the correct password.")
            pass

    def print_emp_record(self):
        while True:
            with open('emp_details.json', 'r') as openfile:
                json_file = json.load(openfile)
            print()
            try:
                self.emp_id = input("Enter Employee ID: ")
            except KeyError:
                break
            if self.emp_id in json_file:
                print('\033[1m', "\n\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
                print("\n---------------------- EMPLOYEE RECORD ---------------------\n")
                print("Employee ID: \t", json_file[self.emp_id]["Employee ID"])
                print("Name: \t\t", json_file[self.emp_id]["Name"])
                print("Job: \t\t", json_file[self.emp_id]["Job"])
                print("Age: \t\t", json_file[self.emp_id]["Age"])
                print("Gender: \t", json_file[self.emp_id]["Gender"])
                print("Contact Number: ",
                      json_file[self.emp_id]["Contact Number"])
                print('\n')
                break
            else:
                print(
                    '\033[1m'+"Invalid Employee ID! Employee record not found."+'\033[0m')
                break


class Manager(Employee):
    def __init__(self):
        pass

    def manager_menu(self):
        while True:
            emp = Employee()
            manager = Manager()
            print("-"*60)
            print("[1] - Login")
            print("[2] - View employee data")
            print("[3] - View order records")
            print("[4] - Exit")
            print("-"*60)

            try:
                self.manager_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input!")
                continue

            if self.manager_choice == 1:
                menu_ctr = 0
                if manager.login() == True:
                    menu_ctr = menu_ctr + 2
                else:
                    menu_ctr = menu_ctr - 1
            elif self.manager_choice == 2:
                if menu_ctr >= 1:
                    emp.print_emp_record()
                else:
                    print('\033[1m'+"You must login first!"+'\033[0m')
            elif self.manager_choice == 3:
                if menu_ctr >= 1:
                    order_records = open("order_record.txt", "r+")
                    print('\033[1m', "\n\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎", '\033[0m')
                    print(
                        "\n----------------------- ORDER RECORD -----------------------\n")
                    print(order_records.read())
                else:
                    print('\033[1m'+"You must login first!"+'\033[0m')
            elif self.manager_choice == 4:
                break
            else:
                print("Invalid input!")
                break


class Barista(Employee):
    def __init__(self):
        pass

    def make_bev(self):
        with open('emp_details.json') as json_file:
            emp_login_details = json.load(json_file)

        barista = emp_login_details['21-08848']["Stage name"]
        print(barista + ", the shop Barista, is making your order/s.")

        json_file.close


class ServiceCrew(Employee):
    def __init__(self):
        pass

    def assist_customer(self):
        print("Hi there! Welcome to JYIW CAFE!")
        with open('emp_details.json') as json_file:
            emp_login_details = json.load(json_file)

        service_crew = emp_login_details['21-05676']["Stage name"]
        print("Hello I am", service_crew, "at your service.")

        json_file.close

    def assist_to_cashier(self):
        print("While waiting, please pay for your orders.")
        print("-"*60)


class Cashier(Employee):
    def __init__(self):
        pass

    def assist_customer_to_pay(self):
        print("Hi there!")
        with open('emp_details.json') as json_file:
            emp_login_details = json.load(json_file)

        cashier = emp_login_details['21-09603']["Stage name"]
        print("I am " + cashier + ", the shop Cashier.")

        json_file.close

    def get_payment(self):
        billing.payment_and_billing()
