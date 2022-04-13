from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
from course import courseClass
from student import studentClass 
from result import resultClass
from report import reportClass
from attendence import attendenceClass
import os
import sqlite3

class RMS:
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")  #width x height + x axis(left corner) + top position
        # self.root.config(bg="gray5")
        self.bg_img1=Image.open(r"images/dbg1.jpg")
        self.bg_img1=self.bg_img1.resize((1370,710),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.bg_img1=ImageTk.PhotoImage(self.bg_img1)   # again open image bcz it resize image during runtime and 
         #  dont define (file='path') coz we dont know the path of resized image
        self.lbl_bg1=Label(self.root,image=self.bg_img1)
        self.lbl_bg1.place(x=0,y=0)
        #==== ICONS ======#
        self.logo=ImageTk.PhotoImage(file=r"images\logo_p.png")
        #==== Title =====#
        title=Label(self.root,text="Student Management System",image=self.logo,compound=LEFT,padx=10,
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0 , y=0 ,relwidth=1,height=50) 
                    #compound = Where logo is placed , padx = distance between logo and label
                    # object of Label class (label class is widget of tkinter)
                    #first parameter = where label is made i.e label made on root window 
                    #relwidth = same width and heigth as parent window
       
        
        #=====Menu=======#
        #1st parat=meter = where to place
        # M_Frame=LabelFrame(self.root,font=("times new roman",15),bg="gray5")
        # M_Frame.place(x=10 , y=70,width=1340,height=60)
        #==Buttons----
        btn_course=Button(self.lbl_bg1,text="Course",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_course).place(x=20, y=80,width=200,height=40)
        btn_student=Button(self.lbl_bg1,text="Student",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_student).place(x=240, y=80 ,width=200,height=40)
        btn_attendence=Button(self.lbl_bg1,text="Attendance",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.attendence).place(x=460, y=80 ,width=200,height=40)
        btn_result=Button(self.lbl_bg1,text="Result",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_result).place(x=680, y=80 ,width=200,height=40)
        btn_view=Button(self.lbl_bg1,text="View Student Result",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.add_report).place(x=900, y=80 ,width=200,height=40)
        btn_logout=Button(self.lbl_bg1,text="Logout",font=("goudy old style",15,"bold"),bg="#033054",fg="white",cursor="hand2",command=self.logout).place(x=1120, y=80 ,width=200,height=40)
        
      
        #====CONTENT WINDOW====
        self.bg_img=Image.open(r"images\dbg12.jpg")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.bg_img=ImageTk.PhotoImage(self.bg_img)   # again open image bcz it resize image during runtime and 
                                                      #  dont define (file='path') coz we dont know the path of resized image
        self.lbl_bg=Label(self.root,bd=2,relief=GROOVE,image=self.bg_img).place(x=220, y=180 ,width=920,height=350)

        #=====Update details=====
        self.lbl_course=Label(self.root,text="Total Courses[0]",font=("goudy old style",20),bd=5,relief=RAISED,bg="gray9",fg="white")
        self.lbl_course.place(x=220, y=530 ,width=300,height=100)
        self.lbl_student=Label(self.root,text="Total Student[0]",font=("goudy old style",20),bd=5,relief=RAISED,bg="gray9",fg="white")
        self.lbl_student.place(x=530, y=530 ,width=300,height=100)
        self.lbl_result=Label(self.root,text="Total Results[0]",font=("goudy old style",20),bd=5,relief=RAISED,bg="gray9",fg="white")
        self.lbl_result.place(x=840, y=530 ,width=300,height=100)
        self.update_details()
        
        #==== footer =====#
        footer=Label(self.root,text="The Imposters",
        font=("goudy old style",12,"bold"),bg="black",fg="white").pack(side=BOTTOM,fill=X)

        
#========================== functions ==============================================================#
    def update_details(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course[{str(len(cr))}]")
            # self.lbl_course.after(200,self.update_details)
            cur.execute("SELECT * FROM student")
            st=cur.fetchall()
            self.lbl_student.config(text=f"Total Student[{str(len(st))}]")
            # self.lbl_student.after(200,self.update_details)
            cur.execute("SELECT * FROM result")
            rt=cur.fetchall()
            self.lbl_result.config(text=f"Total Result[{str(len(rt))}]")
            self.lbl_result.after(20,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add_course(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=courseClass(self.new_window) 
    def add_student(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=studentClass(self.new_window)
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
            self.root.destroy()
            os.system("python login.py")

    def attendence(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=attendenceClass(self.new_window) 
            

if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=RMS(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen

