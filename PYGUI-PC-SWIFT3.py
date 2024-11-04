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

#box
txt2 = Label(text="กรุณาป้อนค่า",fg="black").place(x=99,y=55)
txt3 = Label(text="รอคำนวณ",fg="black").place(x=99,y=105)
txt4 = Label(text="รอคำนวณ",fg="black").place(x=99,y=155)

    
def open():
    import tkinter.ttk 
    import tkinter.filedialog
    import tkinter.messagebox
    ss = Tk()
    ss.title("ขนาดพื้นที่")
    ss.geometry("250x200")

    WidthW = IntVar()
    WidthW = Label(ss,text="กว้าง").grid(row=0,column=0)
    et1=Entry(ss,textvariable=WidthW)
    et1.grid(row=0,column=1)

    LongL = IntVar()
    LongL = Label(ss,text="ยาว").grid(row=1,column=0)
    et2=Entry(ss,textvariable=LongL)
    et2.grid(row=1,column=1)

    Heigh = IntVar()
    Heigh = Label(ss,text="สูง").grid(row=2,column=0)
    et3=Entry(ss,textvariable=Heigh)
    et3.grid(row=2,column=1)

    SSs = Label(ss,text="ได้พื้นที่ขนาด").grid(row=3,column=0)
    et4 = Entry(ss,textvariable="ผลรวมที่จะได้")
    et4.grid(row=3,column=1)

    def deleteText():
        et1.delete(0,END)
        et2.delete(0,END)
        et3.delete(0,END)
        et4.delete(0,END)
    button = Button(ss,text="ลบ",command=deleteText).grid(row=4,column=2)
    button2 = Button(ss,text="คำนวน",command="").grid(row=4,column=1)
    

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



#ใส่ปุ่ม
bt1 = Button(root,text="ขนาดพื้นที่",fg="black",bg="white",command=open).place(x=20,y=50)
bt2 = Button(root,text="ขนาดพัดลม",fg="black",bg="white",command=open2).place(x=20,y=100)
bt3 = Button(root,text="จำนวนพัดลม",fg="black",bg="white",command=open3).place(x=20,y=150)



root.mainloop()
