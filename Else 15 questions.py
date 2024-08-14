from tkinter import *
import tkinter
# create a class file manager to read and write form a file:

#text = "this is a new program"
#class file_manager:
#    def read_to_file(self):
#        with open("text.txt") as file:
#            print(file.read())

#    def write_to_file(self):
#        with open("text.txt" , "w") as file:
#            print(file.write(text))
            
# create a class log that write error message
#class log:
#    def write_error_message():
#        with open("log.txt" , "w") as file:
#            print(file.write("error message"))

# create a class config

#class config:
#    def config_message(self, path):
#        with open(path, "r") as file:
#            print(file.read())
#d = config()
#d.config_message("C:\\Users\\AMK 17The\\Desktop\\factorial.txt")        

# 26. Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price. Provide methods to display ticket details and apply discounts.
#class ticket:
#   def __init__(self, movie_name, seat_number, price):
#        self.movie_name = movie_name
#        self.seat_number = seat_number
#        self.price = price

#   def show_details(self):
#       print(f"the movie name is {self.movie_name},\n seat number {self.seat_number} \n the price ${self.price}")

#   def apply_discount(self, member):
#       if member >= 4:
#           discount = int(input("please insert amount of discount you want!! "))
#           print(f"your new price is ")
#       else:
#           print("sorry!!!!!!, "  " you have not enough member for applying discount.")
#customer = ticket("John", 12, 40)
#customer.apply_discount(5)
#customer.show_details()


# 27. Create a class ShoppingCart with methods to add, remove, and display items.
#  Each item should be an object of a class Item with attributes name and price

#class shpping-cart:
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price
#        self.item = []

#    def add_item(self, new_item):
#        if self.item == new_item:
#            print("item exists")
#        else:
#            self.item.append(new_item)

#    def remove_item(self, old_itme):
#        if self.item == old_itme:
#            self.item.remove(old_itme)
#        else:
#            print("the file does not exists")

# 28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide methods to add and remove items from the menu.

#    class restaurant:
#        def __init__(self, name , meenu):
#            self.name = name
#            self.menu = ["pizza", "potato chips", "humbarger", "hotdog", "fries", "Kabab", "Qabli_palaw"]
#            print(f"name of customer { self.name}, and menu {self.menu}")

#        def add_items(self, new_items):
#            if new_items == self.menu:
#                print('the items excits in the menu ')
#            else:
#                self.menu.append(new_items)
#                print("you added the itme")

#        def remove_item(self, remove_item):
#            if remove_item == self.menu:
#                self.menu.remove(remove_item)
#            else:
#                print("the itme you wanna remove is not excits")

#        def new_menu(self):
#            print(f"your menu is {self.menu}")

#    customer = restaurant("Ali", "your menu is: ")
#    customer.add_items("pasta")
#    customer.new_menu()
            

# 30 create a class Hotel with attributes name and rooms(list of room objects). each room should have attributes room_number and is_occupied
# methods to book and checkout.

#class room:
#    def __init__(self, room_number):
#        self.room_number = room_number
#        self.is_occupied = False

#    def book(self):
#        if not self.is_occupied:
#            self.is_occupied = True
#            print(f"the room {self.room_number}  booked.")
#        else:
#            print(f"the room has been already {self.room_number} booked.")

#    def checkout(self):
#        if self.is_occupied:
#            self.is_occupied = False
#            print(f"the room {self.room_number} is available")
#        else:
#            print(f"the room {self.room_number} isn't available")

#class hotel:
#    def __init__(self, name):
#        self.name = name
#        self.rooms = []

#    def add_room(self, room_number):
#        self.rooms.append(room(room_number))

#    def book_room(self, room_number):
#        for room in self.rooms:
#            if room.room_number == room_number:
#                room.book()
#                return
#            print(f"the room {room_number} does not exists")

#    def checkout_room(self, room_number):
#        for room in self.rooms:
#            if room.room_number == room_number:
#                room.checkout()
#                return
#            print(f"the room {room_number} isn't available")

#grand_hotel = hotel("Grand Hotel")
#grand_hotel.add_room(101)
#grand_hotel.add_room(102)
#grand_hotel.add_room(103)

#grand_hotel.book_room(101)
#grand_hotel.checkout_room(102)


# 38. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.


#calculation = ""
#def add_calculation_symbol(symbol):
 #   global calculation
 #   calculation += str(symbol)
#    text.delete(1.0 , END)
#    text.insert(1.0 , calculation)

#def evalute_calcualtion():
#    global calculation
#    try:
#       calculation = str(eval(calculation))
#       text.delete(1.0, END)
#       text.insert(1.0 , calculation)
#    except:
#        clear_field()
#        text.insert(1.0 , "error")

#def clear_field():
#    global calculation
#    calculation = ""
#    text.delete(1.0, END)
#root = Tk()
#root.geometry("300x400")
#root.title("calcuator")

#text = Text(root)
#text.grid(row= 0, columnspan=3)

#Button(root, width=3, height=1, text="C", font=("arial"), bd=1, bg="#fff", fg="#3697f5", command= lambda:clear_field()).place(x=10, y=100)
#Button(root, width=3, height=1, text="/", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda: add_calculation_symbol("/")).place(x=70, y=100)
#Button(root, width=3, height=1, text="%", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command=lambda : add_calculation_symbol("%")).place(x=130, y=100)
#Button(root, width=3, height=1, text="*", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("*")).place(x=190, y=100)

#Button(root, width=5, height=1, text="7", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("7")).place(x=10, y=200)
#Button(root, width=5, height=1, text="8", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("8")).place(x=70, y=200)
#Button(root, width=5, height=1, text="9", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("9")).place(x=130, y=200)
#Button(root, width=5, height=1, text="-", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("-")).place(x=190, y=200)

