import tkinter
from tkinter import *

top = tkinter.Tk() 

# Set the size of the main window
top.geometry("800x600")  # Width x Height

# Create a frame with a specific size and padding
frame_width = 200
frame_height = 50
frame = tkinter.Frame(top, width=frame_width, height=frame_height, padx=10, pady=10)
frame.pack_propagate(False)  # This prevents the frame from resizing to fit its contents
frame.pack()

def sel(): 
    selection = "You selected the option " + str(var.get()) 
    label.config(text = selection)

var = IntVar() 
R1 = Radiobutton(top, text="Option 1", variable=var, value=1, 
command=sel) 
R1.pack( anchor = W ) 
R2 = Radiobutton(top, text="Option 2", variable=var, 
value=2,command=sel) 
R2.pack( anchor = W ) 
R3 = Radiobutton(top, text="Option 3", variable=var, 
value=3,command=sel) 
R3.pack( anchor = W) 
label = Label(top) 
label.pack()

top.mainloop()