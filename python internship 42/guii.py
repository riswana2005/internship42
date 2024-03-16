# from tkinter import*
# root=Tk()
# root.mainloop()

# from tkinter import*


# run=Tk()
# run.mainloop()

# from tkinter import*
# root=Tk()
# root.title("welcome to python lobby")
# root.geometry("300x200")
# root.mainloop()
# from tkinter import*
# root=Tk()
# root.title("welcome to python lobby")
# root.geometry("200x250")
# lbl=Label(root,text="we are python lobby-ian")
# lbl.pack()
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.title("welcome to python loop")
# root.geometry("250x250")
# lbl=Label(root,text='my name is affin',font=("helvetica",12),fg='white',bg='black')
# lbl.pack()

# root.mainloop()

# from tkinter import*
# root=Tk()

# root.title("welcome to python lobby")
# def clicked():
#     print(" am iclicked")
# btn=Button(root,text="click me",command=clicked)
# btn.pack()
# root.geometry('250x200')
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.title("welcom to python lobby")
# root.geometry("250x200")
# entry=Entry(root,bg="yellow",fg="red",bd=5)
# entry.pack()
# root.mainloop()


# from tkinter import*
# root=Tk()
# root.title("welcome to python lobby")
# root.geometry("250x200")
# entry=Entry(root,bg="yellow",fg="red",bd=5)
# entry.pack()
# root.mainloop()

# CHECK BUTTON
# from tkinter import*
# root=Tk()
# root.title("pythonlobby")
# w=Label(root,text='pythonlobby.com',font="60")
# w.pack()
# Checkbox1=IntVar()
# Checkbox2=IntVar()
# Button0=Checkbutton(root,text="learning",
#                      variable=Checkbox1,
#                     onvalue=1,
#                     offvalue=0,
#                     height=3,
#                     width=12)
# Button1=Checkbutton(root,text="tutorial",
#                     variable=Checkbox2,
#                     onvalue=1,
#                     offvalue=0,
#                     height=3,
#                     width=12)
# Button0.pack()
# Button1.pack()
# root.geometry("320x320")
# mainloop()


# RADIOBUTTON
from tkinter import*
root=Tk()
root.title("PythonLobby")
value1=StringVar(root,"2")
rbtn1=Radiobutton(root,text="Radio Button1",variable=value1,valu="1")
rbtn1.pack()
rbtn2=Radiobutton(root,text="Radio Button2",variable=value1,value="2")
rbtn2.pack()
rbtn3=Radiobutton(root,text="Radio Button3",variable=value1,value="3")
rbtn3.pack()
root.geometry("250x200")
mainloop()

