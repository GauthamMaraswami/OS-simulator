from Tkinter import *
import tkMessageBox
import time
import random
import Tkinter
import sys
root = Tk()

WIDTH = 1920
HEIGHT = 1080
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
root.title("Page replacement")
canvas.pack()


a = []
n=0

m=0
#input n
def getcount():
    global n
    counter1 = 0
    redbutton = Label(canvas, text="enter no of pages", fg="black",height=2,bd=2)
    redbutton.pack()
    redbutton.place(relx=0.68,rely=0.02)
    root.update()    
    
    
    def onClick(event=None):
        global n
        if n<20:
            n=n + 1
            L1=Label(root, text=(n), fg="red",height=1,width=4)
    	    L1.pack()
            L1.place(relx=0.7,rely=0.07 )
        else:
            tkMessageBox.showinfo("error", "max limit reached")
    def onClick1(event=None):
        global n
        if n>0:
            n=n - 1
            L1=Label(root, text=(n), fg="red",height=1,width=4)
    	    L1.pack()
            L1.place(relx=0.7,rely=0.07 )
        else:
            tkMessageBox.showinfo("error", "no of pages cannot be negative")
    
    B1=Button(root, text="+", command=onClick, fg="dark green", bg = "white")
    B1.pack()
    B1.place(relx=0.67,rely=0.07)
    root.update()  
    B2=Button(root, text="-", command=onClick1, fg="dark green", bg = "white")
    B2.pack()
    B2.place(relx=0.73,rely=0.07)
    root.update()
    
def getframe():
    global m
    counter1 = 0
    redbutton = Label(canvas, text="enter no of frames", fg="black",height=2,bd=2)
    redbutton.pack()
    redbutton.place(relx=0.81,rely=0.02)
    root.update()    
    
    
    def onClick2(event=None):
        global m
        if m<10:
            m=m + 1
            L1=Label(root, text=(m), fg="red",height=1,width=4)
    	    L1.pack()
            L1.place(relx=0.85,rely=0.07 )
        else:
            tkMessageBox.showinfo("error", "max limit reached")
    def onClick3(event=None):
        global m
        if m>0:
            m=m - 1
            L1=Label(root, text=(m), fg="red",height=1,width=4)
    	    L1.pack()
            L1.place(relx=0.85,rely=0.07 )
        else:
            tkMessageBox.showinfo("error", "no of pages cannot be negative")
    
    B1=Button(root, text="+", command=onClick2, fg="dark green", bg = "white")
    B1.pack()
    B1.place(relx=0.81,rely=0.07)
    root.update()  
    B2=Button(root, text="-", command=onClick3, fg="dark green", bg = "white")
    B2.pack()
    B2.place(relx=0.87,rely=0.07)
    root.update()

