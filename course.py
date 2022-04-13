from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3
class courseClass:     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+100")  #width x height + x axis(left corner) + top position
        self.root.config(bg="gray7")
        self.root.focus_force()
        #==== Title =====#
        title=Label(self.root,text="Manage Course Details",
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10 , y=15 ,width=1180,height=35)
        

#============================================ WIDGETS ======================================================================#

        #=====Variables======#
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
 
        #===== Label =========#
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="gray7",fg="white").place(x=10 , y=63)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="gray7",fg="white").place(x=10 , y=103)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="gray7",fg="white").place(x=10 , y=143)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="gray7",fg="white").place(x=10 , y=183)
        #===Entry fields======#
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",18,"bold"),bg="light yellow",fg="black")
        self.txt_courseName.place(x=150 , y=63,width=200)  #convert to self as it is used in function also

        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",18,"bold"),bg="light yellow",fg="black").place(x=150 , y=103 , width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",18,"bold"),bg="light yellow",fg="black").place(x=150 , y=143,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",18,"bold"),bg="light yellow",fg="black")
        self.txt_description.place(x=150 , y=185 , width=500 , height=130)

        #======Buttons========#
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400 ,width=110,height=30)

        self.btn_update=Button(self.root,text="update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400 ,width=110,height=30)

        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="black",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400 ,width=110,height=30)

        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400 ,width=110,height=30)
        
        #=====Search Panel=======#
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="gray7",fg="white").place(x=720 , y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="light yellow",fg="black").place(x=870 , y=60 , width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.search).place(x=1070, y=60 ,width=120,height=30)

        #=========content=========#
        self.C_Frame=Frame(self.root , bd=2 , relief=RIDGE)
        self.C_Frame.place(x=720 , y = 100 , width= 470 , height= 340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course Id")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")

        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=100)

        self.CourseTable.pack(fill=BOTH , expand=1)  #place according C_frame
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data) # help to perform event with button click
        self.show()
#============================================== FUNCTIONS ============================================================================

    def clear(self):
        self.show()
        self.var_course.set("") #not include course id
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0",END)  # first delete data store in desp
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root) # parent = appeared on which window
            else:
                cur.execute("SELECT * FROM course WHERE name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select the course",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM course WHERE name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        

    def get_data(self,event):# second parameter essential if we bind any event
        self.txt_courseName.config(state="readonly")
        r=self.CourseTable.focus()   # focus on where we click cursor and that stores in r
        content=self.CourseTable.item(r) # to get item , get r 
        row=content["values"]  #(only get values) the values in content stores in row 
        self.var_course.set(row[1]) #not include course id
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0",END)  # first delete data store in desp
        self.txt_description.insert(END,row[4])

 
    
    def add(self):  
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root) # parent = appeared on which window
            else:
                cur.execute("SELECT * FROM course WHERE name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    cur.execute("INSERT INTO course(name,duration,charges,description) values(?,?,?,?)",
                    (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):  
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root) # parent = appeared on which window
            else:
                cur.execute("SELECT * FROM course WHERE name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course from list",parent=self.root)
                else:
                    cur.execute("UPDATE course set duration=?,charges=?,description=? where name=?",
                    (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course update successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute(f"SELECT * FROM course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=courseClass(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen