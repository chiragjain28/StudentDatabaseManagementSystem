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
        self.root.geometry("1300x650+30+10")  #width x height + x axis(left corner) + top position
        self.root.config(bg="white")
        self.root.focus_force()
        #==== Title =====#
        title=Label(self.root,text="Attendence",
        font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0 , y=15 ,width=1300,height=35)
#======================================CHECK BOX==============================================================================#

        self.im_checked=Image.open('images/checked.png')
        self.im_checked=self.im_checked.resize((30,30),Image.ANTIALIAS)
        self.im_check=ImageTk.PhotoImage(self.im_checked)

        self.im_unchecked=Image.open('images/unchecked.png')
        self.im_unchecked=self.im_unchecked.resize((30,30),Image.ANTIALIAS)
        self.im_uncheck=ImageTk.PhotoImage(self.im_unchecked)
#===================================== Frame ======================================================================#
        self.frame1=Frame(self.root,bg="white",bd=2,relief=GROOVE)
        self.frame1.place(x=35,y=60,width=1230,height=577)
        # self.calendar = Calendar(self.frame1, year=2021, month=6, selectforeground='white',selectbackground='red')
        # self.calendar.pack()
        self.C_Frame=Frame(self.frame1, bd=2 , relief=RIDGE,bg="black") # attendence taking frame 
        self.C_Frame.place(x=10, y = 47 , width= 500 , height= 460)

        # separator = ttk.Separator(self.frame1, orient='vertical',bg="white")
        # separator.place(x=505,y=0, relwidth=0.1, relheight=1)
        line=Frame(self.frame1, bd=2 , relief=RAISED,bg="gray") # attendence taking frame 
        line.place(x=525 , y =0 , width=1 , height= 572)

        self.D_Frame=Frame(self.frame1, bd=2 , relief=RIDGE,bg="black") # attendence taking frame 
        self.D_Frame.place(x=540 , y = 47 , width= 673 , height= 460)
        
# ==================================== Date/Calendar/Button===========================================================       
        # im_unchecked=ImageTk.PhotoImage(Image.open('images/unchecked.png'))
        self.date=StringVar()
        self.date1=StringVar()
        self.roll=StringVar()
        lbl_date=Label(self.frame1,text="Date",font=("georgia",15,"bold"),bg="white",fg="gray9").place(x=15,y=8)
        # self.lbl_entry=Entry(self.frame1,textvariable=self.date, font=("times new roman",15,"bold"),bg="lightyellow")
        # self.lbl_entry.place(x=70,y=3,width=200)
        # self.top=Toplevel(self.frame1)
        self.ent=DateEntry(self.frame1,text="",textvariable=self.date,width=15,bg="blue",fg="red",bd=3)
        self.ent.place(x=80,y=8,width=150,height=30)
         
        lbl_dateSearch=Label(self.frame1,text="Date",font=("georgia",15,"bold"),bg="white",fg="gray9").place(x=545,y=8)
        self.ent1=DateEntry(self.frame1,text="",textvariable=self.date1,width=15,bg="lightyellow",fg="red",bd=3)
        self.ent1.place(x=610,y=8,width=150,height=30)
        
        lbl_roll=Label(self.frame1,text="Roll",font=("georgia",15,"bold"),bg="white",fg="gray9").place(x=940,y=8)
        entry_roll=Entry(self.frame1,text="Roll",textvariable=self.roll,font=("georgia",15,"bold"),bg="white",fg="gray9").place(x=1000,y=8,width=150,height=30)
        self.im_search=Image.open('images/search1.png')
        self.im_search=self.im_search.resize((40,40),Image.ANTIALIAS)
        self.im_search=ImageTk.PhotoImage(self.im_search)
        self.datesearch=Button(self.frame1,image=self.im_search,bd=0,font=("times new roman",13,"bold"),bg="white",cursor='hand2',command=self.date_search).place(x=765,y=2)
        self.rollSearch=Button(self.frame1,image=self.im_search,bd=0,font=("times new roman",13,"bold"),bg="white",cursor='hand2',command=self.roll_search).place(x=1155,y=2)
        
        self.dtBtn=Button(self.frame1,text="Select",font=("times new roman",13,"bold"),bg="#e43b06",cursor='hand2',command=self.date_func).place(x=240,y=8,width=115,height=30)
        self.tka=Button(self.frame1,text="Take Attendence",font=("times new roman",13,"bold"),bg="#0676ad",cursor='hand2',command=self.take_atten).place(x=368,y=8,height=30)
        self.btn_done=Button(self.frame1,text="Done",font=("goudy old style",15,"bold"),bg="#038074",cursor='hand2',command=self.done).place(x=70, y=520,width=170,height=40)
        self.btn_clear=Button(self.frame1,text="Clear",font=("goudy old style",15,"bold"),bg="gray",cursor='hand2',command=self.clear).place(x=290, y=520,width=170,height=40)


        self.lbl_present=Label(self.frame1,text="Present ",font=("goudy old style",15),bd=1,relief=GROOVE,bg="#e43b06",fg="white")
        self.lbl_present.place(x=600, y=520 ,width=170,height=40)
        self.lbl_absent=Label(self.frame1,text="Absent ",font=("goudy old style",15),bd=1,relief=GROOVE,bg="#0676ad",fg="white")
        self.lbl_absent.place(x=800, y=520 ,width=170,height=40)
        self.lbl_total=Label(self.frame1,text="Total ",font=("goudy old style",15),bd=1,relief=GROOVE,bg="#038074",fg="white")
        self.lbl_total.place(x=1000, y=520,width=170,height=40)
        
        # lab=Label(self.C_Frame,image=self.im_check).pack()
        # lab1=Label(self.C_Frame,image=self.im_uncheck).pack()
