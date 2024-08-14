import math


#  Create a class called Person with attributes name and age. Create an object of the class and print its attributes.
#class person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age


#    def name(self):
#        print(f"your name is {self.name}")
#    def age(self):
#        print(f"you are {self.age} years old.")
#    def info(self):
#        print(f"your name is {self.name} your age is {self.age}")



# 2nd: Add a method called greet to the Person class that prints a greeting message including the person's name.

#class person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def greet(self):
#        print(f"hello {self.name}")


# 3rd:  Create a class called Car with attributes make, model, and year. Include a method to print out the car's details.

#class car:
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#
#    def car_details(self):
#        print(f"this car is made in {self.make}, {self.model} model, and its made in {self.year}")


# 4. Create a class Circle with a method to compute the area. Initialize the class with the radius.
#class circle:
#    def __init__(self, radius):
#        self.radius = radius
#
#    def compute_area(self):
#        print(math.pi * (math.pow(self.radius, 2)))



# . Create a class Rectangle with methods to compute the area and perimeter. Initialize the class with the length and width

#class rectangle:
#    def __init__(self, width, lenght)
#        self.width = width
#        self.length = lenght
#
#    def compute_area(self):
#        print(1/2 * (self.width * self.length))
#
#    def compute_perimeter(self):
#        print(self.length + self.width)

# . Create a base class Animal with a method speak. Create two derived classes Dog and Cat that override the speak method.

#class Animal:
#    def speak()
#        print("yap")

#class dog(Animal):
#    def speak():
#        print("chew")

#class cat(Animal):
#    def speak():
#        print("meow")



#. Create a base class Shape with a method area. Create derived classes Square and Triangle that implement the area method.


# class compute_area:
#    def __init__(self, width, lenght):
#        self.width = width
#        self.lenght = lenght

#class shape:
#    def area(self):
#        raise NotImplementedError


#class rectangle(shape):
#    def __init__(self, width, length):
#        self.length = length
#        self.width = width


#    def area(self):
#        print(1/2 * (self.width * self.lenght))

#class square(shape):
#    def __init__(self, a):
#        self.a= a
    
#    def area(self):
#        print(math.pow(self.a, 2))

# Create a class Employee with attributes name and salary. Create a derived class Manager with an additional attribute department.

#class employess:
#    def __init__(self, name, salary):
#        self.name = name
#        self.salary = salary
#        print(f"your name is {self.name} salary is: {self.salary}")

#class manegar(employess):
#    def __init__(self, name , salary, department):
#        self.department = department
#        self.name = name
#        self.salary = salary
#        print(f"your name is {self.name} salary is: {self.salary} department: {self.department}")



# . Create a base class Vehicle with a method drive. Create derived classes Bike and Truck that override the drive method

#class vehicle:
#    def drive(self):
#        print("you are in the write path")

#class truck(vehicle):
#    def drive(self):
#        pass
#class bike(vehicle):
#    def drive(self):
#        pass


# Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override the fly method in Penguin to indicate that penguins cannot fly.

#class bird:
#    def fly(self):
#        print("birds can fly.")
#class eagle(bird):
#    def fly(self):
#        return super().fly()
    
#class penguin(bird):
#    def fly(self):
#        print("penguin can't fly")

# _________________________________________________________________________________________________
#11 . Create a class Account with private attributes balance. Provide public methods to deposit and withdraw money.

#class account:
#    def __init__(self, balance=0):
#        self.__balance = balance

#    def deposit(self, amount):
#        if amount > 0:
#            self.__balance += amount
#            print(f"diposit amount: ${amount}, and your new balance is ${self.__balance}")
#        else:
#            print("your diposit amount must be greater than zero!")

#    def witdraw(self, amount):
#        if amount > 0:
#            if self.__balance >= amount:
#                self.__balance -= amount
#                print(f' your witdraw amount is : ${amount} and your new account is ${self.__balance}')
#            else:
#                print("no enough money to witdraw")
#        else:
#            pass

#    def get_balance(self):
#        print(f"your balance is ${self.__balance}")

#account = account(500)
#account.deposit(400)
#account.witdraw(100)  

# Create a class Book with private attributes title, author, and pages. Provide public methods to get and set these attributes.

#class book:
#    def __init__(self, title, author, page):
#        self.__title = title
#        self.__author = author
#        self.__page = page

#    def get_title(self):
#        print(self.__title)

#    def set_title(self, new_title):
#        self.__title = new_title
        
#    def get_author(self):
#        print(self.__author)

#    def set_author(self, new_author):
#        self.__author = new_author

#    def get_page(self):
#        print(self.__page)
    
#    def set_page(self, new_page):
#        self.__page = new_page

#book1 = book("Advance programming", "Gabriel Garcia", 400)
#book1.set_title("big Advance grammar")
#book1.get_title()


# Create a class Laptop with private attributes brand, model, and price. Provide a method to apply a discount and a method to display laptop details.

#class laptop:
#    def __init__(self, model, brand, price):
#        self.__model = model
#        self.__brand = brand
#        self.__price = price

#    def deatails(self):
#        print(f'the model of this phone is {self.__model}, brand {self.__brand}, the price is : ${self.__price}')

#    def apply_discount(self, discount):
#        self.__price -= discount

#    def new_price(self):
#        self.__price
#        print(f"your new account is {self.__price}")

#customer = laptop("samsung A55", "True", 350 )
#customer.deatails()
#customer.apply_discount(30)
#customer.new_price()

#Create a class BankAccount with private attributes account_number and balance. Provide methods to deposit, withdraw, and check the balance

#class bank_account:
#    def __init__(self, account_numebr, balance):
#        self.__account_number = account_numebr
#        self.__balance = balance

#    def deposit(self, amount):
#       if amount > 0:
#            self.__balance += amount
#            print(f"your diposit amount is ${amount} and your new account is ${self.__balance}")
#        else:
#            print("you cannot deposit zero.")
    
#    def witdraw(self, amount):
#        if amount > 0:
#            if self.__balance >= amount:
#                self.__balance -= amount
#                print(f"your witdraw amount is ${amount} and your new account is ${self.__balance}")
#            else:
#                print("no enough money")
#        else:
#            print("the witdraw amount can't be zero.")

#    def cheack_balance(self):
#        print(f"your finally balance is ${self.__balance}")


#customer = bank_account(729745927397, 1200)
#customer.deposit(44)
#customer.witdraw(50)
#customer.cheack_balance()


#create a class Student with private attributes name, grade, and age. Provide methods to get and set these attributes and a method to display the student's details.

#class student:
#    def __init__(self, name , grade, age):
#        self.__name = name
#        self.__grade = grade
#        self.__age = age

#    def get(self):
#        print(f"name  :{self.__name}\n grade  :{self.__grade}\n age :{self.__age}")
    
#    def set(self, new_name, new_grade, new_age):
#        self.__name = new_name
#        self.__grade = new_grade
#        self.__age = new_age

#    def detials(self):
#        print(f"your name is {self.__name}, your grade is {self.__grade}, and your age is {self.__age}")

#student1 = student("sahil", "A++", 15)
#student1.set("altaf", "A++", 17)
#student1.detials()


# create a class Library with attributes name and books (a list of Book objects). Provide methods to add and remove books.

#class library:
#    def __init__(self, name , book):
#        self.name = name
#        self.book = ["advance grammer", "advance progarmming", "python for biggners", "don't wast your time"]
#        print(f"your library is {self.book}")
        
#    def add(self, new_book):
#        self.book.append(new_book)
#        print(f"your new book {new_book} added to the library, \n {self.book}")
    
#    def remove(self, remove_book):
#        if remove_book in self.book: 
#            self.book.remove(remove_book)
#            print(f"you removed {remove_book} the book.now library is \n {self.book}")
#        else:
#            print(f'the {remove_book} is not avilible in library,')

#    def currnt_situation(self):
#        if not self.book:
#            print('the library is empty')
#        else:
#            print('the library books')
#            for i in self.book:
#                print(i)

#customer = library("Ahmad", "advance grammar")
#customer.add("C++")
#customer.remove("C++")
#customer.currnt_situation()

# create a class School with attributes name and students (a list of Student objects). Provide methods to add and remove students

#class school:
#    def __init__(self, name, students):
#        self.name = name
#        self.students = ["Ahmad", "Hamid", "Mahmod", "Massod", "Amin"]

#    def add_student(self, new_student):
#        if new_student == self.students:
#            print(f"the student {new_student} exits")
#        else:
#            self.students.append(new_student)
#            print(f"the new studnet added to the list.")

#    def remove_student(self, student):
#        if student in self.students:
#            self.students.remove(student)
#            print(f"you removed the {student} from the list")
#        else:
#            print("the student you want to remove isn't exit")

#    def show_student_list(self):
#        print(f"the list of students {self.students}")

#student1 = school("Habibia high school", "Hamid")
#student1.remove_student("lisa")
#student1.show_student_list()


# Create a class Team with attributes name and members (a list of Person objects). Provide methods to add and remove members.

#class team:
#    def __init__(self, name, member):
#        self.name = name
#        self.member = ["Halim", "Aman", "Ali", "Jabar", "Ramos"]

#    def add_to_team(self, new_member):
#        if new_member == self.member:
#            print("the member has been already exits")
#        else:
#            self.member.append(new_member)
#            print(f"your add new member {new_member}")

 #   def remove_member(self, member_to_remove):
#        if member_to_remove == self.member:
#            self.member.remove(member_to_remove)
#            print(f"you removed {member_to_remove}")
#        else:
#            print("there is no member to remove.")

#    def team_list(self):
#        print(f"the current team member { self.member}.")

#team1  = team("Real Madrid", "members")
#team1.team_list()