from tkinter import *

"""root = Tk()
root.title("test GUI")  #ตั้งชื่อ
#ข้อความ/สี/ขนาด/พื้นหลัง
myLabel1 = Label(root,text="HELLO JOJI",fg="red",font=20,bg="black").pack()
#myLabel2 = Label(text="Hi I love You").place(x=0,y=0)


def open():
    ss = Tk()     #จอที่2
    ss.title("show ")
    ss.geometry("400x200")



#ตำแหน่งของภาษาใช้  place(x=,y=) และ grid(row=,colum=) แทน.pack()
def show():
    print("Gogogogogogo")
def show22():
    Label(root,text="Hi I love You").pack()
def ss():
    Message = txt.get()
    Label(root,text=Message).pack()


#box
txt = StringVar()
txt2 = Entry(root,textvariable=txt).pack()


#ใส่ปุ่ม
bt1 = Button(root,text="Go",fg="white",bg="red",command=show22).pack()
bt2 = Button(root,text="SAVE",fg="white",bg="red",command=ss).pack()
bt3 = Button(root,text="SS",fg="white",bg="red",command=open).pack()
#ขนาดหน้าจอ
root.geometry("400x400")
root.mainloop()"""

root = Tk()
root. title("ProPro")
root.geometry("400x400")




#สร้างเมนู
my_menu = Menu()
root.config(menu=my_menu)

def open():
    ss = Tk()     #จอที่2
    ss.title("show ")
    ss.geometry("400x200")
def exitpro():
    root.destroy()


#เมนูย่อยitem
menu_item = Menu()
menu_item.add_command(label="new")
menu_item.add_command(label="open")
menu_item.add_command(label="About")
menu_item.add_command(label="exit",command=exitpro)
menu2 = Menu()
menu2.add_command(label="-open-",command=open)
#เพิ่มแทบเมนู
my_menu.add_cascade(label="A1",menu=menu_item)
my_menu.add_cascade(label="A2",menu=menu2)
my_menu.add_cascade(label="A3")



root.mainloop()