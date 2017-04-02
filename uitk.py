from Tkinter import *
from ttk import *
from tkFont import *
from PIL import Image, ImageTk
import tkMessageBox as messagebox
def nextPage(event):
    global page
    global resNo
    global frame1
    global label2
    global procNo
    global procMaxNo
    global but2
    if page==1:
        if resNo==0:
            messagebox.showerror(title="Resource Manager",message="Add atleast one resource to continue")
        else:
            msg=messagebox.askokcancel(title="Resource Manager",message="Do you want to continue?")
            if msg==True:
                page=page+1
                frame1.destroy()
                frame1 = Frame(window)
                frame1.pack(side=TOP, pady=30)
                label2 = Label(frame1, text="Manage Processes (Maximum resource for each process)", relief=RIDGE, font=fontSmall)
                label2.grid(row=0, column=0,columnspan=2+2*resNo)

                but2 = Button(frame1, text="+", command=addProcess)
                but2.grid(row=1, column=0)

                but3 = Button(frame1, text="-", command=remProcess)
                but3.grid(row=1, column=1)

                for i in range(resNo):
                    Label(frame1, text="Resource " + str(i + 1)).grid(row=1, column=2+i*2,columnspan=2)
                    Label(frame1, text="Value").grid(row=2, column=2 + i*2,padx=5)
                    Label(frame1, text="Change").grid(row=2, column=3 + i*2,padx=5)

    elif page == 2:
        if procNo == 0:
            messagebox.showerror(title="Process Manager", message="Add atleast one process to continue")
        else:
            msg=messagebox.askokcancel(title="Process Manager",message="Do you want to continue?")
            if msg==True:
                page=page+1
                but2.config(state=DISABLED)
                label2.config(text="Manage Processes (Resource allocated for each process)")
                for i in range(procNo):
                    for j in range(resNo):
                        procMaxLabel[i][j].config(text="0")
