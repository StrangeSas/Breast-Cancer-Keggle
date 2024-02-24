from tkinter import *

root = Tk()
root.title("calculator")

e = Entry(root, width = 50)
e.grid(row = 4, column = 1)
def myClick():
    myLabel4 = Label(root, text=e.get())
    myLabel4.grid(row = 1, column = 0)

button1 = Button(root, text="Balls", command=myClick)
button1.grid(row = 0, column = 0)
button2 = Button(root, text="Balls", command=myClick)
button2.grid(row = 0, column = 1)
button3 = Button(root, text="Balls", command=myClick)
button3.grid(row = 0, column = 2)
button4 = Button(root, text="Balls", command=myClick)
button4.grid(row = 1, column = 0)
button5 = Button(root, text="Balls", command=myClick)
button5.grid(row = 1, column = 1)
button6 = Button(root, text="Balls", command=myClick)
button6.grid(row = 1, column = 2)
button7 = Button(root, text="Balls", command=myClick)
button7.grid(row = 2, column = 0)
button8 = Button(root, text="Balls", command=myClick)
button8.grid(row = 2, column = 1)
button9 = Button(root, text="Balls", command=myClick)
button9.grid(row = 2, column = 2)

root.mainloop()