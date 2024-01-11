# from tkinter import *
# from tkinter import font

# top = Tk() 

# # Set the size of the main window
# top.geometry("800x600")  # Width x Height

# # Create a frame with a specific size and padding
# frame_width = 200
# frame_height = 50
# frame = Frame(top, width=frame_width, height=frame_height, padx=10, pady=10)
# frame.pack_propagate(False)  # This prevents the frame from resizing to fit its contents
# frame.pack()
# spinbox_font = font(size=48)

# w = Spinbox(top, from_=0, to=10, width=100, font= spinbox_font) 
# w.pack(padx=10, pady=10)

# top.mainloop()



from tkinter import *

master = Tk() 
master.geometry("300x300")
w = Spinbox(master, from_=0, to=10) 
w.pack() 

mainloop()
