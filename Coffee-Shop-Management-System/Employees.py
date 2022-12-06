import json
import BillingSystem

class Employee:
    global emp_login_details, billing
    emp_login_details = {}
    billing = BillingSystem.Billing()

    def __init__(self):
        self.emp_id = ""
        self.password = ""

    def login(self):
        try:
            print("-"*60)
            self.emp_id = input("Enter login ID: ")
            self.password = input("Enter your password: ")

            with open('emp_details.json') as json_file:
                emp_login_details = json.load(json_file)

            if self.emp_id in emp_login_details[self.emp_id]["Employee ID"]:
                if self.password in emp_login_details[self.emp_id]["Password"]:
                    print("You are now logged in!")
            else:
                print("You are not logged in!")

            json_file.close()

        except KeyError:
            print ("Wrong employee login details!")


    def introduce(self):
        print (f"My name is {self.name}.")

    def show_admin_menu(self):
        ctr = 0
        
        self.admin_pass = input("Enter admin password: ")
        
        if self.admin_pass == "jyiwcafe":
            while True:
                print("-"*60)
                print("\t\t☕︎☕︎☕︎ JYIW CAFE ☕︎☕︎☕︎")
                print("-"*60)
                print ("Admin Panel")
                print("-"*60)
                print("[1] - Manager")
                print("[2] - Barista")
                print("[3] - Service crew")
                print("[4] - Cashier")
                print("[5] - Exit")
                print("-"*60)

                try: choice = int(input("Enter you choice: "))
                except ValueError:
                    print("Invalid input!")
                    break
                    
                if choice == 1:
                    ctr = 0
                    manager = Manager()
                    manager.login()
                    ctr = ctr + 1
                elif choice == 2:
                    barista = Barista()
                    barista.login()

                elif choice == 3:
                    crew = ServiceCrew()
                    crew.login()

                elif choice == 4:
                    cashier = Cashier()
                    cashier.login()

                elif choice == 5:
                    print("Shop is now open!")             
                    break
                
                else:
                    print("Invalid input!")
        else:
            print("Invalid password! Please enter the correct password.")
            pass

class Manager(Employee):
    def __init__(self):
        pass

class Barista(Employee):
    def __init__(self):
        pass

    def make_bev(self):
        with open('emp_details.json') as json_file:
            emp_login_details = json.load(json_file)

        barista = emp_login_details['21-08848']["Stage name"]
        print (barista + ", the shop Barista, is making your order/s.")
        
        json_file.close
        

class ServiceCrew(Employee):
    def __init__(self):
        pass

    def assist_customer(self):
        print ("Hi there! Welcome to JYIW CAFE!")
        with open('emp_details.json') as json_file:
            emp_login_details = json.load(json_file)

        service_crew = emp_login_details['21-05676']["Stage name"]
        print ("Hello I am", service_crew, "at your service.")
        
        json_file.close

    def assist_to_cashier(self):
        print("While waiting, please pay for your orders.")
        print("-"*60) 

class Cashier(Employee):
    def __init__(self):
        pass
    
    def assist_customer_to_pay(self):
        print ("Hi there!")
        with open('emp_details.json') as json_file:
            emp_login_details = json.load(json_file)

        cashier = emp_login_details['21-09603']["Stage name"]
        print ("I am " + cashier + ", the shop Cashier.")
        
        json_file.close

    def get_payment(self):
        billing.get_payment()
        billing.total_payment()
        billing.get_change()
        
    def print_bill(self):
        billing.print_reciept()