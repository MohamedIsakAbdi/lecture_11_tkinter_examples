import tkinter
from tkinter import *

root = tkinter.Tk() 

# Set the size of the main window
root.geometry("800x600")  # Width x Height


frame = Frame(root) 
# Create a frame with a specific size and padding
frame_width = 200
frame_height = 50
frame = tkinter.Frame(root, width=frame_width, height=frame_height, padx=10, pady=10)
frame.pack_propagate(False)  # This prevents the frame from resizing to fit its contents
frame.pack() 

bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text="Red", fg="red") 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text="Brown", fg="brown") 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text="Blue", fg="blue") 
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text="Black", fg="black") 
blackbutton.pack( side = BOTTOM) 
root.mainloop()