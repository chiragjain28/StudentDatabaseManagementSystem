from tkinter import *
from PIL import Image,ImageTk 
class slider2 :   
    def __init__(self,root):
            #initialize root
        self.root=root

        # 2 Block

        img1=Image.open(r"Sports/1.jpg")
        img1=img1.resize((300,160),Image.ANTIALIAS) 
        self.img1=ImageTk.PhotoImage(img1)
        img2=Image.open(r"Sports/2.jpg")
        img2=img2.resize((300,160),Image.ANTIALIAS) 
        self.img2=ImageTk.PhotoImage(img2)
        img3=Image.open(r"Sports/3.jpg")
        img3=img3.resize((300,160),Image.ANTIALIAS) 
        self.img3=ImageTk.PhotoImage(img3)
        img4=Image.open(r"Sports/4.jpg")
        img4=img4.resize((300,160),Image.ANTIALIAS) 
        self.img4=ImageTk.PhotoImage(img4)
        img5=Image.open(r"Sports/5.jpg")
        img5=img5.resize((300,160),Image.ANTIALIAS) 
        self.img5=ImageTk.PhotoImage(img5)
        img6=Image.open(r"Sports/6.jpg")
        img6=img6.resize((300,160),Image.ANTIALIAS) 
        self.img6=ImageTk.PhotoImage(img6)

        Frame_slider2=Frame(self.root)
        Frame_slider2.place(x=900,y=150,width=300,height=160)

        self.lbl1=Label(Frame_slider2,image=self.img1,bd=1)
        self.lbl1.place(x=0,y=0)
        self.lbl2=Label(Frame_slider2,image=self.img2,bd=1)
        self.lbl2.place(x=0,y=0)
        self.lbl3=Label(Frame_slider2,image=self.img3,bd=1)
        self.lbl3.place(x=0,y=0)
        self.lbl4=Label(Frame_slider2,image=self.img4,bd=1)
        self.lbl4.place(x=0,y=0)
        self.lbl5=Label(Frame_slider2,image=self.img5,bd=1)
        self.lbl5.place(x=0,y=0)
        self.lbl6=Label(Frame_slider2,image=self.img6,bd=1)
        self.lbl6.place(x=300,y=0)
        self.x=300       
        #self.slider_func2()
        

    def slider_func2(self) :
        self.x-=1
        
        if self.x==0:
            self.x=300
            self.new_img1=self.img1
            self.img1=self.img2
            self.img2=self.img3
            self.img3=self.img4
            self.img4=self.img5
            self.img5=self.img6
            self.img6=self.new_img1
            self.lbl1.config(image=self.img1)
            self.lbl2.config(image=self.img2)
            self.lbl3.config(image=self.img3)
            self.lbl4.config(image=self.img4)
            self.lbl5.config(image=self.img5)
            self.lbl6.config(image=self.img6)
        self.lbl6.place(x=self.x,y=0)
        self.lbl6.after(12,self.slider_func2)


# root=Tk()
# obj=slider2(root)
# root.mainloop()