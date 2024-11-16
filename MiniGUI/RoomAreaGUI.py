
from tkinter import *
root = Tk()
root.title("คำนวณค่าขนาดพื้นที่")
root.geometry("300x200")

A = StringVar()
Label(text='ความกว้าง(Width)',padx=10).grid(row=0,sticky=W)
et1=Entry(font=5,width=10,textvariable=A)
et1.grid(row=0,column=1)
Label(text='เมตร',padx=10).grid(row=0,column=2)

B = StringVar()
Label(text='ความยาว(Length)',padx=10).grid(row=1,sticky=W)
et2=Entry(font=5,width=10,textvariable=B)
et2.grid(row=1,column=1)
Label(text='เมตร',padx=10).grid(row=1,column=2)

C = StringVar()
Label(text='ความสูง(Height)',padx=10).grid(row=2,sticky=W)
et3=Entry(font=5,width=10,textvariable=C)
et3.grid(row=2,column=1)
Label(text='เมตร',padx=10).grid(row=2,column=2)

Label(text='ได้ขนาดพื้นที่ ',padx=10).grid(row=3,sticky=W)
et4=Entry(font=5,width=10)
et4.grid(row=3,column=1)
Label(text='ลูกบาศก์เมตร',padx=10).grid(row=3,column=2)

def CL():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)
    et4.delete(0,END)


def calculate():
    W = A.get()
    L = B.get()
    H = C.get()
    GG = [(W),(L),(H)]
    GG_float = [float(x)for x in GG]
    result1 = GG_float[0]*GG_float[1]*GG_float[2]
    raer = (f"{result1:.2f}")
    et4.insert(0,raer)


Button(text="ล้าง",width=10,command=CL).grid(row=4,sticky=W)
Button(text="คำนวณ",width=10,command=calculate).grid(row=4,column=1,sticky=E)


root.mainloop()
