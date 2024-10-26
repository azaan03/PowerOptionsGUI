from tkinter import *
from tkinter import messagebox
import os

def restart():
    if messagebox.askyesno("Confirmation","Are you Sure You Want to Restart "):
        os.system("shutdown /r /t 1")
def restart_time():
    if messagebox.askyesno("Confirmation","Are you Sure You Want to Restart in 20 sec"):
        os.system("shutdown /r /t 20")
def lgout():
    if messagebox.askyesno("Confirmation","Are you Sure You Want to Logout"):
        os.system("shutdown -l")
def shutdown():
    if messagebox.askyesno("Confirmation","Are you Sure You Want to Shutdown"):
        os.system("shutdown /s /t 1")
    
st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button=Button(st,text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart,fg="Red")
r_button.place(x=150,y=70,height=50,width=200)

rt_button=Button(st,text="Restart Time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time,fg="Black")
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="LogOut",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=lgout,fg="Blue")
lg_button.place(x=150,y=270,height=50,width=200)

std_button=Button(st,text="Shut Down",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown,fg="Brown")
std_button.place(x=150,y=370,height=50,width=200)


st.mainloop()