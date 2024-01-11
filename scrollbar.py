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

scrollbar = Scrollbar(top) 
scrollbar.pack( side = RIGHT, fill=Y )
mylist = Listbox(top, yscrollcommand = 
scrollbar.set ) 
for line in range(100): 
    mylist.insert(END, "This is line number " + 
    str(line)) 
    
mylist.pack( side = LEFT, fill = BOTH ) 
scrollbar.config( command = mylist.yview ) 

top.mainloop()