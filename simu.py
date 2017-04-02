from Tkinter import *
import tkMessageBox
import time
import random
import Tkinter
root = Tk()
WIDTH = 800
HEIGHT = 600
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
root.title("Page replacement")
canvas.pack()


a = []

#Function to accept reference string and frame size.
def accept():
    window = Tk()
    WIDTH = 800
HEIGHT = 600
    def close_window(): 
        window.destroy()

    frame = Frame(window, width=WIDTH, height=HEIGHT)
    frame.pack()
    kutton = Button (frame, text = "Good-bye.", command = close_window)
    kutton.pack()

    window.mainloop()



def generate():
    redbutton = Button(canvas, text="Accepting", fg="red",height=15,width=30,bg="yellow")
    redbutton.pack()
    redbutton.place(relx=0.5,rely=0)
    root.update()
    tc=0
    global a,n,m
    n =20
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("page que")
    label.pack()
    label.place(relx=0.4,rely=0.425)
    root.update 
    for i in range(n):
        t = random.randrange(0,10)
        a.append(t)
        redbutton = Button(canvas, text=a[i], fg="red",height=1,width=1)
        redbutton.pack()
        redbutton.place(relx=tc+0.1,rely=0.5)
        tc=tc+0.04
    m = 3
    root.update()  
#First In First Out Page Replacement Algorithm
def __fifo():
    global a,n,m
    f = -1
    page_faults = 0
    page = []
    fu=0
    cul= []
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set(" ")
    label.pack()
    label.place(relx=0.3,rely=0.775)
    root.update  
    redbutton = Button(canvas, text="FIFO", fg="black",height=15,width=30,bg="red")
    redbutton.pack()
    redbutton.place(relx=0.5,rely=0)
    root.update()
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("Frames que")
    label.pack()
    label.place(relx=0.4,rely=0.6)
    root.update     
    for i in range(m):
        page.append(-1)
        cul.append(0)
    tc=0
    for i in range(n):
        redbutton = Button(canvas, text=a[i], fg="red",height=1,width=1)
        redbutton.pack()
        redbutton.place(relx=tc+0.1,rely=0.5)
        tc=tc+0.04
    tc=0
    for i in range(n):
        if i>0:
            redbutton = Button(canvas, text=a[i-1], fg="red" ,bg="yellow",height=1,width=1)
            redbutton.pack()
            redbutton.place(relx=(0.04*(i-1)+0.1),rely=0.5)
            time.sleep(0.5)
            root.update()
        redbutton = Button(canvas, text=a[i], fg="red" ,bg="green",height=1,width=1)
        redbutton.pack()
        redbutton.place(relx=tc+0.1,rely=0.5)
        root.update()
        tc=tc+0.04
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%m
            page[f] = a[i]
            page_faults+=1
            redbutton = Button(canvas, text="page fault", fg="red",height=1,width=60 )
            redbutton.pack()
            redbutton.place(relx=0.1,rely=0.9)
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
                        redbutton = Button(canvas, text=page[j], fg="red" ,bg="yellow",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                    else:
                        print page[j],
                        redbutton = Button(canvas, text=page[j], fg="red" ,bg="blue",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                else:
                    if cul[j]==0:
                        print "-",
                        redbutton = Button(canvas, text="N", fg="red" ,bg="yellow",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                    else:
                        print "-",
                        redbutton = Button(canvas, text="N", fg="red" ,bg="blue",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            redbutton = Button(canvas, text="no page fault", fg="red",height=1,width=60 )
            redbutton.pack()
            redbutton.place(relx=0.1,rely=0.9)
            root.update()
    print "\n Total page faults : %d." % (page_faults)
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("\n Total page faults : %d." % (page_faults))
    label.pack()
    label.place(relx=0.3,rely=0.775)
    root.update 
#Least Recently Used Page Replacement Algorithm
def __lru():
    global a,n,m
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
    redbutton = Button(canvas, text="LRU", fg="black",height=15,width=30,bg="green")
    redbutton.pack()
    redbutton.place(relx=0.5,rely=0)
    root.update()
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("Frames que")
    label.pack()
    label.place(relx=0.4,rely=0.6)
    root.update
    for i in range(m):
        page.append(-1)
        cul.append(0)
        
    tc=0
    for i in range(n):
        redbutton = Button(canvas, text=a[i], fg="red",height=1,width=1)
        redbutton.pack()
        redbutton.place(relx=tc+0.1,rely=0.5)
        tc=tc+0.04
    tc=0
    for i in range(n):
        flag = 0
        if i>0:
            redbutton = Button(canvas, text=a[i-1], fg="red" ,bg="yellow",height=1,width=1)
            redbutton.pack()
            redbutton.place(relx=(0.04*(i-1)+0.1),rely=0.5)
            time.sleep(0.5)
            root.update()
        redbutton = Button(canvas, text=a[i], fg="red" ,bg="green",height=1,width=1)
        redbutton.pack()
        redbutton.place(relx=tc+0.1,rely=0.5)
        root.update()
        tc=tc+0.04
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            redbutton = Button(canvas, text="page fault", fg="red",height=1,width=60 )
            redbutton.pack()
            redbutton.place(relx=0.1,rely=0.9)
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
            redbutton = Button(canvas, text="page fault", fg="red",height=1,width=60 )
            redbutton.pack()
            redbutton.place(relx=0.1,rely=0.9)
            root.update()
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    if cul[j]==0:
                        print page[j],
                        redbutton = Button(canvas, text=page[j], fg="red" ,bg="yellow",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                    else:
                        print page[j],
                        redbutton = Button(canvas, text=page[j], fg="red" ,bg="blue",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                else:
                    
                    if cul[j]==0:
                        print "-",
                        redbutton = Button(canvas, text="N", fg="red" ,bg="yellow",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                    else:
                        print "-",
                        redbutton = Button(canvas, text="N", fg="red" ,bg="blue",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            redbutton = Button(canvas, text="no page fault", fg="red",height=1,width=60 )
            redbutton.pack()
            redbutton.place(relx=0.1,rely=0.9)
            root.update()
            
    print "\n Total page faults : %d." % (page_faults)
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("\n Total page faults : %d." % (page_faults))
    label.pack()
    label.place(relx=0.3,rely=0.775)
    root.update
#Optimal Page Replacement Algorithm
def __optimal():
    global a,n,m
    x = 0
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
    redbutton = Button(canvas, text="OPTIMAL", fg="black",height=15,width=30,bg="blue")
    redbutton.pack()
    redbutton.place(relx=0.5,rely=0)
    root.update()
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("Frames que")
    label.pack()
    label.place(relx=0.4,rely=0.6)
    root.update
    cul =[]
    for i in range(m):
        page.append(-1)
	cul.append(0)
    tc=0
    for i in range(n):
        redbutton = Button(canvas, text=a[i], fg="red",height=1,width=1)
        redbutton.pack()
        redbutton.place(relx=tc+0.1,rely=0.5)
        tc=tc+0.04
    tc=0
    for i in range(n):
        if i>0:
            redbutton = Button(canvas, text=a[i-1], fg="red" ,bg="yellow",height=1,width=1)
            redbutton.pack()
            redbutton.place(relx=(0.04*(i-1)+0.1),rely=0.5)
            time.sleep(0.5)
            root.update()
        redbutton = Button(canvas, text=a[i], fg="red" ,bg="green",height=1,width=1)
        redbutton.pack()
        redbutton.place(relx=tc+0.1,rely=0.5)
        root.update()
        tc=tc+0.04
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
        redbutton = Button(canvas, text="page fault", fg="red",height=1,width=60 )
        redbutton.pack()
        redbutton.place(relx=0.1,rely=0.9)
        root.update()
        print "\n%d ->" % (a[i]),
        for j in range(m):
                if page[j] != -1:
                    if cul[j]==0:
                        print page[j],
                        redbutton = Button(canvas, text=page[j], fg="red" ,bg="yellow",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                    else:
                        print page[j],
                        redbutton = Button(canvas, text=page[j], fg="red" ,bg="blue",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                else:
                    if cul[j]==0:
                        print "-",
                        redbutton = Button(canvas, text="N", fg="red" ,bg="yellow",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
                    else:
                        print "-",
                        redbutton = Button(canvas, text="N", fg="red" ,bg="blue",height=1,width=1)
                        redbutton.pack()
                        redbutton.place(relx=(0.04*(j-1)+0.45),rely=0.7)
                        time.sleep(0.35)
                        root.update()
        if flag1==1:
             print "\n%d -> No Page Fault" % (a[i]),
             redbutton = Button(canvas, text="no page fault", fg="red",height=1,width=60 )
             redbutton.pack()
             redbutton.place(relx=0.1,rely=0.9)
             root.update()
    print "\n Total page faults : %d." % (page_faults) 
    var = StringVar()
    label = Message( root, textvariable=var,width=500,font=100,pady=10)
    var.set("\n Total page faults : %d." % (page_faults))
    label.pack()
    label.place(relx=0.3,rely=0.775)
    root.update               

  

print "\n SIMULATION OF PAGE REPLACEMENT ALGORITHM"

var = StringVar()
label = Message( root, textvariable=var,width=500,font=100)
var.set("select your choice")
label.pack()
label.place(relx=0.05,rely=0.1)
root.update
yellobutton = Button(canvas, text="accept", fg="black",bg="yellow",height=1,width=5,command=accept)
yellobutton.pack()
yellobutton.place(relx=(0.1),rely=0.15)
root.update()
yellobutton = Button(canvas, text="generate", fg="white",bg="black",height=1,width=5,command=generate)
yellobutton.pack()
yellobutton.place(relx=(0.1),rely=0.20)
root.update()
redbutton = Button(canvas, text="Fifo", fg="black",bg="red",height=1,width=5,command= __fifo)
redbutton.pack()
redbutton.place(relx=(0.1),rely=0.25)
root.update()
greenbutton = Button(canvas, text="lru", fg="black",bg="green",height=1,width=5,command=__lru )
greenbutton.pack()
greenbutton.place(relx=0.1,rely=0.30)
root.update()
bluebutton = Button(canvas, text="optimal", fg="black",bg="blue",height=1,width=5,command=__optimal )
bluebutton.pack()
bluebutton.place(relx=0.1,rely=0.35)
root.update()


    
root.mainloop()
