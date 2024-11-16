from tkinter import *
from tkinter import font
from cgitb import text
from googletrans import Translator


def translate():
    Message = text1.get(1.0,'end-1c')
    translator = Translator()
    output = translator.translate(text=Message,src='en',dest='th')
    text2.insert('end',output.text)


def ree():
    text1.delete(1.0,'end')
    text2.delete(1.0,'end')


#size
root = Tk()
root.title("DitET Translate Mini")
root.geometry('400x300')
root.maxsize(400,300)
root.minsize(400,300)

#widget
label=Label(text="English To Thai",font=('Arial',20,'bold'))
label.place(x=100,y=10)

#inputE
text1 = Text(root,width=30,height=10)
text1.place(x=4,y=70)


#inputT
text2 = Text(root,width=30,height=10)
text2.place(x=200,y=70)

#button
bt1 = Button(root,text="แปลภาษา",command=translate)
bt2 = Button(root,text="ล้าง",command=ree)
bt2.place(x=230,y=240)#ล้าง
bt1.place(x=140,y=240)#แปล

root.mainloop()