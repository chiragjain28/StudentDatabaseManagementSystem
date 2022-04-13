from tkinter import *
from PIL import Image,ImageTk  # to deal with images

class slider4:
         
    def __init__(self,root):
        self.root=root      #initialize root

        img40=Image.open(r"Hostel/1.jpg")
        img40=img40.resize((300,160),Image.ANTIALIAS) 
        self.img40=ImageTk.PhotoImage(img40)
        img41=Image.open(r"Hostel/2.jpg")
        img41=img41.resize((300,160),Image.ANTIALIAS) 
        self.img41=ImageTk.PhotoImage(img41)
        img42=Image.open(r"Hostel/3.jpg")
        img42=img42.resize((300,160),Image.ANTIALIAS) 
        self.img42=ImageTk.PhotoImage(img42)
        img43=Image.open(r"Hostel/4.jpg")
        img43=img43.resize((300,160),Image.ANTIALIAS) 
        self.img43=ImageTk.PhotoImage(img43)
        Frame_slider4=Frame(self.root)
        Frame_slider4.place(x=900,y=400,width=300,height=160)
        self.lbl40=Label(Frame_slider4,image=self.img40,bd=1)
        self.lbl40.place(x=0,y=0)
        self.lbl41=Label(Frame_slider4,image=self.img41,bd=1)
        self.lbl41.place(x=0,y=0)
        self.lbl42=Label(Frame_slider4,image=self.img42,bd=1)
        self.lbl42.place(x=0,y=0)
        self.lbl43=Label(Frame_slider4,image=self.img43,bd=1)
        self.lbl43.place(x=300,y=0)        
        self.x=300    
        # self.slider_func4()
            

        
 

    def slider_func4(self) :
        self.x-=1 
        if self.x==0 :
            self.x=300
            #=============Swap==============#
            self.new_img4=self.img40 
            self.img40=self.img41
            self.img41=self.img42
            self.img42=self.img43
            self.img43=self.new_img4
            self.lbl40.config(image=self.img40)
            self.lbl41.config(image=self.img41)
            self.lbl42.config(image=self.img42)
            self.lbl43.config(image=self.img43)

        self.lbl43.place(x=self.x,y=0)
        self.lbl43.after(12,self.slider_func4)


# root=Tk()
# obj=slider4(root)
# root.mainloop()