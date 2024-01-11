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

L1 = Label(top, text="User Name") 
L1.pack( side = LEFT) 
E1 = Entry(top, bd =5) 
E1.pack(side = RIGHT)

top.mainloop()