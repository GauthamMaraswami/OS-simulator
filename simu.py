from Tkinter import *
import tkMessageBox
import time
import random
import Tkinter











window = Tk()
    window.geometry("1050x656")
    def close_window(): 
        window.destroy()
    
    frame = Frame(window)
    frame.pack()
    kutton = Button (frame, text = "Good-bye.", command = close_window)
    kutton.pack()

    window.mainloop()




















import sys

root1 = Tkinter.Tk()
root1.geometry("200x100")
root1.title("No of pages")
def close_root1(): 
        root1.destroy()
counter1 = Tkinter.IntVar()
def onClick(event=None):
    if counter1.get()<20:
        counter1.set(counter1.get() + 1)
    else:
        tkMessageBox.showinfo("error", "max limit reached")
def onClick1(event=None):
    if counter1.get()>0:
        counter1.set(counter1.get() - 1)
    else:
        tkMessageBox.showinfo("error", "no of pages cannot be negative")
L1=Label(root1, textvariable=counter1)
L1.pack()
L1.place(relx=0.5,rely=0.25 )
root1.update
B1=Button(root1, text="+", command=onClick, fg="dark green", bg = "white")
B1.pack()
B1.place(relx=0.2,rely=0.25)
root1.update  
B2=Button(root1, text="-", command=onClick1, fg="dark green", bg = "white")
B2.pack()
B2.place(relx=0.7,rely=0.25)
root1.update  
kutton1 = Button (root1, text = "close.", command = close_root1)
kutton1.pack()
kutton1.place(relx=0.4,rely=0.7)
root1.mainloop()
