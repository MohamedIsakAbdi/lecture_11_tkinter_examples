import tkinter
from tkinter import *
from tkinter import font
top = tkinter.Tk() 

# Set the size of the main window
top.geometry("800x600")  # Width x Height

# Create a frame with a specific size and padding
frame_width = 200
frame_height = 50
frame = tkinter.Frame(top, width=frame_width, height=frame_height, padx=10, pady=10)
frame.pack_propagate(False)  # This prevents the frame from resizing to fit its contents
frame.pack()

mb_font = font.Font(size=48)
mb= Menubutton (top, text="condiments", relief=RAISED, height= 60, width=50, font= mb_font) 

mb.menu = Menu ( mb, tearoff = 0) 
mb["menu"] = mb.menu 
mayoVar = IntVar() 
ketchVar = IntVar() 
mb.menu.add_checkbutton(label="mayo", variable=mayoVar) 
mb.menu.add_checkbutton( label="ketchup", variable=ketchVar ) 
mb.pack()

top.mainloop()