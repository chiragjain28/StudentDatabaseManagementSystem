from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3
class reportClass:     
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+100")  #width x height + x axis(left corner) + top position
        self.root.config(bg="gray7")
        self.root.focus_force()
        #==== Title =====#
        title=Label(self.root,text="View Student Result",
        font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10 , y=15 ,width=1180,height=50)
#===============================WIDGETS===========================================#

        #== Variables=========#
        self.var_search=StringVar()

        #===== Search Panel=======#
        self.var_id=""
        lbl_search=Label(self.root,text="Search by Roll No.",font=("goudy old style",20,"bold"),bg="gray7",fg="white").place(x=290 , y=100)
        txt_name=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,"bold"),bg="lightyellow",fg="black").place(x=525 , y=100 , width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",17,"bold"),bg="#2196f3",fg="black",cursor="hand2",command=self.search).place(x=730, y=100 ,width=110,height=30)
        # -----------------------------
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="black",cursor="hand2",command=self.delete).place(x=550, y=400 ,width=110,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",17,"bold"),bg="gray",fg="black",cursor="hand2",command=self.clear).place(x=850, y=100 ,width=110,height=30)

        #======== Labels ==========#
        lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white").place(x=150, y=230 ,width=150,height=50) 
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white").place(x=300, y=230 ,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white").place(x=450, y=230 ,width=150,height=50)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white").place(x=600, y=230 ,width=150,height=50)
        lbl_full_marks=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white").place(x=750, y=230 ,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white").place(x=900, y=230 ,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white")
        self.roll.place(x=150, y=280 ,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white")
        self.name.place(x=300, y=280 ,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white")
        self.course.place(x=450, y=280 ,width=150,height=50)
        self.marks=Label(self.root,font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white")
        self.marks.place(x=600, y=280 ,width=150,height=50)
        self.full_marks=Label(self.root,font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white")
        self.full_marks.place(x=750, y=280 ,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bd=2,relief=GROOVE,bg="white")
        self.per.place(x=900, y=280 ,width=150,height=50)
        


#================================== Functions ====================================#


    def search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                 messagebox.showerror("Error","Search field must not be empty",parent=self.root)
            else:
                cur.execute(f"SELECT * FROM result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def delete(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search result first",parent=self.root) # parent = appeared on which window
            else:
                cur.execute("SELECT * FROM result WHERE rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Action",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM result WHERE rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear(self):
        self.var_id=""
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")



if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=reportClass(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen