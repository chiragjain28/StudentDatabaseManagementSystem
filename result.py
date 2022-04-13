from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3
class resultClass:     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+100")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        self.root.focus_force()
        #==== Title =====#
        title=Label(self.root,text="Add Student Result",
        font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10 , y=15 ,width=1180,height=50)

#========================================== WIDGETS ===================================================================#

        #====== Variables ==============# 
        self.var_roll= StringVar()
        self.var_name= StringVar()
        self.var_course= StringVar()
        self.var_marks= StringVar()
        self.var_full_marks= StringVar()
        self.roll_list=['Select']
        self.fetch_roll()

        #====  Label  ================|
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50 , y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50 , y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50 , y=220)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50 , y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50 , y=340)
        
        #=== Entry fields =============|

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_student.place(x=280 , y=100,width=170) #convert to self as it is used in function also
        self.txt_student.current(0)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.search).place(x=470, y=99 ,width=110,height=30)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="light yellow",fg="black",state='readonly').place(x=280 , y=160 , width=300)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="light yellow",fg="black",state='readonly').place(x=280 , y=220,width=300)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",20,"bold"),bg="light yellow",fg="black").place(x=280 , y=280,width=300)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20,"bold"),bg="light yellow",fg="black").place(x=280 , y=340,width=300)
        
        #=======Buttons============#
        btn_add=Button(self.root,text="Submit",font=("goudy old style",15,"bold"),bg="lightgreen",activebackground="lightgreen" , fg="black",cursor="hand2",command=self.add).place(x=300, y=420 ,width=110,height=35)
        btn_clear=Button(self.root,text="clear",font=("goudy old style",15,"bold"),bg="#f44336",activebackground="#f44336",fg="black",cursor="hand2",command=self.clear).place(x=430, y=420 ,width=120,height=35)

         #==== image ==============#
        self.bg_img=Image.open(r"images\result.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS) #ANTIALIAS = resolution / pixel won't effect
        self.bg_img=ImageTk.PhotoImage(self.bg_img)   # again open image bcz it resize image during runtime and 
                                                      #  dont define (file='path') coz we dont know the path of resized image
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650, y=100)

#========================FUNCTIONS====================================================================================
    def fetch_roll(self):
            con=sqlite3.connect(database='rms.db')
            cur=con.cursor()
            try:
                cur.execute("SELECT roll FROM student")
                rows=cur.fetchall()
                if len(rows)>0:
                    for row in rows:
                        self.roll_list.append(row[0])
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute(f"SELECT name,course FROM student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):  
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please Search Student Record",parent=self.root) # parent = appeared on which window
            else:
                cur.execute("SELECT * FROM result WHERE roll=? AND course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result Already Exist",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100/int(self.var_full_marks.get()))
                    cur.execute("INSERT INTO result(roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",
                    (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def clear(self):
        self.var_roll.set("Select")         
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=resultClass(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen