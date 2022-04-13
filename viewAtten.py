from tkinter import *
from PIL import Image,ImageTk  # to deal with images
from tkinter import ttk,messagebox
import sqlite3
# from ttkwidgets import  Calendar
from tkcalendar import *

class attendenceClass: 
    def __init__(self,root):
        self.root=root      #initialize root
        self.root.title("Student Management System")
        self.root.geometry("1100x640+110+10")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        self.root.focus_force()
        #==== Title =====#
        title=Label(self.root,text="Attendence",
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0 , y=15 ,width=1100,height=35)

#==================================== FRAME ============================================================================
        self.frame1=Frame(self.root,bg="white",bd=2,relief=GROOVE)
        self.frame1.place(x=35,y=55,width=1025,height=577)

        self.C_Frame=Frame(self.frame1, bd=2 , relief=RIDGE,bg="black") # attendence taking frame 
        self.C_Frame.place(x=10, y = 70 , width= 1000 , height= 440)
        # self.calendar = Calendar(self.frame1, year=2021, month=6, selectforeground='white',selectbackground='red')
        # self.calendar.pack()
        self.date=StringVar()
        self.roll=StringVar()
        lbl_date=Label(self.frame1,text="Date",font=("georgia",15,"bold"),bg="white",fg="gray9").place(x=20,y=20)
        self.ent=DateEntry(self.frame1,textvariable=self.date,width=15,bg="blue",fg="red",bd=3)
        self.ent.place(x=90,y=20,width=150,height=30)

        self.im_search=Image.open('images/search1.png')
        self.im_search=self.im_search.resize((40,40),Image.ANTIALIAS)
        self.im_search=ImageTk.PhotoImage(self.im_search)
        self.datesearch=Button(self.frame1,image=self.im_search,bd=0,font=("times new roman",13,"bold"),bg="white",cursor='hand2',command=self.date_search).place(x=250,y=14)
        self.Show=Button(self.frame1,text="Show All",font=("times new roman",13,"bold"),bg="gray9",fg="white",cursor='hand2',command=self.show).place(x=790,y=20,width=95)
        self.btn_clear=Button(self.frame1,text="Clear",font=("times new roman",13,"bold"),bg="gray",fg="white",cursor='hand2',command=self.clear).place(x=900, y=20,width=95)
        # self.rollSearch=Button(self.frame1,image=self.im_search,bd=0,font=("times new roman",13,"bold"),bg="white",cursor='hand2').place(x=115,y=2)
         
        # lbl_dateSearch=Label(self.frame1,text="Date",font=("georgia",15,"bold"),bg="white",fg="gray9").place(x=545,y=8)

        # separator = ttk.Separator(self.frame1, orient='vertical',bg="white")
        # separator.place(x=505,y=0, relwidth=0.1, relheight=1)
        # line=Frame(self.frame1, bd=2 , relief=RAISED,bg="gray") # attendence taking frame 
        # line.place(x=525 , y =0 , width=1 , height= 572)

        # self.D_Frame=Frame(self.frame1, bd=2 , relief=RIDGE,bg="black") # attendence taking frame 
        # self.D_Frame.place(x=540 , y = 47 , width= 673 , height= 460)
        self.lbl_present=Label(self.frame1,text="Present ",font=("goudy old style",15),bd=1,relief=GROOVE,bg="#e43b06",fg="white")
        self.lbl_present.place(x=200, y=520 ,width=170,height=40)
        self.lbl_absent=Label(self.frame1,text="Absent ",font=("goudy old style",15),bd=1,relief=GROOVE,bg="#0676ad",fg="white")
        self.lbl_absent.place(x=400, y=520 ,width=170,height=40)
        self.lbl_total=Label(self.frame1,text="Total ",font=("goudy old style",15),bd=1,relief=GROOVE,bg="#038074",fg="white")
        self.lbl_total.place(x=600, y=520,width=170,height=40)
        

# ============================= Tree View ==========================================================================

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
              
        self.CourseTable1=ttk.Treeview(self.C_Frame,columns=(1,2,3,4,5),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set,height=6)
        style=ttk.Style(self.CourseTable1)
        style.theme_use("clam")    #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        style.configure('Treeview',rowheight=30)
        # self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","password","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable1.xview)
        scrolly.config(command=self.CourseTable1.yview)
        # self.CourseTable.tag_configure('checked',image=self.im_check)
        # self.CourseTable.tag_configure('unchecked',image=self.im_uncheck)
        self.CourseTable1.pack(fill=BOTH,expand=1)  #place according C_frame
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable1.xview)
        scrolly.config(command=self.CourseTable1.yview)

        
        self.CourseTable1.heading("#1",text="Roll No.")
        self.CourseTable1.heading("#2",text="Name")
        self.CourseTable1.heading("#3",text="Course")
        self.CourseTable1.heading("#4",text="Date")
        self.CourseTable1.heading("#5",text="Status")

        self.CourseTable1["show"]='headings'
        
        self.CourseTable1.column("1",width=100,anchor=CENTER)
        self.CourseTable1.column("2",width=170,anchor=CENTER)
        self.CourseTable1.column("3",width=200,anchor=CENTER)
        self.CourseTable1.column("4",width=150,anchor=CENTER)
        self.CourseTable1.column("5",width=150,anchor=CENTER)
        self.myRoll()
#=========================================================================================================================
    def myRoll(self):  #JOIN OPERATION
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT s.roll FROM student s INNER JOIN momo m ON s.email=m.email ")
            # cur.execute("SELECT * FROM attendence WHERE date=?",(self.date1.get(),))
            rows=cur.fetchone()
            return rows[0]
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
    
        self.CourseTable1.delete(*self.CourseTable1.get_children())
        self.lbl_present.config(text="Present ")
        self.lbl_absent.config(text="Absent ")
        self.lbl_total.config(text="Total ")

    def date_search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        roll=self.myRoll()
        try:
            cur.execute("SELECT * FROM attendence WHERE date=? and roll=?",(self.date.get(),roll))
            rows=cur.fetchall()
            pcount=0
            acount=0
            if(len(rows)>0):
                self.CourseTable1.delete(*self.CourseTable1.get_children())
                for row in rows:
                    self.CourseTable1.insert('',END,values=row)   # by default box in unchecked
                    if "Present" in row:
                        pcount+=1
                    elif "Absent" in row:
                        acount+=1
                self.lbl_present.config(text=f"Present {str(pcount)}")
                self.lbl_absent.config(text=f"Absent {str(acount)}")
                self.lbl_total.config(text=f"Total {str(len(rows))}")
                con.commit()
                con.close()
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def show(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        roll=self.myRoll()
        try:
            cur.execute("SELECT * FROM attendence WHERE roll=?",(roll,))
            rows=cur.fetchall()
            # print(rows)
            pcount=0
            acount=0
            if(len(rows)>0):
                self.CourseTable1.delete(*self.CourseTable1.get_children())
                for row in rows:
                    self.CourseTable1.insert('',END,values=row)   # by default box in unchecked
                    if "Present" in row:
                        pcount+=1
                    elif "Absent" in row:
                        acount+=1
                self.lbl_present.config(text=f"Present {str(pcount)}")
                self.lbl_absent.config(text=f"Absent {str(acount)}")
                self.lbl_total.config(text=f"Total {str(len(rows))}")
                con.commit()
                con.close()
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=attendenceClass(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen