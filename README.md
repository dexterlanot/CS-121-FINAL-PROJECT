# Coffee Shop Management System

Final Project in **CS 121 - Advanced Computer Programming**   
Instructor: Dr. Francis Jesmar P. Montalbo

**Group Members**
 - Ilao, Whayne Darlyne R. -
[@whayneilao](https://www.github.com/whayneilao)
 - Lagajeno, Yeleina P. -
[@Yeleina](https://www.github.com/Yeleina)
 - Lanot, John Dexter R. -
[@dexterlanot](https://www.github.com/dexterlanot)
 - Pagcaliwagan, Ivy Nicole M. -
[@ivynicole](https://www.github.com/ivynicole)

## Self Assesment

The group evaluated the system using the provided grading rubric, which resulted in the following:

| Metric             	| 4 	| 3 	| 2 	| 1 	|
|--------------------	|---	|---	|---	|---	|
| Code Reusability   	|   	|    	| ✔     |   	|
| Maintainability    	|   	| ✔ 	|   	|   	|
| Scalability        	| ✔ 	|   	|   	|   	|
| Execution          	|   	| ✔ 	|   	|   	|
| Originality        	| ✔ 	|   	|   	|   	|
| Overall Impression 	|    	| ✔  	|   	|   	|

## Project Overview

Because of the current demand for instant coffee or tea, the programmers decided to develop a shopping business system that is related to the shop's day-to-day operations. The Python programming language and Object-Oriented Programming (OOP) concepts were used to create this system. In software, classes and objects and inheritance are used specifically. Furthermore, the programmers used JSON to store employee data, which is retrieved upon logging in, and file handling to keep track of each shop order.

## Pre-requisites
Make sure you have installed maskpass before you use the system.

 - [Maskpass](https://pypi.org/project/maskpass/) is a Python library like getpass but with advanced features like masking and reveal/un-reveal. 


### Installation
Use the package manager pip to install maskpass.

```
pip install maskpass
```
# Video Demo

The video includes a code breakdown as well as an output demonstration. [**Click here**](https://youtu.be/sy2JWudIQ9I) or click the video thumbnail below to watch the video presentation. Time stamps are added to the video description.

[![Video](https://img.youtube.com/vi/sy2JWudIQ9I/maxresdefault.jpg)](https://youtu.be/sy2JWudIQ9I)

# General Information

### Admin Interface

An employee must input the admin password to gain access to the admin interface. After verification, each staff (Manager, Barista, Service crew, and Cashier) should log in to open the store system for client interaction. The system will only be available for customers when all of the employees have logged in.

### Customer Interface

This interface includes the ordering system and the billing system. Customers can add orders and pay the bill associated with their orders. And a reciept will be generated right after a successful transaction. Also, customer can cancel their order if they wanted to.

# UML Diagram
![Diagram](images/CSMS-UML.png "UML Diagram")

# System Walk-through
## Step 1: Login of Employees is required!

The main menu is the first thing you'll see when you boot up the system. This main menu has the following options: **Admin, Customer, View shop menu, and Exit**.   

```
[1] - Admin
[2] - Customer
[3] - View shop menu
[4] - Exit
```

The shop employees must select the Admin option, which will display the admin menu. To enter the admin menu, however, a password is required to verify that the user is an employee. Customers will be unable to access the Customer and View shop menus if this is not done. **Manager, Barista, Service Crew, Cashier, Open Shop and Exit** are the options here. 

```
[1] - Manager
[2] - Barista
[3] - Service crew
[4] - Cashier
[5] - Open Shop
[6] - Exit
```
When selected, the Barista, Service Crew, and Cashier go directly to login. When Manager is selected, the manager menu appears, which includes **Login**, **View employee data** retrieved from a JSON file, **View order records** retrieved from a text file created whenever a successful customer order and billing transaction occurs, and **Exit**. Furthermore, if the manager does not log in, he or she cannot access the View employee data and View order records options.

```
[1] - Login
[2] - View employee data
[3] - View order records
[4] - Exit
```
Following that, a counter is added to the code to determine whether or not all of the shop employees have already logged in. After all employees have logged in, the employee will see the message *"Cafe is now OPEN!!"* when navigating to the **Open Shop** in the admin menu. If not, the message *"All employees are required to login before opening the shop!"* will appear.

## Step 2: Customers can now navigate to the View shop menu

Selecting the View Shop menu in the options will only display the shop's available beverages. In real-life situations, a customer should first browse the menu and decide on a beverage before placing an order.

## Step 3: Customer interface

By selecting the Customer option from the main menu, you will be taken to the customer menu, which includes **Order, Pay order, Cancel order, and Exit**.

```
[1] - Order
[2] - Pay order
[3] - Cancel order/s
[4] - Exit
```
* Order

After selecting Order, the system will ask the customer what type of beverage he or she prefers. There are four options are **Hot Coffee, Cold Coffee, Milk Tea, and Exit**.

```
What do you want?
[A] Hot Coffee, [B] Cold Coffee, [C] Milk Tea
or [D] Exit
```
Customers can choose the type of beverage they want, then the specific drinks they want to buy, as well as the size and quantity.

* Pay order

When this option is selected, the total amount to be paid by the customer is displayed. The system will prompt the customer to enter the amount of money he or she wishes to pay. If the amount is greater than the total amount due, the system will calculate how much change the customer will receive. Following that, the customer will receive a receipt.

* Cancel order

When this option is selected, the system will ask the customer to verify if he or she wants to cancel the order. If yes, the system will remove the customer's order from the queue otherwise the system will display a message *"Proceed to paying your order bill..."*.

# Conclusion

The programmers created this system not only to meet the requirement, but also to learn Python programming, which will help us on our path to becoming future system developers. We learned about various OOP principles and their implementation, as well as advanced programming, in this course. With this, we successfully created the "Coffee Shop Management System," which enabled us to explore and discover advanced skills required for the system's completion.
