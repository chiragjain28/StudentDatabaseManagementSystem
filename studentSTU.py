from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3

class studentDashclass: 
     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("775x480+260+100")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        self.root.focus_force()
        #==== Title =====#
        title=Label(self.root,text="Student Details",
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10 , y=15 ,width=775,height=35)
        

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
        self.txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="light yellow",fg="black")
        self.txt_admission.place(x=488 , y=140,width=192)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=480 , y=210,width=200)
        self.txt_course.current(0)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=540 , y=250,width=140)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=350 , y=250,width=133)
        #=====Buttons==============#
        # self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.add)
        # self.btn_add.place(x=150, y=400 ,width=110,height=30)

        self.btn_update=Button(self.root,text="update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400 ,width=110,height=30)

        # self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="black",cursor="hand2",command=self.delete)
        # self.btn_delete.place(x=390, y=400 ,width=110,height=30)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400 ,width=110,height=30)
        self.get_data(3)
    
#============================================= FUNCTIONS ===========================================================================
    
    # def fill_field(self,value):
    #     doge=value
        
        
        # self.txt_address.delete("1.0",END)  # first delete data store in desp
        # self.txt_roll.config(state=NORMAL)   

    def clear(self):
        # self.show()
        self.var_roll.set("")         
        self.var_name.set("")
        self.var_email.set("")
        self.var_pass.set("")
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
        # self.var_search.set("")
    
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
        # self.txt_roll.config(state="readonly")
        # r=self.CourseTable.focus()   # focus on where we click cursor and that stores in r
        # content=self.CourseTable.item(r) # to get item , get r 
        # row=content["values"]  #(only get values) the values in content stores in row
        # print(type(self.var_a_date))
        con=sqlite3.connect('rms.db')
        cur=con.cursor()
        cur.execute("SELECT email FROM momo")
        mail=cur.fetchone()
        cj=mail[0]
        # print(mail[0])
        cur.execute("SELECT * FROM student WHERE email=?",(cj,))
        row=cur.fetchone()
        # print(row)
        # cur.execute("DELETE FROM momo WHERE email=?",(cj,))
        # cur.execute("DELETE FROM student WHERE roll=?",(self.var_roll.get(),))
        con.commit()
        con.close()
        self.txt_roll.config(state="readonly")
        self.txt_admission.config(state="readonly")
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

        # row=[1,2,3,4,5,6,7,7,8,9,9,97,54]
        # print("get ",type(self.var_name))
        # print("hello")
        # print("get data ofjjdhd",row)
        
        
        # self.txt_address.delete("1.0",END)  # first delete data store in desp
        # self.txt_address.insert(END,row[11])


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
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update successfully",parent=self.root)
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
    

    




if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=studentDashclass(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen