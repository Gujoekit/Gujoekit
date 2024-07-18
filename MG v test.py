from tkinter import *
from tkinter.filedialog import *  
from tkinter.colorchooser import *
import tkinter.messagebox

root = Tk()
root.title("Air Flow Calculate V.(test)")
root.geometry("400x400")
#-----------------------#
myLabel1 = Label(root,text="Air Flow Calculate",fg="blue",font=20).pack()
myLabel2 = Label(text="โปรแกรมคำนวณนี้เป็นการคำนวณ เบื้องต้นเท่านั้น").place(x=20,y=300)
myLabel3 = Label(text="ค่าความต่างอาจมีผลได้จาก สภาพพื้นที่ปิด-เปิด ช่องทางไหลของอากาศ และ สิ่งกั้น").place(x=20,y=320)
myLabel4 = Label(text="By Joji",fg="red").place(x=0,y=350)
def open():
    ss = Tk()     #จอที่2
    ss.title("show ")
    ss.geometry("400x200")
    te1 = Label(ss,text="กว้าง ยาว สูง").pack()
def open2():
    ss = Tk()     #จอที่3
    ss.title("show ")
    ss.geometry("400x200")
    te1 = Label(ss,text="54-42-36-25-20").pack()
def open3():
    ss = Tk()     #จอที่4
    ss.title("show ")
    ss.geometry("400x200")
    te1 = Label(ss,text="XXXXXXXXX").pack()
#ตำแหน่งของภาษาใช้  place(x=,y=) และ grid(row=,colum=) ใน.pack()
def T1():
    Message = txt.get()
    Label(root,text=Message).pack()
#box
txt = StringVar()
txt2 = Entry(root,textvariable=txt).place(x=100,y=55)
txt3 = Entry(root,textvariable=txt).place(x=100,y=105)
txt4 = Entry(root,textvariable=txt).place(x=100,y=155)

#ใส่ปุ่ม
bt1 = Button(root,text="ขนาดพื้นที่",fg="black",bg="white",command=open).place(x=20,y=50)
bt2 = Button(root,text="ขนาดพัดลม",fg="black",bg="white",command=open2).place(x=20,y=100)
bt3 = Button(root,text="จำนวนพัดลม",fg="black",bg="white",command=open3).place(x=20,y=150)



root.mainloop()
