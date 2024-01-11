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

text = Text(top) 
text.insert(INSERT, "Hello.....") 
text.insert(END, "Bye Bye.....") 
text.pack() 
text.tag_add("here", "1.0", "1.4") 
text.tag_add("start", "1.8", "1.13") 
text.tag_config("here", background="yellow", foreground="blue") 
text.tag_config("start", background="black", foreground="green") 

top.mainloop()