#Button(root, width=5, height=1, text="4", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("4")).place(x=10, y=300)
#Button(root, width=5, height=1, text="5", font=("arial"), bd=1, bg="#fff", fg="#2a2d36",command= lambda : add_calculation_symbol("5")).place(x=70, y=300)
#Button(root, width=5, height=1, text="6", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("6")).place(x=130, y=300)
#Button(root, width=5, height=1, text="+", font=("arial"), bd=1, bg="#fff", fg="#2a2d36", command= lambda : add_calculation_symbol("+")).place(x=190, y=300)

#root.mainloop()


# . Create a class FileManager with methods to read from and write to a file
#text = "this is a new one"
#class filemaneger:
#    def read_to_file(self):
#        with open ("C:\\Users\\AMK 17The\\Desktop\\test.txt") as file:
#            print(file.read())

#    def write_to_file(self):
#        with open ("C:\\Users\\AMK 17The\\Desktop\\test.txt", 'w') as file:
#            print(file.write(text))

#read = filemaneger()
#read.read_to_file()
#read.write_to_file()




# create a login page using tkinter.

#import tkinter as tk  
#from tkinter import messagebox  

#class LoginApp:  
   # def __init__(self, master):  
       # self.master = master  
       # master.title("Login Form")  

        #self.label_username = tk.Label(master, text="Username:")  
        #self.label_username.grid(row=0, column=0)  

        #self.entry_username = tk.Entry(master)  
       # self.entry_username.grid(row=0, column=1)  

      #  self.label_password = tk.Label(master, text="Password:")  
     #   self.label_password.grid(row=1, column=0)  

    #    self.entry_password = tk.Entry(master, show="*")  
   #     self.entry_password.grid(row=1, column=1)  

  #      self.login_button = tk.Button(master, text="Login", command=self.login)  
 #       self.login_button.grid(row=2, columnspan=2)  
#
      #  self.message_label = tk.Label(master, text="")  
     #   self.message_label.grid(row=3, columnspan=2)  

    #def login(self):  
   #     username = self.entry_username.get()  
  #      password = self.entry_password.get()  

 #       if username == "admin" and password == "password":  
#            self.message_label.config(text="Login successful!", fg="green")  

    #    elif username == "" and password == "":
   #         messagebox.showerror(title="show error", message="insert your username and password")
  #      else:  
 #           self.message_label.config(text="Invalid credentials. Try again.", fg="red")  

#if __name__ == "__main__":  
   # root = tk.Tk()  
   # app = LoginApp(root)  
   # root.mainloop()


# . Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and decrement buttons.

#from tkinter import *
#root = Tk()

#count = 0
#def increase_counter():
#    global count
#    count += 1
#    print(count)

#count = 0
#def decrease_counter():
#    global count
#    count -= 1
#    print(count)

#decrease_button = Button(root, text="decrease", command=decrease_counter)
#decrease_button.pack()

#increase_button = Button(root, text="increase", command=increase_counter)
#increase_button.pack()

#root.mainloop()
        

# create a to do app using tkinter

#class To_do_app:
#    def __init__(self, root):
#        self.root = root
#        self.root.title("To DO App")
#        self.root.geometry("400x300")
        

#        self.task_entry = Entry(self.root, text=" ")
#        self.task_entry.place(x=200)

#        self.add_task_button = Button(self.root, text="add task", bg="black", fg="green",relief="groove", bd=5, command=self.add_task)
#        self.add_task_button.place(x=200, y= 25, width=70)

#        self.listbox = Listbox(self.root, relief="raised", bd=5)
#        self.listbox.place(x=10, y=10)

#        self.remove_task_button = Button(self.root, text="remove task", bg="black", fg="green", relief="ridge", bd=5, command=self.remove)
#        self.remove_task_button.place(x= 280, y=25, width=70)
        
#    def add_task(self):
#        self.listbox.insert(self.listbox.size(), self.task_entry.get())
#        self.task_entry.delete(0, END)
             
#    def remove(self):
#        self.listbox.delete(self.listbox.curselection())


#if __name__ == "__main__":
#    root = Tk()
#    To_do_app(root)

# create a weather app using tkinter



#class weather_app:
#    def __init__(self, master):
#        self.master = master
#        self.master.title("weather app")
#        self.master.geometry("400x200")

#        self.entry_lable = Label(self.master, text="enter the city")
#        self.entry_lable.grid(row=0, column=0)#

#        self.city_entry = Entry(self.master, text="")
#        self.city_entry.grid(row=0, column=1)

 #       self.weather_button = Button(self.master, text="get weather", command=self.get_weather, bg="black", fg="white")
 #       self.weather_button.grid(row=0, column=2)
#
#        self.weather_lable = Label(self.master, text="")
#        self.weather_lable.grid(row=1,columnspan=3)

#    def get_weather(self):
#        weather = self.city_entry.get()
#        response = {
 #           "main":{"temp":20},
 #           "weather":[{"discription": "sky clear"}],
 #           "name" : weather
#        }

#        if "name" in response:
#            temp = response["main"]["temp"]
#            discription = response["weather"][0]["discription"]
#            self.weather_lable.config(text=f"weather in {response['name']}: {temp}C, {discription}")
        
#        elif weather == "":
#            messagebox.showerror("error", "please insert a region")
        
#        else:
#            messagebox.showerror(text="error", Message="unble to find erea.")



#if __name__ == "__main__":
#    root = Tk()
#    app = weather_app(root)
#    root.mainloop()