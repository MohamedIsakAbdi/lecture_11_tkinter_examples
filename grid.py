from tkinter import *

app = Tk() 
app.config(bg="#9ea6ad")


label1 = Label(text="7" ,bg="red",width=12)
label1.grid(row=0, column=0,pady=2)
label2 = Label(text="4",bg="red",width=12)
label2.grid(row=1, column=0,pady=2)
label3 = Label(text="1",bg="red",width=12)
label3.grid(row=2, column=0,pady=2)
label4 = Label(text=".",bg="red",width=12)
label4.grid(row=3, column=0,pady=2)
label5 = Label(text=".",bg="red",width=12)
label5.grid(row=4, column=0, pady=2)

label6 = Label(text="8" ,bg="red",width=12)
label6.grid(row=0, column=1,pady=2,padx=2)
label7 = Label(text="5",bg="red",width=12)
label7.grid(row=1, column=1,pady=2,padx=2)
label8 = Label(text="2",bg="red",width=12)
label8.grid(row=2, column=1,pady=2,padx=2)
label9 = Label(text="",bg="red",width=12)
label9.grid(row=3, column=1,pady=2,padx=2)
label0 = Label(text="",bg="red",width=12)
label0.grid(row=4, column=1, pady=2,padx=2)

label11 = Label(text="9" ,bg="red",width=12)
label11.grid(row=0, column=2,pady=2,padx=2)
label12 = Label(text="6",bg="red",width=12)
label12.grid(row=1, column=2,pady=2,padx=2)
label13 = Label(text="3",bg="red",width=12)
label13.grid(row=2, column=2,pady=2,padx=2)
label14 = Label(text="",bg="red",width=12)
label14.grid(row=3, column=2,pady=2,padx=2)
label15 = Label(text="",bg="red",width=12)
label15.grid(row=4, column=2, pady=2,padx=2)

label16 = Label(text="÷" ,bg="red",width=12)
label16.grid(row=0, column=3,pady=2,padx=2)
label17 = Label(text="x",bg="red",width=12)
label17.grid(row=1, column=3,pady=2,padx=2)
label18 = Label(text="-",bg="red",width=12)
label18.grid(row=2, column=3,pady=2,padx=2)
label19 = Label(text="+",bg="red",width=12)
label19.grid(row=3, column=3,pady=2,padx=2)
label20 = Label(text="=",bg="red",width=12)
label20.grid(row=4, column=3, pady=2,padx=2)




app.mainloop()
