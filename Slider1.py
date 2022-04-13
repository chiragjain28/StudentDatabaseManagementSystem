from tkinter import *
from PIL import Image,ImageTk  # to deal with images

class slider1:
         
    def __init__(self,root):
        self.root=root      #initialize root
        

        img10=Image.open(r"Class/1.jpg")
        img10=img10.resize((300,160),Image.ANTIALIAS) 
        self.img10=ImageTk.PhotoImage(img10)
        img11=Image.open(r"Class/2.jpg")
        img11=img11.resize((300,160),Image.ANTIALIAS) 
        self.img11=ImageTk.PhotoImage(img11)
        img12=Image.open(r"Class/3.jpg")
        img12=img12.resize((300,160),Image.ANTIALIAS) 
        self.img12=ImageTk.PhotoImage(img12)
        img13=Image.open(r"Class/4.jpg")
        img13=img13.resize((300,160),Image.ANTIALIAS) 
        self.img13=ImageTk.PhotoImage(img13)
        Frame_slider4=Frame(self.root)
        Frame_slider4.place(x=100,y=400,width=300,height=160)
        self.lbl10=Label(Frame_slider4,image=self.img10,bd=1)
        self.lbl10.place(x=0,y=0)
        self.lbl11=Label(Frame_slider4,image=self.img11,bd=1)
        self.lbl11.place(x=0,y=0)
        self.lbl12=Label(Frame_slider4,image=self.img12,bd=1)
        self.lbl12.place(x=0,y=0)
        self.lbl13=Label(Frame_slider4,image=self.img13,bd=1)
        self.lbl13.place(x=300,y=0)        
        self.x=300    
    #    self.slider_func1()
            

        
 

    def slider_func1(self) :
        self.x-=1 
        if self.x==0 :
            self.x=300
            #=============Swap==============#
            self.new_img1=self.img10 
            self.img10=self.img11
            self.img11=self.img12
            self.img12=self.img13
            self.img13=self.new_img1
            self.lbl10.config(image=self.img10)
            self.lbl11.config(image=self.img11)
            self.lbl12.config(image=self.img12)
            self.lbl13.config(image=self.img13)

        self.lbl13.place(x=self.x,y=0)
        self.lbl13.after(12,self.slider_func1)


# root=Tk()
# obj=slider1(root)
# root.mainloop()



