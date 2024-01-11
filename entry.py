from tkinter import *

def display_hello():
    username = E1.get()
    result_label.config(text=f"Hello {username}!")

top = Tk()

top.geometry("300x200")
top.config(bg="black")

frame = Frame(top, padx=10, pady=10)
frame.pack_propagate(False)
frame.pack()

L1 = Label(top, text="User Name", fg="white", bg="black", font=("arial", 25))
L1.pack()

E1 = Entry(top, bd=5)
E1.pack()

# Button to display "Hello" in the Entry widget
hello_button = Button(top, text="Say Hello", command=display_hello, bg="blue", fg="white")
hello_button.pack()

# Label to display the result
result_label = Label(top, text="", fg="white", bg="black", font=("arial", 12))
result_label.pack()

top.mainloop()
