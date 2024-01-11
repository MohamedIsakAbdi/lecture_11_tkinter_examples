from tkinter import *

top = Tk() 

# Set the size of the main window
top.geometry("400x300")  # Width x Height
top.config(bg="blue")

frame = Frame(top, padx=10, pady=10)
frame.pack_propagate(False)  # This prevents the frame from resizing to fit its contents
frame.pack()

CheckVar1 = IntVar() 
CheckVar2 = IntVar() 
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, 
height=5, width = 20) 

C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, 
height=5, width = 20) 
C1.pack() 
C2.pack() 
top.mainloop()


