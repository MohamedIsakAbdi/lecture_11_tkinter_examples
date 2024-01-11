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


C = Canvas(top, bg="blue", height=400, width=400) 
coord = 8, 8, 400, 400 
arc = C.create_arc(coord, start=0, extent=90, fill="red") 
C.pack() 

top.mainloop()