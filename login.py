import sqlite3
from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3
import os
from loginTop import top_Class # from studentSTU import studentDashclass as Sd

guava="1234"
class Login: 
    # guava="1234ff"    
    def __init__(self,root):  # pass root which is object of Tk
        self.root=root      #initialize root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")  #width x height + x axis(left corner) + top position
        # self.root.config(bg="gray5")
        #===== Background colour ===========#

        self.bg_img1=Image.open(r"images/login1.png")
        self.bg_img1=self.bg_img1.resize((1360,700),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.bg_img1=ImageTk.PhotoImage(self.bg_img1)

        self.lbl_bg1=Label(self.root,image=self.bg_img1)
        self.lbl_bg1.place(x=-3,y=-3)

        # left_label=Label(self.root,bg="dark slate gray")  #skyblue colour #08A3D2
        # left_label.place(x=0 , y=0 , relheight=1 , width=600)

        # rght_label=Label(self.root,bg="dark slate gray")  #Blue colour  #031F3C
        # rght_label.place(x=700 , y=0 , relheight=1 , relwidth=1)

        # cen_label=Label(self.root,bg="gray5")  #Blue colour  #031F3C
        # cen_label.place(x=0 , y=300 , height=80 , relwidth=1)
        #========= Variables ==================# 
        self.var_emai=StringVar()
        self.var_pas=StringVar()
        #========= Frame ==================#
        self.var_email=StringVar()
        frame1=Frame(self.root,bg="gray9")
        frame1.place(x=435,y=80,width=420,height=550)
        
        #========= Label ===================#
        title=Label(frame1,text="LOGIN HERE",font=("georgia",30),bg="gray9",fg="white").place(x=80,y=35)
        email=Label(frame1,text="Email Address",font=("helvetica",18,"bold"),bg="gray9",fg="white").place(x=60,y=160)
        password=Label(frame1,text="Password",font=("comic sans",18,"bold"),bg="gray9",fg="white").place(x=60,y=250)
        #========= Entry fields ===================#
        self.txt_email=Entry(frame1,textvariable=self.var_email, font=("time new roman",15,"bold"),bg="lightgray")
        self.txt_email.place(x=60,y=200,width=300)
        self.txt_password=Entry(frame1,show="*",font=("time new roman",15,"bold"),bg="lightgray")
        self.txt_password.place(x=60,y=290,width=300)
        #========= Button ===============#

        btn_register=Button(frame1,text="Don't have an account? Sign Up",font=("comic sans",12),bd=0,activebackground="white",bg="gray9",fg="#B00857",cursor="hand2",command=self.register_window)
        btn_register.place(x=60,y=335)
        # btn_login=Button(frame1,text="Login",font=("helvetica",15),activebackground="#B00857",bg="#B00857",fg="white",cursor="hand2",command=self.login)
        # btn_login.place(x=130,y=420,width=160)
        text1=Label(frame1,text="Admin",font=("georgia",10),bg="gray9",fg="white").place(x=115,y=485)
        text2=Label(frame1,text="Student",font=("georgia",10),bg="gray9",fg="white").place(x=243,y=485)

        admin=Image.open('images/admin1.png')
        admin=admin.resize((70,70),Image.ANTIALIAS)
        self.admin_img=ImageTk.PhotoImage(admin)
        btn_admin=Button(frame1,image=self.admin_img,cursor="hand2",bg="gray9",activebackground="gray9",bd=0,relief=GROOVE,command=self.login)
        btn_admin.place(x=90,y=410,width=100)
        # btn_e=Button(frame1,text="email",cursor="hand2",bg="gray9",bd=0,relief=GROOVE,command=self.email)
        # btn_e.place(x=160,y=410,width=100)

        student=Image.open('images/student1.Png')
        student=student.resize((70,70),Image.ANTIALIAS)
        self.stu_img=ImageTk.PhotoImage(student)
        btn_student=Button(frame1,image=self.stu_img,cursor="hand2",bg="gray9",activebackground="gray9",bd=0,relief=GROOVE,command=self.login_student)
        btn_student.place(x=220,y=410,width=100)

        face=Image.open('images/face1.Png')
        face=face.resize((50,50),Image.ANTIALIAS)
        self.face=ImageTk.PhotoImage(face)
        btn_face=Button(frame1,image=self.face,cursor="hand2",bg="gray9",activebackground="gray9",bd=0,relief=GROOVE,command=self.add_recog)
        btn_face.place(x=160,y=100,width=100)


    # def email(self):
    #     messagebox.showinfo("Email",self.txt_email.get(),parent=self.root)
    def register_window(self):
        self.root.destroy()
        os.system("python register.py")

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","Email and password are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor() # help to execute sql queries like insert delete select
                cur.execute("SELECT * FROM employe WHERE email=? and password=?",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone() # give none if record is not found else return one record corresponding to email and password
                
                if row==None:
                    messagebox.showerror("Error","Invalid username or password",parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")

            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)
    

    def login_student(self):
    
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","Email and password are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor() # help to execute sql queries like insert delete select
                cur.execute("SELECT * FROM student WHERE email=? and password=?",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone() # give none if record is not found else return one record corresponding to email and password
                if row==None:
                    messagebox.showerror("Error","Invalid username or password",parent=self.root)
                else:
                    # print(self.var_email.get())
                    guava=self.var_email.get()
                    # print(value)
                    
                    # print("vslue",value)
                    print(self.var_email.get())
                    # cur.execute("INSERT INTO student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address,password) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    cur.execute("INSERT INTO momo(email) values(?)",(self.var_email.get(),))
                    con.commit()
                    con.close()
                    # row=cur.fetchone()
                    # Sd.fill_field(self,self.var_email.get())
                    # ,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]
                    # ,row[9],row[10],row[11]
                    # a="c"
                    # Sd.get_data(self,a,row)
                    # print(row[1])
                    # Sd.var_roll=row[0]
                    
                    self.root.destroy()
                    os.system("python dashboardStudent.py")
                    

            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    def add_recog(self):
        self.new_window=Toplevel(self.root)   # Create new window , Toplevel = appear on top of other 
                                              # window which is given as arguement
        self.new_obj=top_Class (self.new_window)

    
if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=Login(root)    #create object of RMS class and pass root obj
    
    root.mainloop()  #for continously show on screen