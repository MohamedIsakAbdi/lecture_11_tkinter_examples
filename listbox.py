from tkinter import *

top = Tk() 

# Set the size of the main window
top.geometry("400x300")  # Width x Height
top.config(bg="orange") # set background color for main window

# Create a frame with a specific size and padding
frame_width = 200
frame_height = 50
instruction_label = Label(text="List Box", fg="white", font=("arial"),15)
instruction_label.pack(pady=12)
frame = Frame(top, padx=10, pady=10)
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