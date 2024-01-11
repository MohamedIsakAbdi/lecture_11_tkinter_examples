import tkinter
import tkinter.messagebox as msg

top = tkinter.Tk() 

def helloCallBack(): 
    msg.showinfo( "Hello Python", 
    "Hello World") 

B = tkinter.Button(top, text ="Hello", command = 
helloCallBack,fg="white", bg="black") 
B.pack() 

top.mainloop()