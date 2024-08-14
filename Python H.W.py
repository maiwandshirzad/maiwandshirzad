import tkinter as tk

def display():
    text.delete(1.0, tk.END)
    with open("C:\\Users\\AMK 17The\\Desktop\\factorial.txt") as f:
        data = f.read()
    text.insert(tk.INSERT, data)

    
def display1():
    text.delete(1.0, tk.END)
    with open("C:\\Users\\AMK 17The\\Desktop\\new.txt") as f:
        data1 = f.read()
    text.insert(tk.INSERT, data1)

def display2():
    text.delete(1.0 , tk.END)
    with open("C:\\Users\\AMK 17The\\Desktop\\first.txt") as f:
        data2 = f.read()
    text.insert(tk.INSERT, data2)

Root = tk.Tk()
Root.geometry("600x500")
Root.config(bg="pink")
Root.title("My HOME WORK")


buttonframe = tk.Frame(Root)
buttonframe.columnconfigure(0, weight=4)
buttonframe.columnconfigure(1, weight=4)
buttonframe.columnconfigure(2, weight=4)

button = tk.Button(buttonframe, text="first", bg="black", fg="green", command= display)
button.grid(row=0, column=0, sticky= tk.W+tk.E)

button1 = tk.Button(buttonframe, text="second", bg="black", fg="green", command=display1)
button1.grid(row=0, column=1, sticky= tk.W + tk.E)

button2 = tk.Button(buttonframe, text="third", bg="black", fg="green", command= display2)
button2.grid(row=0, column=2, sticky=tk.W + tk.E)
buttonframe.pack(fill="x")

text = tk.Text(Root, width=70, height=20, bg="yellow")
text.pack()


Root.mainloop()