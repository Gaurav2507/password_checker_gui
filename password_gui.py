from tkinter import *

def ok():
    pwd=e1.get()
    file=open("password.txt",'r')

    k=file.read()

    file.close()
    if pwd==k:
        print("Correct Password")
    else:
        print("Wrong Password")
        print(pwd)
def ok1():
    pwd1=e2.get()
    pwd2=e3.get()

    if pwd1==pwd2:
        file=open("password.txt",'w')
        file.write(pwd1)
        file.close()
        print("Password matched and Details updated")
    else:
        print("password did not match")
        
    
def login():
    
    lButton.grid_forget()
    sButton.grid_forget()
    label.grid_forget()

    label1=Label(root,text="Enter your password")    
    button_ok=Button(root,text="OK",command=ok)

    label1.grid(row=0,column=0)
    e1.grid(row=0,column=1)
    button_ok.grid(row=1,column=0)


def signup():
    lButton.grid_forget()
    sButton.grid_forget()
    label.grid_forget()

    label1=Label(root,text="Enter new password")
    label2=Label(root,text="Confirm Password")

    label1.grid(row=0,column=0)
    e2.grid(row=0,column=1)
    label2.grid(row=1,column=0)
    e3.grid(row=1,column=1)
   
    button_ok=Button(root,text="OK",command=ok1)
    button_ok.grid(row=2,column=0)
    

root=Tk()
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
label=Label(root,text="Hello! Welcome")
label.grid(row=0,column=1)

lButton=Button(root,text="login",command=login)
sButton=Button(root,text="signup",command=signup)


lButton.grid(row=1,column=0)
sButton.grid(row=1,column=1)

root.mainloop()
