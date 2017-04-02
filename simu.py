import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B1 = Tkinter.Button(top, text ="Hello1", command = helloCallBack)
B.pack()
B1.pack()
top.mainloop()
