
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
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        self.root.focus_force()

#========================= WIDGETS= ======================================================================#

        #======== Variables ==========#
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_confirm=StringVar()
        self.imageList=[]
        #===== Background ===========#
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0 ,relwidth=1,relheight=1) # relwidth = take according to root windw

        #===== Left image ================#
        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=80 , y=100  , width=400 , height=500)

        #======== Register Frame ===========#
        frame1=Frame(self.root,bg="gray9")
        frame1.place(x=480,y=100,width=800,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="gray9",fg="green").place(x=50,y=30)
        #============Photo Frame==========#
        frame2=Frame(frame1,bg="lightyellow",bd=2,relief=GROOVE)
        frame2.place(x=600,y=20,width=170,height=200)
        upload_btn=Button(frame1,text="Upload",cursor='hand2',command=self.imageupload).place(x=635 , y=225,width=100 )
        self.lbl_frame=Label(frame2)
        self.lbl_frame.place(x=0, y=0)
        # rec_btn=Button(frame1,text="Upload",cursor='hand2',command=self.scan).place(x=635 , y=275,width=100 )

        #======= Label =============#
        lbl_fname= Label(frame1, text="First Name ",font=("times new roman ",15 ,"bold"),bg="gray9",fg="white").place(x=45,y=100)
        lbl_star= Label(frame1, text="*",font=("times new roman ",15 ,"bold"),bg="gray9",fg="red2").place(x=150,y=100)
        lbl_lname=Label(frame1, text="Last Name",font=("times new roman ",15 ,"bold"),bg="gray9",fg="white").place(x=350,y=100)
        lbl_contact= Label(frame1, text="Contact No.",font=("times new roman ",15 ,"bold"),bg="gray9",fg="white").place(x=45,y=200)
        lbl_star1= Label(frame1, text="*",font=("times new roman ",15 ,"bold"),bg="gray9",fg="red2").place(x=160,y=200)
        lbl_email=Label(frame1, text="Email",font=("times new roman ",15 ,"bold"),bg="gray9",fg="white").place(x=350,y=200)
        lbl_password= Label(frame1, text="Password",font=("times new roman ",15 ,"bold"),bg="gray9",fg="white").place(x=45,y=300)
        lbl_star1= Label(frame1, text="*",font=("times new roman ",15 ,"bold"),bg="gray9",fg="red2").place(x=145,y=300)
        lbl_confirm=Label(frame1, text="Confirm Password",font=("times new roman ",15 ,"bold"),bg="gray9",fg="white").place(x=350,y=300)
        lbl_star1= Label(frame1, text="*",font=("times new roman ",15 ,"bold"),bg="gray9",fg="red2").place(x=530,y=300)

        #======= Entry fields =========#

        txt_fname=Entry(frame1,textvariable=self.var_fname,font=("times new roman ",15 ,"bold"),bg="lightyellow").place(x=45,y=130,width=220)
        txt_lname=Entry(frame1,textvariable=self.var_lname,font=("times new roman",15,"bold"),bg="lightyellow").place(x=350,y=130,width=220)
        txt_contact=Entry(frame1, textvariable=self.var_contact,font=("times new roman ",15 ,"bold"),bg="lightyellow").place(x=45,y=230,width=220)
        txt_email=Entry(frame1,textvariable=self.var_email,font=("times new roman",15,"bold"),bg="lightyellow").place(x=350,y=230,width=220)
        txt_password=Entry(frame1, textvariable=self.var_password,font=("times new roman ",15 ,"bold"),bg="lightyellow").place(x=45,y=330,width=220)
        txt_confirm=Entry(frame1,textvariable=self.var_confirm,font=("times new roman",15,"bold"),bg="lightyellow").place(x=350,y=330,width=220)

        #======== Check box ============#
        self.var_chk=IntVar()
        self.chk=Checkbutton(frame1,text="I agree to all terms & conditions",variable=self.var_chk,onvalue=1,offvalue=0,activebackground="gray9",font=("times new roman",12,"bold"),bg="gray9",fg="gray").place(x=45,y=370)

        #===== Button ==========#
        # self.btn_image=ImageTk.PhotoImage(file="images/admin1.png")
        # btn_register=Button(frame1,image=self.btn_image,bd=0, cursor="hand2",command=self.register_data).place(x=49,y=450)
        btn_login=Button(self.root,text="Sign in",font=("times new roman",17,"bold"),bd=0, cursor="hand2",command=self.login_window).place(x=240,y=460)


        admin=Image.open('images/admin1.png')
        admin=admin.resize((70,70),Image.ANTIALIAS)
        self.admin_img=ImageTk.PhotoImage(admin)
        btn_admin=Button(frame1,image=self.admin_img,cursor="hand2",bg="gray9",activebackground="gray9",bd=0,relief=GROOVE,command=self.register_data)
        btn_admin.place(x=260,y=405,width=100)
        text1=Label(frame1,text="Admin",font=("georgia",10),bg="gray9",fg="white").place(x=286,y=476)

        # student=Image.open('images/student1.Png')
        # student=student.resize((70,70),Image.ANTIALIAS)
        # self.stu_img=ImageTk.PhotoImage(student)
        # btn_student=Button(frame1,image=self.stu_img,cursor="hand2",bg="gray9",bd=0,relief=GROOVE,command=self.register_stu_data)
        # btn_student.place(x=220,y=420,width=100)
    
