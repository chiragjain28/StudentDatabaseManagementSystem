from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3
import smtplib

class studentClass:     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+100")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        self.root.focus_force()
        #==== Title =====#
        title=Label(self.root,text="Student Details",
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10 , y=15 ,width=1180,height=35)
        

#======================================== WIDGETS ===================================================================#

        #=====Variables===========#

        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_pass=StringVar()

        #====  Column 1  ================#

        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=10 , y=60)
        lbl_Name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10 , y=100)
        lbl_Email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10 , y=140)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15,"bold"),bg="white").place(x=10 , y=175)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10 , y=210)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10 , y=250)
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10 , y=290)
        #===Column 1 -> Entry fields=============#
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="light yellow",fg="black")
        self.txt_roll.place(x=150 , y=60,width=200)  #convert to self as it is used in function also
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=150 , y=100 , width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=150 , y=140,width=200)
        self.txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15,"bold"),bg="light yellow",fg="black")
        self.txt_pass.place(x=150 , y=175,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=150 , y=210,width=200)
        self.txt_gender.current(0)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=150 , y=250,width=135)
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="light yellow",fg="black")
        self.txt_address.place(x=150 , y=290 , width=530 , height=100)
        

        #====  Column 2  ================#
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=360 , y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360 , y=100)
        lbl_Admission=Label(self.root,text="Admission No.",font=("goudy old style",15,"bold"),bg="white").place(x=360 , y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=360 , y=210)
        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=492 , y=250)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=303 , y=250)
        #===Column 2 -> Entry fields=============#
        self.course_list=["Select"]
        self.fetch_course()
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=488 , y=60,width=192)  #convert to self as it is used in function also
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=488 , y=100 , width=192)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=488 , y=140,width=192)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=480 , y=210,width=200)
        self.txt_course.current(0)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=540 , y=250,width=140)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=350 , y=250,width=133)
        #=====Buttons==============#
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400 ,width=110,height=30)
        self.btn_update=Button(self.root,text="update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400 ,width=110,height=30)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400 ,width=110,height=30)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400 ,width=110,height=30)
        
        #=====Search Panel======#
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Rollno.",font=("goudy old style",15,"bold"),bg="white").place(x=720 , y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=870 , y=60 , width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.search).place(x=1070, y=60 ,width=120,height=30)

        #====content=======#
        self.C_Frame=Frame(self.root , bd=2 , relief=RIDGE)
        self.C_Frame.place(x=720 , y = 100 , width= 470 , height= 340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","password","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("password",text="Password")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="Pin")
        self.CourseTable.heading("address",text="Address")


        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=150)
        self.CourseTable.column("name",width=150)
        self.CourseTable.column("email",width=150)
        self.CourseTable.column("password",width=150)
        self.CourseTable.column("gender",width=150)
        self.CourseTable.column("dob",width=150)
        self.CourseTable.column("contact",width=150)
        self.CourseTable.column("admission",width=150)
        self.CourseTable.column("course",width=150)
        self.CourseTable.column("state",width=150)
        self.CourseTable.column("city",width=150)
        self.CourseTable.column("pin",width=150)
        self.CourseTable.column("address",width=150)

        self.CourseTable.pack(fill=BOTH , expand=1)  #place according C_frame
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data) # help to perform event with button click
        self.show()
        self.fetch_course()
#============================================= FUNCTIONS ===========================================================================
    def clear(self):
        self.show()
        self.var_roll.set("")         
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)  # first delete data store in desp
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
        self.var_pass.set("")

    def delete(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll number should be required",parent=self.root) # parent = appeared on which window
            else:
                cur.execute("SELECT * FROM student WHERE roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select the student",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM student WHERE roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        

    def get_data(self,event):# second parameter essential if we bind any event
        self.txt_roll.config(state="readonly")
        r=self.CourseTable.focus()   # focus on where we click cursor and that stores in r
        content=self.CourseTable.item(r) # to get item , get r 
        row=content["values"]  #(only get values) the values in content stores in row 
        print(type(self.var_roll))
        self.var_roll.set(row[0])          
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_pass.set(row[3])
        self.var_gender.set(row[4])
        self.var_dob.set(row[5])
        self.var_contact.set(row[6])
        self.var_a_date.set(row[7])
        self.var_course.set(row[8])
        self.var_state.set(row[9])
        self.var_city.set(row[10])
        self.var_pin.set(row[11])
        self.txt_address.delete("1.0",END)  # first delete data store in desp
        self.txt_address.insert(END,row[12])

    def sendEmail(self,to,name,pas,course,count):
        if(count==1):
            TEXT=f"Dear {name} , \n\nCongratulations !\n\nYou have successfully registered for cousre {course}\nNow you can access our ''Imposter's portal'' and update your information\n\nYour login details: \nLogin id : {to}\nPassword : {pas} \n\nIMPORTANT NOTICE :\n\nYou need not to worry about the course fee and expenses , Due to this pandemic,You have to attend online classes \nand you are not using college stuff so we have halved the fees,also you can pay the fees anytime.\nWe understand your compulsion\n\nIf you have any questions or concerns, feel free to contact me at cjain3631@gmail.com or 7828872160.\n\nBest,\nImposters"
            SUBJECT="Imposters Registered You"
        else:
            TEXT=f"Dear {name} , \n\nYou have successfully updated your details for cousre {course}\nNow you can access our ''Imposter's portal''\n\nYour login details: \nLogin id : {to}\nPassword : {pas} \n\nIMPORTANT NOTICE :\n\nYou need not to worry about the course fee and expenses , Due to this pandemic,You have to attend online classes \nand you are not using college stuff so we have halved the fees,also you can pay the fees anytime.\nWe understand your compulsion\n\nIf you have any questions or concerns, feel free to contact me at cjain3631@gmail.com or 7828872160.\n\nBest,\nImposters"
            SUBJECT="Updated Successfully"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('cjain3631@gmail.com', 'Chiragjain3631')
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        server.sendmail('cjain3631@gmail.com',to , message)
        server.close()
        print("success")
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo()
        # server.starttls()
        # server.login('youremail@gmail.com', 'your-password')
        # server.sendmail('youremail@gmail.com', to, content)
        # server.close()    

 
    def add(self):  
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root) # parent = appeared on which window
            elif self.var_pass.get()=="":
                messagebox.showerror("Error","Password should be required",parent=self.root)
            elif self.var_email.get()=="":
                messagebox.showerror("Error","Email should be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll Number already present",parent=self.root)
                else:
                    cur.execute("INSERT INTO student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address,password) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.txt_pass.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added successfully",parent=self.root)
                    self.show()
                    count=1
                    self.sendEmail(self.var_email.get(),self.var_name.get(),self.var_pass.get(),self.var_course.get(),count)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def update(self):  
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root) # parent = appeared on which window
            else:
                cur.execute("SELECT * FROM student WHERE roll=?",(self.var_roll.get(),))
                row=cur.fetchall()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("UPDATE student set name=?,email=?,password=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? WHERE roll=?",
                    (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_pass.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update successfully",parent=self.root)
                    self.show()
                    count=0
                    self.sendEmail(self.var_email.get(),self.var_name.get(),self.var_pass.get(),self.var_course.get(),count)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def fetch_course(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT name FROM course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute(f"SELECT * FROM student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=studentClass(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen