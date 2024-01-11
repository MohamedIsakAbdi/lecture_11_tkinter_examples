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

var = DoubleVar() 
def sel(): 
    selection = "Value = " + str(var.get()) 
    label.config(text = selection) 


scale = Scale( top, variable = var, orient=HORIZONTAL) 
scale.pack(anchor=CENTER) 
button = Button(top, text="Get Scale Value", command=sel) 
button.pack(anchor=CENTER) 
label = Label(top) 
label.pack()

top.mainloop()