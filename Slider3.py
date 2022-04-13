from tkinter import *
from PIL import Image,ImageTk  # to deal with images

class slider3:
         
    def __init__(self,root):
        self.root=root      #initialize root
        # self.lbl3=Label(self.root,text="Fest",font=("goudy old style",20),bd=0,relief=RAISED,bg="blue",fg="#000")
        # self.lbl3.place(x=400, y=530 ,width=50,height=50)

        img30=Image.open(r"Fest/1.jpg")
        img30=img30.resize((300,160),Image.ANTIALIAS) 
        self.img30=ImageTk.PhotoImage(img30)
        img31=Image.open(r"Fest/2.jpg")
        img31=img31.resize((300,160),Image.ANTIALIAS) 
        self.img31=ImageTk.PhotoImage(img31)
        img32=Image.open(r"Fest/3.jpg")
        img32=img32.resize((300,160),Image.ANTIALIAS) 
        self.img32=ImageTk.PhotoImage(img32)
        img33=Image.open(r"Fest/4.jpg")
        img33=img33.resize((300,160),Image.ANTIALIAS) 
        self.img33=ImageTk.PhotoImage(img33)
        img34=Image.open(r"Fest/5.jpg")
        img34=img34.resize((300,160),Image.ANTIALIAS) 
        self.img34=ImageTk.PhotoImage(img34)
        img35=Image.open(r"Fest/6.jpeg")
        img35=img35.resize((300,160),Image.ANTIALIAS) 
        self.img35=ImageTk.PhotoImage(img35)

        Frame_slider3=Frame(self.root)
        Frame_slider3.place(x=100,y=150,width=300,height=160)
        self.lbl30=Label(Frame_slider3,image=self.img30,bd=1)
        self.lbl30.place(x=0,y=0)
        self.lbl31=Label(Frame_slider3,image=self.img31,bd=1)
        self.lbl31.place(x=0,y=0)
        self.lbl32=Label(Frame_slider3,image=self.img32,bd=1)
        self.lbl32.place(x=0,y=0)
        self.lbl33=Label(Frame_slider3,image=self.img33,bd=1)
        self.lbl33.place(x=300,y=0)        
        self.lbl34=Label(Frame_slider3,image=self.img34,bd=1)
        self.lbl34.place(x=0,y=0)
        self.lbl35=Label(Frame_slider3,image=self.img35,bd=1)
        self.lbl35.place(x=300,y=0)
        self.x=300    
        # self.slider_func3()
        
 

    def slider_func3(self) :
        self.x-=1 
        if self.x==0:
            self.x=300
            self.new_img3=self.img30
            self.img30=self.img31
            self.img31=self.img32
            self.img32=self.img33
            self.img33=self.img34
            self.img34=self.img35
            self.img35=self.new_img3
            self.lbl30.config(image=self.img30)
            self.lbl31.config(image=self.img31)
            self.lbl32.config(image=self.img32)
            self.lbl33.config(image=self.img33)
            self.lbl34.config(image=self.img34)
            self.lbl35.config(image=self.img35)
        self.lbl35.place(x=self.x,y=0)
        self.lbl35.after(12,self.slider_func3)

# root=Tk()
# obj=slider3(root)
# root.mainloop()