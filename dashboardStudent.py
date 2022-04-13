from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
from course import courseClass
from studentSTU import studentDashclass 
from result import resultClass
from reportStu import reportClass
import os
import sqlite3
from viewAtten import attendenceClass
from Slider1 import slider1
from Slider2 import slider2
from Slider3 import slider3
from Slider4 import slider4

class RMS:     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")  #width x height + x axis(left corner) + top position
        # self.root.config(bg="gray9")
        # self.root.wm_attributes("-transparentcolor",'green')
        # self.bg=ImageTk.PhotoImage(file="images/dasd.jpg")
        # self.label_bg=Label(self.root,image=self.bg)
        # self.label_bg.place(x=0 , y=0)


        self.bg_img=Image.open(r"images/studentBg.png")
        self.bg_img=self.bg_img.resize((1350,700),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.bg_img=ImageTk.PhotoImage(self.bg_img)   # again open image bcz it resize image during runtime and 
         #  dont define (file='path') coz we dont know the path of resized image
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=0,y=0)

        self.obj1=slider1(root)
        self.obj1.slider_func1()
        self.obj2=slider2(root)
        self.obj2.slider_func2()
        self.obj3=slider3(root)
        self.obj3.slider_func3()
        self.obj4=slider4(root)
        self.obj4.slider_func4()
        # self.obj5=slider5(root)
        # self.obj5.slider_func5()
        Frame_slider5=Frame(self.root)
        Frame_slider5.place(x=0,y=50,width=1400,height=25)
        self.t1=Label(Frame_slider5,text="NOTE: University Tuition fee has been reduced by 50% in response to ongoing pandemic caused by coronavirus . #StaySafe #StayHome ...",compound=LEFT,padx=10,
        font=("goudy old style",18,"bold"))#,bg="#033054",fg="white")
        self.t1.place(x=1400 , y=0 ,width=1400,height=25) 
        self.x=1600
        self.slider_func5()
 
        n=self.myName()
        
        #==== ICONS ======#
        self.logo=ImageTk.PhotoImage(file=r"images\logo_p.png")
        #==== Title =====#
        title=Label(self.root,text="Student Management System",image=self.logo,compound=LEFT,padx=10,
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0 , y=0 ,relwidth=1,height=50) 
                    #compound = Where logo is placed , padx = distance between logo and label
                    # object of Label class (label class is widget of tkinter)
                    #first parameter = where label is made i.e label made on root window 
                    #relwidth = same width and heigth as parent window
        top_name=Label(self.root,text=" Welcome "+n,compound=LEFT,padx=10,
        font=("goudy old style",16,"bold"),bg="#033054",fg="khaki1").place(x=1090, y=10 ) 
        #=====Menu=======#
        #1st parat=meter = where to place
        # M_Frame=LabelFrame(self.root,font=("times new roman",15),bg='gray9')
        # M_Frame.place(x=75, y=70,width=1190,height=65)
        #==Buttons----
        # btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_course).place(x=20, y=8 ,width=200,height=40)
        btn_student=Button(self.root,text="Student",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_student).place(x=75, y=85 ,width=220,height=40)
        # btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_result).place(x=460, y=8 ,width=200,height=40)
        btn_view=Button(self.root,text="View Student Result",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_report).place(x=330, y=85 ,width=220,height=40)
        btn_attendence=Button(self.root,text="Attendence",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.attendence).place(x=585, y=85 ,width=220,height=40)
        btn_logout=Button(self.root,text="Logout",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.logout).place(x=840, y=85 ,width=220,height=40)
        btn_exit=Button(self.root,text="Exit",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.exit).place(x=1090, y=85 ,width=220,height=40)
      
        #====CONTENT WINDOW====
        # self.bg_img=Image.open(r"images/bg.png")
        # self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        # self.bg_img=ImageTk.PhotoImage(self.bg_img)   # again open image bcz it resize image during runtime and 
        #                                               #  dont define (file='path') coz we dont know the path of resized image
        # self.lbl_bg=Label(self.root,image=self.bg_img).place(x=220, y=180 ,width=920,height=450)

        #=====Update details=====
        # self.lbl_course=Label(self.root,text="Total Courses[0]",font=("goudy old style",20),bd=5,relief=RAISED,bg="#e43b06",fg="white")
        # self.lbl_course.place(x=220, y=530 ,width=300,height=100)
        # self.lbl_student=Label(self.root,text="Total Student[0]",font=("goudy old style",20),bd=5,relief=RAISED,bg="#0676ad",fg="white")
        # self.lbl_student.place(x=530, y=530 ,width=300,height=100)
        # self.lbl_result=Label(self.root,text="Total Results[0]",font=("goudy old style",20),bd=5,relief=RAISED,bg="#038074",fg="white")
        # self.lbl_result.place(x=840, y=530 ,width=300,height=100)
        # self.update_details()
        
        #==== footer =====#
        
        footer=Label(self.root,text="The Imposters\nDon't Try to Contact Us",
        font=("goudy old style",12,"bold"),bg="black",fg="white").pack(side=BOTTOM,fill=X)

        
#========================== functions ==============================================================#

    def slider_func5(self) :
        self.x-=1 
        if self.x==-1400 :
            self.x=1600
            #=============Swap==============#
            self.title1=self.t1 
            self.t1=self.title1        
        self.t1.place(x=self.x,y=0)
        self.t1.after(15,self.slider_func5)

    def myName(self):
        con=sqlite3.connect('rms.db')
        cur=con.cursor()
        cur.execute("SELECT s.name FROM student s INNER JOIN momo m ON s.email=m.email ")
        mail=cur.fetchone()
        return mail[0]

    def add_course(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=courseClass(self.new_window) 
    def add_student(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=studentDashclass(self.new_window)
    def add_result(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=resultClass(self.new_window) 

    def add_report(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=reportClass(self.new_window) 
    def logout(self):
        
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.del_login()
            self.root.destroy()
            os.system("python login.py")
    
    def attendence(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=attendenceClass(self.new_window) 

    def exit(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.del_login()
            self.root.destroy()
            os.system("python let'sStart.py")

    def del_login(self):
        con=sqlite3.connect('rms.db')
        cur=con.cursor()
        cur.execute("SELECT email FROM momo")
        mail=cur.fetchone()
        cj=mail[0]
        cur.execute("DELETE FROM momo WHERE email=?",(cj,))
        con.commit()
        con.close()
        # cur.execute("DELETE FROM momo WHERE email=?",(cj,))
            

if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=RMS(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen

