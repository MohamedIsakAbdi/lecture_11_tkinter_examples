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

m1 = PanedWindow() 
m1.pack(fill=BOTH, expand=1) 



left = Label(m1, text="left pane") 
m1.add(left) 
m2 = PanedWindow(m1, orient=VERTICAL) 
m1.add(m2) 


m2_frame = tkinter.Frame(m2, background='blue', width=100, height=200)
m2_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame_label = Label(m2_frame, text="This is inside the frame m2", background='blue')
frame_label.pack()


m2.add(m2_frame)



top_pane = Label(m2, text="top pane") 
m2.add(top_pane) 

bottom = Label(m2, text="bottom pane") 
m2.add(bottom) 

# labelframe = LabelFrame(top, text="This is a LabelFrame") 
# labelframe.pack(fill="both", expand="yes") 
# left_label = Label(labelframe, text="Inside the LabelFrame") 
# left_label.pack() 


top.mainloop()