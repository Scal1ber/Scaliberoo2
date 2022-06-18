import math
from tkinter import *
from tkinter.ttk import *

class tugiac():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
class tugiac1(tugiac):
    def chuvi1(self):
        return self.a + self.b + self.c + self.d
    def max1(self):
        return max([self.a,self.b,self.c,self.d])
class tugiac2(tugiac):
    def chuvi2(self):
        return self.a + self.b + self.c + self.d
    def max2(self):
        return max([self.a,self.b,self.c,self.d])
class tugiac3(tugiac):
    def chuvi3(self):
        return self.a + self.b + self.c + self.d
    def max3(self):
        return max([self.a,self.b,self.c,self.d])

def sel():
    if(var.get()==1):
        txt.configure(text="Ban chon hinh tu giac 1")
        canh1.configure(text="Nhap canh  1:")
        nhap_canh1= Entry(window, textvariable = text1)
        nhap_canh1.grid(column=1, row=5)
        canh2.configure(text="Nhap canh  2:")
        nhap_canh2= Entry(window, textvariable = text2)
        nhap_canh2.grid(column=1, row=6)
        canh3.configure(text="Nhap canh 3:")
        nhap_canh3= Entry(window, textvariable = text3)
        nhap_canh3.grid(column=1, row=7)
        canh4.configure(text="Nhap canh 4:")
        nhap_canh4= Entry(window, textvariable = text4)
        nhap_canh4.grid(column=1, row=8)
    elif(var.get()==2):
        txt.configure(text="Ban chon hinh tu giac 2")
        canh1.configure(text="Nhap canh 1:")
        nhap_canh1= Entry(window, textvariable = text1)
        nhap_canh1.grid(column=1, row=5)
        canh2.configure(text="Nhap canh 2:")
        nhap_canh2= Entry(window, textvariable = text2)
        nhap_canh2.grid(column=1, row=6)
        canh3.configure(text="Nhap canh 3:")
        nhap_canh3= Entry(window, textvariable = text3)
        nhap_canh3.grid(column=1, row=7)
        canh4.configure(text="Nhap canh 4:")
        nhap_canh4= Entry(window, textvariable = text4)
        nhap_canh4.grid(column=1, row=8)
    else:
        txt.configure(text="Ban chon hinh tu giac 3")
        canh1.configure(text="Nhap canh 1:")
        nhap_canh1= Entry(window, textvariable = text1)
        nhap_canh1.grid(column=1, row=5)
        canh2.configure(text="Nhap canh 2:")
        nhap_canh2= Entry(window, textvariable = text2)
        nhap_canh2.grid(column=1, row=6)
        canh3.configure(text="Nhap canh 3:")
        nhap_canh3= Entry(window, textvariable = text3)
        nhap_canh3.grid(column=1, row=7)
        canh4.configure(text="Nhap canh 4:")
        nhap_canh4= Entry(window, textvariable = text4)
        nhap_canh4.grid(column=1, row=8)

def tinh():
    a = int(text1.get())
    b = int(text2.get())
    c = int(text3.get())
    d = int(text4.get())

    if(var.get()==1):
        ob = tugiac1(a,b,c,d)
        prt_cv1.configure(text="Chu vi tu giac 1 la: "+str(ob.chuvi1()))
        prt_dd1.configure(text="Do dai canh tu giac 1 lon nhat la: "+str(ob.max1()))
    elif(var.get()==2):
        ob = tugiac2(a,b,c,d)
        prt_cv2.configure(text="Chu vi tu giac 2 la: "+str(ob.chuvi2()))
        prt_dd2.configure(text="Do dai canh tu giac 2 lon nhat la: "+str(ob.max2()))
    else:
        ob = tugiac3(a,b,c,d)
        prt_cv3.configure(text="Chu vi tu giac 3 la: "+str(ob.chuvi3()))
        prt_dd3.configure(text="Do dai canh tu giac 3 lon nhat la: "+str(ob.max3()))

    
window = Tk()
window.title("Tinh toan chu vi dien tich tam giac")
window.geometry("1080x1080")
var = IntVar()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
txt = Label(window, text ="Hay chon hinh de tinh")
txt.grid(column=2, row=4)
canh1 = Label(window)
canh1.grid(column=0,row=5)
canh2 = Label(window)
canh2.grid(column=0,row=6)
canh3 = Label(window)
canh3.grid(column=0,row=7)
canh4 = Label(window)
canh4.grid(column=0,row=8)
prt_cv1 = Label(window)
prt_cv1.grid(column=1, row=10)
prt_dd1 = Label(window)
prt_dd1.grid(column=1, row=11)

prt_cv2 = Label(window)
prt_cv2.grid(column=1, row=12)
prt_dd2 = Label(window)
prt_dd2.grid(column=1, row=13)

prt_cv3 = Label(window)
prt_cv3.grid(column=1, row=14)
prt_dd3 = Label(window)
prt_dd3.grid(column=1, row=15)


Radiobutton(window, text = "Tu giac 1", variable = var, value = 1, command = sel).grid(column=0, row=0)
Radiobutton(window, text = "Tu giac 2", variable = var, value = 2, command = sel).grid(column=0, row=1)
Radiobutton(window, text = "Tu giac 3", variable = var, value = 3, command = sel).grid(column=0, row=3)
Button(window, text = "Tinh", command = tinh).grid(column=1, row=9)
window.mainloop()