#================================= FUNCTIONS ==============================================#

    
    def imageupload(self):
        file1=askopenfilename()
        img=Image.open(file1)
        img1=img.resize((162,192),Image.ANTIALIAS)
        img1=ImageTk.PhotoImage(img1) 
        self.lbl_frame.image=img1
        self.lbl_frame.config(image=img1)
        
        with open(file1, 'rb') as file:
             blobData = file.read()
            #  print("blobData",blobData, type(blobData))
             self.var_pic=blobData

    
        #  ANTIALIAS = resolution / pixel won't effect
        #  again open image bcz it resize image during runtime and 
        #  dont define (file='path') coz we dont know the path of resized image
        
        
    def clear(self):
        self.var_chk.set(0)
        self.var_confirm.set("")
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_password.set("")
        self.lbl_frame.image=''

    def register_data(self):
       
        if self.var_fname.get() == "" or self.var_contact.get()=="" or self.var_password.get()=="" or self.var_confirm.get()=="":
            messagebox.showerror("Error","Fill the required field",parent=self.root)
        elif  self.var_password.get()!=self.var_confirm.get():
            messagebox.showerror("Error","password & confirm password should be same",parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","please agree our terms & condition",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM employe WHERE email=?",(self.var_email.get(),))
                row=cur.fetchone()  # if record is found then fetch that record otherwise retur none
                if row!=None:
                    messagebox.showerror("Error","Email address is already registered, try with different email",parent=self.root)
                else:
                    cur.execute("INSERT into employe(fname,lname,contact,email,password,photo) values(?,?,?,?,?,?)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_password.get(),
                        self.var_pic
                    ))
                    # self.fetch_e()
                    self.collect(self.var_pic,self.var_fname.get())
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully",parent=self.root)
                    self.clear()
                    

            except Exception as e:
                print(e)
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)


    def register_stu_data(self):
       
        if self.var_fname.get() == "" or self.var_contact.get()=="" or self.var_password.get()=="" or self.var_confirm.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif  self.var_password.get()!=self.var_confirm.get():
            messagebox.showerror("Error","password & confirm password should be same",parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","please agree our terms & condition",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM user WHERE email=?",(self.var_email.get(),))
                row=cur.fetchone()  # if record is found then fetch that record otherwise retur none
                if row!=None:
                    messagebox.showerror("Error","Email address is already registered, try with different email",parent=self.root)
                else:
                    cur.execute("INSERT into user(fname,lname,contact,email,password,photo) values(?,?,?,?,?,?)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_password.get(),
                        self.var_pic
                    ))
                    # self.fetch_e()
                    self.collect(self.var_pic,self.var_fname.get())
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully",parent=self.root)
                    self.clear()
                    

            except Exception as e:
                print(e)
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.root)

    def collect(self,pic,name):
        data=f"D:\Projects\Student_management_System\\faces_rec\\ {name} .jpg"
        self.imageList.append(data)
        with open(data, 'wb') as file:
            	file.write(pic)
    
    def scan(self):
        # op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        os.system("python recog.py")

    
    def fetch_e(self):
        faceRec=[]
        # self.var_email="cjain3631@gmail.com"
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT photo FROM employe")
            row=cur.fetchone()
            j=0
            for i in row:
                print(type(i))
                data=f"D:\Projects\Student_management_System\\faces_rec\\ { str(j)} .jpg"
                faceRec.append(data)
                j=j+1
                # print(i)
                with open(data, 'wb') as file:
            	     file.write(i)
        except Exception as ex:
            # print(ex)
            messagebox.showerror("Error",f"Error due to {str(ex)}")

            # fp = io.BytesIO(i)
            # print("Stored blob data into: ",data)
            # for i in row:
            #     # fp = io.BytesIO(i[0])
            #     print(type(i[0]))
            # with open(data, 'wb') as file:
            # 	file.write(row)
            # print(data)
            # cur.execute("SELECT * FROM employe WHERE email=?",(self.var_email,))
            # rows=cur.fetchone()
            # print("row",type(rows))
            # print("fname = ", rows[1], "lname = ", rows[2])
            # photo = rows[6]  
            # print(type(photo))
            # fp = io.BytesIO(photo)
            # image = Image.open(fp)
            # image=image.resize((162,192),Image.ANTIALIAS)
            # render = ImageTk.PhotoImage(image)
            # img = Label(image=render)
            # img.image = render
            # img.place(x=0, y=0)
       
        


    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
            

if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=Register(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen