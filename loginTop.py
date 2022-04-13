from tkinter import *
# from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image,ImageTk  # to deal with images
import os
# import face_recognition
# import cv2
from tkinter import ttk,messagebox
import numpy as np


class top_Class:     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Face Recognition")
        self.root.geometry("420x420+435+130")  #width x height + x axis(left corner) + top position
        self.root.config(bg="black")
        #==== Title =====#

        self.bg_img=Image.open("images/face6.jpg")
        self.bg_img=self.bg_img.resize((420,420),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.title=Label(self.root,bg="gray9",fg="white",image=self.bg_img).place(relwidth=1,relheight=1)

        self.strt=Image.open("images/start2.jpg")
        self.strt=self.strt.resize((70,40),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.strt=ImageTk.PhotoImage(self.strt)
        strt=Button(self.root,bd=1,relief=RAISED,image=self.strt,command=self.func).place(x=165,y=315,width=70,height=40)
        lbl=Label(self.root,text="Please Wait.. This may take a while",font=("georgia",13,"italic"),fg="white",bg="black").place(x=70,y=380)
        # self.wait=Image.open("images/wait1.jpg")
        # self.wait=self.wait.resize((350,70),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        # self.wait=ImageTk.PhotoImage(self.wait)
        # lbl=Label(self.root,image=self.wait).place(x=30,y=130,width=350,height=70)
        # quit=Button(self.root,text="Quit",font=("georgia",13,"italic"),fg="white",bg="black",command=self.root.destroy).place(x=150,y=100,width=100)
    def func(self):
        os.system('python recognition.py')
        self.root.destroy()
        os.system("python dashboard.py")
       
if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=top_Class(root)     #create object of RMS class and pass root obj
    root.mainloop()