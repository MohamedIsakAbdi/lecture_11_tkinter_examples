from tkinter import *


top = Tk()
top.geometry("300x200")
top.config(bg="orange")

def display_hello():
    username = Entry(top,text="")
    # username = E1.get()
    result_label.config(text=f"Hello {username}!",bg="orange")
    

L1 = Label(top, text="User Name", fg="white", bg="orange", font=("arial", 20))
L1.pack()

E1 = Entry(top,text="", bd=5)
E1.pack()

# Button to display "Hello" in the Entry widget
hello_button = Button(top, text="Say Hello", command=display_hello, bg="yellow", fg="blue")
hello_button.pack(pady=10)

# Label to display the result
result_label = Label(top, text="", fg="white", bg="black", font=("arial", 12))
result_label.pack()

top.mainloop()
