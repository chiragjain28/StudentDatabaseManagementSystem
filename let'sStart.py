import sqlite3
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3
import os
import io

class Register:     
    def __init__(self,root):  # pass root which is object of Tk
        self.root=root      #initialize root
        self.root.title("IMPOSTERS")
        self.root.geometry("1350x700+0+0")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        self.root.focus_force()

        

        self.bg_img=Image.open(r"images/StartBg17.png")
        self.bg_img=self.bg_img.resize((1350,700),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.bg_img=ImageTk.PhotoImage(self.bg_img)   # again open image bcz it resize image during runtime and 
         #  dont define (file='path') coz we dont know the path of resized image
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=0,y=0)

        # title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",
        # font=("goudy old style",25,"bold"),bg="lightcyan",fg="gray9").place(x=370, y=400 ,width=650,height=70)

if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=Register(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen