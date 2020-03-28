from tkinter import *

def add():
      s1=e1.get()
      s2=e2.get()
      try:
            if s1=="" and s2=="":
                  err.set("No input")
            else:
                  x=int(s1)
                  y=int(s2)
                  z=x+y
                  res.set(str(z))
      except ValueError:
            err.set("Invalid input")
      return


def subs():
      s1=e1.get()
      s2=e2.get()
      try:
            if s1=="" and s2=="":
                  err.set("No input")
            else:
                  x=int(s1)
                  y=int(s2)
                  z=x-y
                  res.set(str(z))
      except ValueError:
            err.set("Invalid input")
      return


def mul():
      s1=e1.get()
      s2=e2.get()
      try:
            if s1=="" and s2=="":
                  err.set("No input")
            else:
                  x=int(s1)
                  y=int(s2)
                  z=x*y
                  res.set(str(z))
      except ValueError:
            err.set("Invalid input")
      return

def divide():
      s1=e1.get()
      s2=e2.get()
      try:
            if s1=="" and s2=="":
                  err.set("No input")
            else:
                  x=int(s1)
                  y=int(s2)
                  z=x/y
                  res.set(str(z))
      except ValueError:
            err.set("Invalid input")
      return




window=Tk()
window.title("Calculator")
window.configure(background="Cyan")
window.geometry("500x400")

err=StringVar()
res=StringVar()

l1=Label(window,text="Enter No 1.",font="Times 30",fg="blue",bg="cyan")
e1=Entry(window,font="Times 20")

l2=Label(window,text="Enter No 2.",font="Times 30",fg="blue",bg="cyan")
e2=Entry(window,font="Times 20")

l3=Label(window,text="Result:",font="Times 30",fg="blue",bg="cyan")
e3=Entry(window,textvariable=res,font="Times 20")

l4=Label(window,textvariable=err,font="Times 20",fg="red",bg="cyan")

b1=Button(window,text="+",command=add,font="Times 20",bg="lightgreen")
b2=Button(window,text="-",command=subs,font="Times 20",bg="yellow")
b3=Button(window,text="/",command=divide,font="Times 20",bg="red")
b4=Button(window,text="x",command=mul,font="Times 20",bg="blue")

l1.grid(row=0,column=1)
e1.grid(row=1,column=1)
l2.grid(row=2,column=1)
e2.grid(row=3,column=1)
l3.grid(row=4,column=1)
e3.grid(row=5,column=1)

b1.place(x=300,y=60)
b2.place(x=350,y=60)
b3.place(x=400,y=60)
b4.place(x=450,y=60)
l4.place(x=330,y=200)
