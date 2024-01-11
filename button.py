from tkinter import *

root = Tk() 
root.geometry("100x100")
frame = Frame(root) 
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
























# import tkinter
# import tkinter.messagebox as msg

# top = tkinter.Tk() 
# top.geometry("200x100")
# top.config(bg="blue")
# def helloCallBack(): 
#     msg.showinfo( "Hello Python", 
#     "Hello World") 

# B = tkinter.Button(top, text ="Hello", command = 
# helloCallBack,fg="white", bg="black") 
# B.pack() 

# top.mainloop()