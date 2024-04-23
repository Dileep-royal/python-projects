#program to create simple calculator
from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry("350x400")
window.config(bg="orange")

#entry box
e=Entry(window,width=25,borderwidth=5,bg="lightyellow")
e.place(x=10,y=0)
#er=Entry(window,width=25,borderwidth=5,bg="lightyellow")
#er.place(x=120,y=360)

#function to edit
def edit():
    res=e.get()
    e.delete(len(res)-1)
#button to edit
b1=Button(window,text="X",width=12,bg="lightblue",command=edit)
b1.place(x=230,y=0)

#function to respond for buttons clicks
def click(num):
    res=e.get()
    e.delete(0,END)
    e.insert(0,str(res)+str(num))    
#buttons
b1=Button(window,text="1",width=12,bg="lightblue",command=lambda:click(1))
b1.place(x=10,y=60)
b1=Button(window,text="2",width=12,bg="lightblue",command=lambda:click(2))
b1.place(x=120,y=60)
b1=Button(window,text="3",width=12,bg="lightblue",command=lambda:click(3))
b1.place(x=230,y=60)
b1=Button(window,text="4",width=12,bg="lightblue",command=lambda:click(4))
b1.place(x=10,y=120)
b1=Button(window,text="5",width=12,bg="lightblue",command=lambda:click(5))
b1.place(x=120,y=120)
b1=Button(window,text="6",width=12,bg="lightblue",command=lambda:click(6))
b1.place(x=230,y=120)
b1=Button(window,text="7",width=12,bg="lightblue",command=lambda:click(7))
b1.place(x=10,y=180)
b1=Button(window,text="8",width=12,bg="lightblue",command=lambda:click(8))
b1.place(x=120,y=180)
b1=Button(window,text="9",width=12,bg="lightblue",command=lambda:click(9))
b1.place(x=230,y=180)
b1=Button(window,text="0",width=12,bg="lightblue",command=lambda:click(0))
b1.place(x=10,y=240)

#function for addition
def add():
    x=e.get()
    global op1,do
    do="add"
    e.delete(0,END)
    try:
      op1=int(x)
    except Exception:
        e.insert(0,"Enter Number")
#button to perform addition
b1=Button(window,text="+",width=12,bg="lightblue",command=add)
b1.place(x=120,y=240)

#function for substraction
def sub():
    x=e.get()
    global op1,do
    do="sub"
    e.delete(0,END)
    try:
      op1=int(x)
    except Exception:
      e.insert(0,"Enter Number")
#button to perform substraction
b1=Button(window,text="-",width=12,bg="lightblue",command=sub)
b1.place(x=230,y=240)

#function for division
def div():
    x=e.get()
    global op1,do
    do="div"
    e.delete(0,END)
    try:
      op1=int(x)
    except Exception:
        e.insert(0,"Enter Number")
#button to perform division
b1=Button(window,text="/",width=12,bg="lightblue",command=div)
b1.place(x=10,y=300)

#function for multiplication
def mul():
    x=e.get()
    global op1,do
    do="mul"
    e.delete(0,END)
    try:
      op1=int(x)
    except Exception:
        e.insert(0,"Enter Number")
#button to perform multiplication
b1=Button(window,text="*",width=12,bg="lightblue",command=mul)
b1.place(x=120,y=300)
#function to evaluate operand1 and operand2
def equal():
    op2=e.get()
    e.delete(0,END)
    try:
        if do=="add":
            e.insert(0,op1+int(op2))
        elif do=="sub":
            e.insert(0,op1-int(op2))
        elif do=="div":
            e.insert(0,op1/int(op2))
        elif do=="mul":
            e.insert(0,op1*int(op2))
    except Exception:
        e.insert(0,op1)
#button to perform evaluation
b1=Button(window,text="=",width=12,bg="lightblue",command=equal)
b1.place(x=230,y=300)
#function to clear the Entry
def clear():
    e.delete(0,END)
#button to clear
b1=Button(window,text="Clear",width=12,bg="lightgreen",command=clear)
b1.place(x=10,y=360)
window.mainloop()
