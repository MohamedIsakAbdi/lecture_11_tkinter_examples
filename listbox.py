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

Lb1 = Listbox(top) 
Lb1.insert(1, "Python") 
Lb1.insert(2, "Perl") 
Lb1.insert(3, "C") 
Lb1.insert(4, "PHP") 
Lb1.insert(5, "JSP") 
Lb1.insert(6, "Ruby") 
Lb1.pack() 

top.mainloop()