#=================================== Tree View 1 / Scroll Bar ========================================================

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
              
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=(1,2,3,4),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set,height=6)
        style=ttk.Style(self.CourseTable)
        style.theme_use("clam") 
        style.configure('Treeview',rowheight=35)
        # self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","password","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.tag_configure('checked',image=self.im_check)
        self.CourseTable.tag_configure('unchecked',image=self.im_uncheck)
        self.CourseTable.pack(fill=BOTH,expand=1)  #place according C_frame
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        # self.tree.heading("#0",text="")
        self.CourseTable.heading("#0",text="Status")
        self.CourseTable.heading("#1",text="Roll No.")
        self.CourseTable.heading("#2",text="Name")
        self.CourseTable.heading("#3",text="Course")

        # self.CourseTable["show"]='headings'
        self.CourseTable.column("0")
        self.CourseTable.column("1",width=100)
        self.CourseTable.column("2",width=150)
        self.CourseTable.column("3",width=150)
        # self.CourseTable.column("status",width=100)
        # self.show()
        self.CourseTable.bind("<ButtonRelease-1>",self.toggleCheck)
    
#=================================== Tree View 2 ======================================================================

        scrolly=Scrollbar(self.D_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.D_Frame,orient=HORIZONTAL)
              
        self.CourseTable1=ttk.Treeview(self.D_Frame,columns=(1,2,3,4,5),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set,height=6)
        style=ttk.Style(self.CourseTable1)
        style.theme_use("clam") 
        style.configure('Treeview',rowheight=35)
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
        
        self.CourseTable1.column("1",width=100)
        self.CourseTable1.column("2",width=140)
        self.CourseTable1.column("3",width=150)
        self.CourseTable1.column("4",width=150)
        self.CourseTable1.column("5",width=150)

        # self.CourseTable.pack(fill=BOTH , expand=1)  #place according C_frame
        # self.CourseTable.bind("<Double 1>",self.get_data) # help to perform event with button click
        
        # # self.show()
        # # self.fetch_course()

    # def dateselect(self):
    #     self.top=Toplevel(self.frame1)
    #     self.calendar = Calendar(self.top,selectmode="day", year=2021, month=6,selectforeground='white',selectbackground='black')
    #     self.calendar.pack()
    #     btn=Button(self.top, text='Select',command=self.date_func).pack()
    #     # print(self.calendar.get_date())
        
    # def select(self):
        # print(self.calendar.get_date)
        # self.date.set(self.calendar.get_date())
    # def validate(self):
    #     # sel = self.calendar.selection
    #     print(sel.strftime('%x'))
    #     if sel is not None:
    #         self.date.set(sel.strftime('%x'))
    #         # label.configure(text='Selected date: %s' % sel.strftime('%x'))
    
        

    # def get_data(self,event):
    #     print("treeview")
#================================= FUNCTIONS ==============================================#\
    def databseCon(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        return cur 

    def roll_search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM attendence WHERE roll=?",(self.roll.get(),))
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

    def date_search(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM attendence WHERE date=?",(self.date1.get(),))
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
        

    def done(self):
        self.show()
        # rows=self.databseCon()
        # pcount=0
        # acount=0
        # for row in rows:
        #     if "Present" in row:
        #         pcount+=1
        #     elif "Absent" in row:
        #         acount+=1
        # self.lbl_present.config(text=f"Present {str(pcount)}")
        # self.lbl_absent.config(text=f"Absent {str(acount)}")
        # self.lbl_total.config(text=f"Present {str(len(rows))}")

    def date_func(self):
        # Label(self.frame1,text="Select").pack(padx=10,pady=10)
        self.date.get()

    def take_atten(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT roll , name , course FROM student")
            rows=cur.fetchall()
            # print(rows)
            status="Absent"
            for row in rows:
                cur.execute("INSERT INTO attendence (roll,name,course,date,status) values(?,?,?,?,?)",
                (row[0],row[1],row[2],self.date.get(),status))
            con.commit()
            con.close()
            self.show()
        except Exception as e:
            print(e)
    def clear(self):
        self.CourseTable.delete(*self.CourseTable.get_children())
        self.CourseTable1.delete(*self.CourseTable1.get_children())
        self.lbl_present.config(text="Present ")
        self.lbl_absent.config(text="Absent ")
        self.lbl_total.config(text="Total ")

    def show(self):
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT roll , name , course FROM student")
            rows=cur.fetchall()
            
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row,tags="unchecked")   # by default box in unchecked
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def toggleCheck(self,event):  #accept event and identify row
        try:
            
            rowid=self.CourseTable.identify_row(event.y)
            # print(type(self.CourseTable.item(rowid,"tags")))
            tag=self.CourseTable.item(rowid,"tags")[0]   #get current state , tags will be in tuple so 1st element is tag checked or uncheck
            tags= list(self.CourseTable.item(rowid,"tags")) #this will return tags list  # convert tags into list so remove the current state of tags
            tags.remove(tag)  # remove current tag
            self.CourseTable.item(rowid,tags=tags) # this will set empty tag , reset the tag
            if tag=="checked":
                self.data(tag)
                # print("Absent")
                self.CourseTable.item(rowid,tags="unchecked")
            else:
                self.data(tag)
                # print("Present")
                self.CourseTable.item(rowid,tags="checked")
        except Exception as e:
            print(e)

    def data(self,tag):
        
        r=self.CourseTable.focus()   # focus on where we click cursor and that stores in r
        content=self.CourseTable.item(r) # to get item , get r 
        row=content["values"] 
        # print(row[0],row[1],row[2])
        status="Present"
        if(tag=="checked"):
            status="Absent"
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute("UPDATE attendence set status=? WHERE roll=? and date=?",
            (
                status,row[0],self.date.get()
            ))

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        con.commit()

            




if __name__=="__main__":
    root=Tk()         #create object of tkinter module
    obj=attendenceClass(root)     #create object of RMS class and pass root obj
    root.mainloop()  #for continously show on screen