def getobjects():
    for i in range(n):
        t = 0
        a.append(t)
        redbutton = Label(canvas, text=i, fg="black",height=1,bd=1)
        redbutton.pack()
        redbutton.place(relx=0.73,rely=0.15+i*0.04)
        root.update()
        if n>0:    
            def onClick4(event=None):  
                if a[0]<10:
                    a[0]=a[0] + 1
                    L1=Label(root, text=(a[0]), fg="red",height=1,width=4)
            	    L1.pack()
                    L1.place(relx=0.85,rely=-0.10+0.25 )
                else:
                    tkMessageBox.showinfo("error", "max limit reached")
            def onClick5(event=None):
                if a[0]>0:
                    a[0]=a[0] - 1
                    L1=Label(root, text=(a[0]), fg="red",height=1,width=4)
            	    L1.pack()
                    L1.place(relx=0.85,rely=-0.10+0.25 )
                else:
                    tkMessageBox.showinfo("error", "no of pages cannot be negative")
            B1=Button(root, text="+", command=onClick4, fg="dark green", bg = "white")
            B1.pack()
            B1.place(relx=0.81,rely=-0.10+0.25)
            root.update()  
            B2=Button(root, text="-", command=onClick5, fg="dark green", bg = "white")
            B2.pack()
            B2.place(relx=0.87,rely=-0.10+0.25)
            root.update()
            if(n>1):
                def onClick6(event=None):  
                    if a[1]<10:
                        a[1]=a[1] + 1
                        L1=Label(root, text=(a[1]), fg="red",height=1,width=4)
    	                L1.pack()
                        L1.place(relx=0.85,rely=-0.10+0.29 )
                    else:
                        tkMessageBox.showinfo("error", "max limit reached")
                def onClick7(event=None):
                    if a[1]>0:
                        a[1]=a[1] - 1
                        L1=Label(root, text=(a[1]), fg="red",height=1,width=4)
                        L1.pack()
                        L1.place(relx=0.85,rely=-0.10+0.29 )
                    else:
                        tkMessageBox.showinfo("error", "no of pages cannot be negative")
                B3=Button(root, text="+", command=onClick6, fg="dark green", bg = "white")
                B3.pack()
                B3.place(relx=0.81,rely=-0.10+0.29)
                root.update()  
                B4=Button(root, text="-", command=onClick7, fg="dark green", bg = "white")
                B4.pack()
                B4.place(relx=0.87,rely=-0.10+0.29)
                root.update()
                if(n>2):
                    def onClick8(event=None):  
                        if a[2]<10:
                            a[2]=a[2] + 1
                            L1=Label(root, text=(a[2]), fg="red",height=1,width=4)
                    	    L1.pack()
                            L1.place(relx=0.85,rely=-0.10+0.33 )
                        else:
                            tkMessageBox.showinfo("error", "max limit reached")
                    def onClick9(event=None):
                        if a[2]>0:
                            a[2]=a[2] - 1
                            L1=Label(root, text=(a[2]), fg="red",height=1,width=4)
                    	    L1.pack()
                            L1.place(relx=0.85,rely=-0.10+0.33 )
                        else:
                            tkMessageBox.showinfo("error", "no of pages cannot be negative")
                    B5=Button(root, text="+", command=onClick8, fg="dark green", bg = "white")
                    B5.pack()
                    B5.place(relx=0.81,rely=-0.10+0.33)
                    root.update()  
                    B6=Button(root, text="-", command=onClick9, fg="dark green", bg = "white")
                    B6.pack()
                    B6.place(relx=0.87,rely=-0.10+0.33)
                    root.update()
                if n>3:    
                    def onClick10(event=None):  
                        if a[3]<10:
                            a[3]=a[3] + 1
                            L1=Label(root, text=(a[3]), fg="red",height=1,width=4)
                    	    L1.pack()
                            L1.place(relx=0.85,rely=-0.10+0.37 )
                        else:
                            tkMessageBox.showinfo("error", "max limit reached")
                    def onClick11(event=None):
                        if a[3]>0:
                            a[3]=a[3] - 1
                            L1=Label(root, text=(a[3]), fg="red",height=1,width=4)
                    	    L1.pack()
                            L1.place(relx=0.85,rely=-0.10+0.37 )
                        else:
                            tkMessageBox.showinfo("error", "no of pages cannot be negative")
                    B5=Button(root, text="+", command=onClick10, fg="dark green", bg = "white")
                    B5.pack()
                    B5.place(relx=0.81,rely=-0.10+0.37)
                    root.update()  
                    B6=Button(root, text="-", command=onClick11, fg="dark green", bg = "white")
                    B6.pack()
                    B6.place(relx=0.87,rely=-0.10+0.37)
                    root.update()
    if n>4:
        def onClick12(event=None):  
            if a[4]<10:
                a[4]=a[4] + 1
                L1=Label(root, text=(a[4]), fg="red",height=1,width=4)
    	        L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.41 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick13(event=None):
            if a[4]>0:
                a[4]=a[4] - 1
                L1=Label(root, text=(a[4]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.41 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick12, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.41)
        root.update()  
        B6=Button(root, text="-", command=onClick13, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.41)
        root.update()
    if n>5:
        def onClick14(event=None):  
            if a[5]<10:
                a[5]=a[5] + 1
                L1=Label(root, text=(a[5]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.45 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick15(event=None):
            if a[5]>0:
                a[5]=a[5] - 1
                L1=Label(root, text=(a[5]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.45 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick14, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.45)
        root.update()  
        B6=Button(root, text="-", command=onClick15, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.45)
        root.update()
    if n>6:
        def onClick16(event=None):  
            if a[6]<10:
                a[6]=a[6] + 1
                L1=Label(root, text=(a[6]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.49 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick17(event=None):
            if a[6]>0:
                a[6]=a[6] - 1
                L1=Label(root, text=(a[6]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.49 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick16, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.49)
        root.update()  
        B6=Button(root, text="-", command=onClick17, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.49)
        root.update()
    if(n>7):
        def onClick18(event=None):  
            if a[7]<10:
                a[7]=a[7] + 1
                L1=Label(root, text=(a[7]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.53 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick19(event=None):
            if a[7]>0:
                a[7]=a[7] - 1
                L1=Label(root, text=(a[7]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.53 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick18, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.53)
        root.update()  
        B6=Button(root, text="-", command=onClick19, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.53)
        root.update()
    if(n>8):
        def onClick20(event=None):  
            if a[8]<10:
                a[8]=a[8]+ 1
                L1=Label(root, text=(a[8]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.57 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick21(event=None):
            if a[8]>0:
                a[8]=a[8] - 1
                L1=Label(root, text=(a[8]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.57 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick20, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.57)
        root.update()  
        B6=Button(root, text="-", command=onClick21, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.57)
        root.update()
    if n>9:
        def onClick22(event=None):  
            if a[9]<10:
                a[9]=a[9] + 1
                L1=Label(root, text=(a[9]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.61 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick23(event=None):
            if a[9]>0:
                a[9]=a[9] - 1
                L1=Label(root, text=(a[9]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.61 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick22, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.61)
        root.update()  
        B6=Button(root, text="-", command=onClick23, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.61)
        root.update()
    if n>10:
        def onClick24(event=None):  
            if a[10]<10:
                a[10]=a[10] + 1
                L1=Label(root, text=(a[10]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.65 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick25(event=None):
            if a[10]>0:
                a[10]=a[10] - 1
                L1=Label(root, text=(a[10]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.65 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick24, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.65)
        root.update()  
        B6=Button(root, text="-", command=onClick25, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.65)
        root.update()
    if n>11:
        def onClick26(event=None):  
            if a[11]<10:
                a[11]=a[11] + 1
                L1=Label(root, text=(a[11]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.69 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick27(event=None):
            if a[11]>0:
                a[11]=a[11] - 1
                L1=Label(root, text=(a[11]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.69 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick26, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.69)
        root.update()  
        B6=Button(root, text="-", command=onClick27, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.69)
        root.update()
    if n>12:
        def onClick28(event=None):  
            if a[12]<10:
                a[12]=a[12] + 1
                L1=Label(root, text=(a[12]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.73 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick29(event=None):
            if a[12]>0:
                a[12]=a[12] - 1
                L1=Label(root, text=(a[12]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.73 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick28, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.73)
        root.update()  
        B6=Button(root, text="-", command=onClick29, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.73)
        root.update()
    if n>13:
        def onClick30(event=None):  
            if a[13]<10:
                a[13]=a[13] + 1
                L1=Label(root, text=(a[13]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.77 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick31(event=None):
            if a[13]>0:
                a[13]=a[13] - 1
                L1=Label(root, text=(a[13]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.77 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick30, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.77)
        root.update()  
        B6=Button(root, text="-", command=onClick31, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.77)
        root.update()
    if n>14:
        def onClick32(event=None):  
            if a[14]<10:
                a[14]=a[14] + 1
                L1=Label(root, text=(a[14]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.81 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick33(event=None):
            if a[14]>0:
                a[14]=a[14] - 1
                L1=Label(root, text=(a[14]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.81 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick32, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.81)
        root.update()  
        B6=Button(root, text="-", command=onClick33, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.81)
        root.update()
    if n>15:
        def onClick34(event=None):  
            if a[15]<10:
                a[15]=a[15] + 1
                L1=Label(root, text=(a[15]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.85 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick35(event=None):
            if a[15]>0:
                a[15]=a[15] - 1
                L1=Label(root, text=(a[15]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.85 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick34, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.85)
        root.update()  
        B6=Button(root, text="-", command=onClick35, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.85)
        root.update()
    if n>16:
        def onClick36(event=None):  
            if a[16]<10:
                a[16]=a[16] + 1
                L1=Label(root, text=(a[16]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.89 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick37(event=None):
            if a[16]>0:
                a[16]=a[16] - 1
                L1=Label(root, text=(a[16]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.89 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick36, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.89)
        root.update()  
        B6=Button(root, text="-", command=onClick37, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.89)
        root.update()
    if n>17:
        def onClick38(event=None):  
            if a[17]<10:
                a[17]=a[17] + 1
                L1=Label(root, text=(a[17]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.93 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick39(event=None):
            if a[17]>0:
                a[17]=a[17] - 1
                L1=Label(root, text=(a[17]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.93 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick38, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.93)
        root.update()  
        B6=Button(root, text="-", command=onClick39, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.93)
        root.update()
    if n>18:
        def onClick40(event=None):  
            if a[18]<10:
                a[18]=a[18] + 1
                L1=Label(root, text=(a[18]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.97 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick41(event=None):
            if a[18]>0:
                a[18]=a[18] - 1
                L1=Label(root, text=(a[18]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+0.97 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick40, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+0.97)
        root.update()  
        B6=Button(root, text="-", command=onClick41, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+0.97)
        root.update()
    if n>19:
        def onClick42(event=None):  
            if a[19]<10:
                a[19]=a[19] + 1
                L1=Label(root, text=(a[19]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+1.01 )
            else:
                tkMessageBox.showinfo("error", "max limit reached")
        def onClick43(event=None):
            if a[19]>0:
                a[19]=a[19] - 1
                L1=Label(root, text=(a[19]), fg="red",height=1,width=4)
                L1.pack()
                L1.place(relx=0.85,rely=-0.10+1.01 )
            else:
                tkMessageBox.showinfo("error", "no of pages cannot be negative")
        B5=Button(root, text="+", command=onClick42, fg="dark green", bg = "white")
        B5.pack()
        B5.place(relx=0.81,rely=-0.10+1.01)
        root.update()  
        B6=Button(root, text="-", command=onClick43, fg="dark green", bg = "white")
        B6.pack()
        B6.place(relx=0.87,rely=-0.10+1.01)
        root.update()
        La=Label( canvas, textvariable="fffffffffffffffffffff",fg="dark green",bg="black",height=(200-n),width=50 )
        La.pack()
        La.place(relx=0.8,rely=1-(0.068*(20-n)) )
        root.update()
        
#Function to accept reference string and frame size.
def accept():
    getcount()
    getframe()
  
    yellobutton = Button(canvas, text="accept", fg="black",bg="yellow",height=1,width=5,command=getobjects)
    yellobutton.pack()
    yellobutton.place(relx=(0.5),rely=0.15)
    root.update()
    #La=Label( canvas, textvariable="fffffffffffffffffffff",fg="dark green",height=(20),width=50 )
    #La.pack()
    #La.place(relx=0.5,rely=0.5 )
    #root.update()


def generate():
    redbutton = Label(canvas, text="generating", fg="red",height=15,width=30,bg="yellow")
    redbutton.pack()
    redbutton.place(relx=0.2,rely=0)
    root.update()
    tc=0
    global a,n,m

    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("page que")
    label.pack()
    label.place(relx=0.1,rely=0.425)
    root.update 
    for i in range(n):
        t = random.randrange(0,10)
        a.append(t)
        redbutton = Label(canvas, text=a[i], fg="red",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        tc=tc+0.02
    m = 3
    root.update()  
#First In First Out Page Replacement Algorithm
def __fifo():
    var="What is First in First Out page replacement algorithm?\nA FIFO replacement algorithm associates with each page the time when that page was brought into memory. When a page must be replaced, the oldestpage is chosen"
    tkMessageBox.showinfo("fifo", var)
    root.update
    global a,n,m
    f = -1
    page_faults = 0
    page = []
    fu=0
    cul= []
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
 

    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("Frames que")
    label.pack()
    label.place(relx=0.1,rely=0.6)
    root.update     
    for i in range(m):
        page.append(-1)
        cul.append(0)
    tc=0
    for i in range(n):
        redbutton = Label(canvas, text=a[i], fg="red",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        tc=tc+0.02
    for i in range(n,20):
        redbutton = Label(canvas, text=" ", fg="red",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        tc=tc+0.02
    tc=0
    for i in range(n):
        if i>0:
            redbutton = Label(canvas, text=a[i-1], fg="red" ,bg="yellow",height=1,width=4)
            redbutton.pack()
            redbutton.place(relx=(0.02*(i-1)+0.01),rely=0.5)
            time.sleep(0.5)
            root.update()
        redbutton = Label(canvas, text=a[i], fg="red" ,bg="green",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        root.update()
        tc=tc+0.02
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%m
            page[f] = a[i]
            page_faults+=1
            tkMessageBox.showinfo("error", "page fault")
            root.update()
            print "\n%d ->" % (a[i]),
            if cul[f]==0:
                cul[f]=1
            else:
                cul[f]=0
            for j in range(m):
                if page[j] != -1:
                    if cul[j]==0:
                        print page[j],
                        redbutton = Label(canvas, text=page[j], fg="red" ,bg="yellow",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                    else:
                        print page[j],
                        redbutton = Label(canvas, text=page[j], fg="red" ,bg="blue",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                else:
                    if cul[j]==0:
                        print "-",
                        redbutton = Label(canvas, text="N", fg="red" ,bg="yellow",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                    else:
                        print "-",
                        redbutton = Label(canvas, text="N", fg="red" ,bg="blue",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            tkMessageBox.showinfo("error", "no page fault")
            root.update()
    print "\n Total page faults : %d." % (page_faults)
    tkMessageBox.showinfo("error", "Total page faults : %d." % (page_faults))
    root.update 
#Least Recently Used Page Replacement Algorithm
def __lru():
    global a,n,m
    var="Least recently used Page replacement algorithm?\nLRU chooses the page that has not been used for the longest period of time."
    tkMessageBox.showinfo("lru", var)
    root.update
    x = 0
    page_faults = 0
    page = []
    cul= []
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set(" ")
    label.pack()
    label.place(relx=0.3,rely=0.775)
    root.update  
    redbutton = Label(canvas, text="LRU", fg="black",height=15,width=30,bg="green")
    redbutton.pack()
    redbutton.place(relx=0.2,rely=0)
    root.update()
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("Frames que")
    label.pack()
    label.place(relx=0.1,rely=0.6)
    root.update
    for i in range(m):
        page.append(-1)
        cul.append(0)
        
    tc=0
    for i in range(n):
        redbutton = Label(canvas, text=a[i], fg="red",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        tc=tc+0.02
    for i in range(n,20):
        redbutton = Label(canvas, text=" ", fg="red",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        tc=tc+0.02
    tc=0
    for i in range(n):
        flag = 0
        if i>0:
            redbutton = Label(canvas, text=a[i-1], fg="red" ,bg="yellow",height=1,width=4)
            redbutton.pack()
            redbutton.place(relx=(0.02*(i-1)+0.01),rely=0.5)
            time.sleep(0.5)
            root.update()
        redbutton = Label(canvas, text=a[i], fg="red" ,bg="green",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        root.update()
        tc=tc+0.02
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            tkMessageBox.showinfo("error", "page fault")
            root.update()
            if page[x] != -1:
                min = 999
                for k in range(m):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(page[k] == a[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            page[x] = a[i]
            if cul[x]==0:
                cul[x]=1
            else:
                cul[x]=0
            x=(x+1)%m
            page_faults+=1
            #tkMessageBox.showinfo("error", "no page fault")
            root.update()
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    if cul[j]==0:
                        print page[j],
                        redbutton = Label(canvas, text=page[j], fg="red" ,bg="yellow",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                    else:
                        print page[j],
                        redbutton = Label(canvas, text=page[j], fg="red" ,bg="blue",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                else:
                    
                    if cul[j]==0:
                        print "-",
                        redbutton = Label(canvas, text="N", fg="red" ,bg="yellow",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                    else:
                        print "-",
                        redbutton = Label(canvas, text="N", fg="red" ,bg="blue",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            tkMessageBox.showinfo("error", "no page fault")
            root.update()
            
    print "\n Total page faults : %d." % (page_faults)
    var = StringVar()
    tkMessageBox.showinfo("error", "Total page faults : %d." % (page_faults))
    root.update
#Optimal Page Replacement Algorithm
def __optimal():
    global a,n,m
    x = 0
    var="What is Optimal page replacement algorithm?\nThe theoretically optimal page replacement algorithm is an algorithm that works as follows: when a page needs to be swapped in, the operating system swaps out the page whose next use will occur farthest in the future."
    tkMessageBox.showinfo("optimal", var)
    root.update
    page_faults = 0
    page = []
    flag1 = 0
    flag2 = 0
    flag3 = 0
    pos=0
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set(" ")
    label.pack()
    label.place(relx=0.3,rely=0.775)
    root.update  
    redbutton = Label(canvas, text="OPTIMAL", fg="black",height=15,width=30,bg="blue")
    redbutton.pack()
    redbutton.place(relx=0.2,rely=0)
    root.update()
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("Frames que")
    label.pack()
    label.place(relx=0.1,rely=0.6)
    root.update
    cul =[]
    for i in range(m):
        page.append(-1)
	cul.append(0)
    tc=0
    for i in range(n):
        redbutton = Label(canvas, text=a[i], fg="red",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        tc=tc+0.02
    for i in range(n,20):
        redbutton = Label(canvas, text=" ", fg="red",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        tc=tc+0.02

    tc=0
    for i in range(n):
        if i>0:
            redbutton = Label(canvas, text=a[i-1], fg="red" ,bg="yellow",height=1,width=4)
            redbutton.pack()
            redbutton.place(relx=(0.02*(i-1)+0.01),rely=0.5)
            time.sleep(0.5)
            root.update()
        redbutton = Label(canvas, text=a[i], fg="red" ,bg="green",height=1,width=4)
        redbutton.pack()
        redbutton.place(relx=tc+0.01,rely=0.5)
        root.update()
        tc=tc+0.02
        #print "\n"  
        flag1 = 0
        flag2 = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag1 = 1
                flag2 = 1
               
                break
            
        if flag1 == 0:
            for j in range(m):
                if(page[j] == -1):
                    page_faults+=1
                    page[j] =a[i]
                    if cul[j]==0:
                        cul[j]=1
                    else:
                        cul[j]=0
                    flag2 = 1
                    break
        
        if flag2 == 0:
            flag3 = 0
            temp = []                 
            for j in range(m):
               # print "%dass adf ktm  "% (page[j])
                temp.append(999)
               # print "xxxxx%d   "% (temp[j])
                for  k in range(i+1,n):
                    if(page[j] == a[k]):
                        temp[j] = k
                       # print "xxxxx%d   "% (temp[j])
                        break
            for j in range(m):
            	#print "i am executed\n"
                if(temp[j] == 999):
                   # print "i am executed\n"
                    pos = j
                    flag3 = 1
                    break
            if flag3 == 0:
                m1 = temp[0]
                pos = 0
                for j in range(1,m):
                    if(temp[j] > m1):
                        m1 = temp[j]
                        pos = j
                  
            page[pos] = a[i]
            if cul[j]==0:
                cul[j]=1
            else:
                cul[j]=0
            page_faults+=1
        tkMessageBox.showinfo("error", "page fault")
        
        print "\n%d ->" % (a[i]),
        for j in range(m):
                if page[j] != -1:
                    if cul[j]==0:
                        print page[j],
                        redbutton = Label(canvas, text=page[j], fg="red" ,bg="yellow",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        # time.sleep(0.35)
                        root.update()
                    else:
                        print page[j],
                        redbutton = Label(canvas, text=page[j], fg="red" ,bg="blue",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                else:
                    if cul[j]==0:
                        print "-",
                        redbutton = Label(canvas, text="N", fg="red" ,bg="yellow",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
                    else:
                        print "-",
                        redbutton = Label(canvas, text="N", fg="red" ,bg="blue",height=1,width=4)
                        redbutton.pack()
                        redbutton.place(relx=(0.02*(j-1)+0.1),rely=0.7)
                        #time.sleep(0.35)
                        root.update()
        if flag1==1:
             print "\n%d -> No Page Fault" % (a[i]),
             tkMessageBox.showinfo("error", "no page fault")
          
    print "\n Total page faults : %d." % (page_faults) 
    var = StringVar()
    #label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("\n Total page faults : %d." % (page_faults))
    tkMessageBox.showinfo("error", "Total page faults : %d." % (page_faults))
    
    #label.pack()
    #label.place(relx=0.3,rely=0.775)
    root.update               

  

print "\n SIMULATION OF PAGE REPLACEMENT ALGORITHM"

var = StringVar()
label = Message( root, textvariable=var,width=500,font=100)
var.set("select your choice")
label.pack()
label.place(relx=0.001,rely=0.1)
root.update
yellobutton = Button(canvas, text="accept", fg="black",bg="yellow",height=1,width=5,command=accept)
yellobutton.pack()
yellobutton.place(relx=(0.01),rely=0.15)
root.update()
yellobutton = Button(canvas, text="generate", fg="white",bg="black",height=1,width=5,command=generate)
yellobutton.pack()
yellobutton.place(relx=(0.01),rely=0.20)
root.update()
redbutton = Button(canvas, text="Fifo", fg="black",bg="red",height=1,width=5,command= __fifo)
redbutton.pack()
redbutton.place(relx=(0.01),rely=0.25)
root.update()
greenbutton = Button(canvas, text="lru", fg="black",bg="green",height=1,width=5,command=__lru )
greenbutton.pack()
greenbutton.place(relx=0.01,rely=0.30)
root.update()
bluebutton = Button(canvas, text="optimal", fg="black",bg="blue",height=1,width=5,command=__optimal )
bluebutton.pack()
bluebutton.place(relx=0.01,rely=0.35)
root.update()


    
root.mainloop()
