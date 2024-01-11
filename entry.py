from tkinter import *

top = Tk() 

# Set the size of the main window
top.geometry("300x200")  # Width x Height
top.config(bg="black")
# Create a frame with a specific size and padding

frame = Frame(top,  padx=10, pady=10)
frame.pack_propagate(False)  # This prevents the frame from resizing to fit its contents
frame.pack()

L1 = Label(top, text="User Name", fg="white",  bg="black", font=("arial",25)) 
L1.pack() 
E1 = Entry(top, bd =5) 
E1.pack()

top.mainloop()