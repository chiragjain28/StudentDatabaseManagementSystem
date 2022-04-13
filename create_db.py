import sqlite3


def create_db():
    con=sqlite3.connect(database="rms.db")  # make connection of Sqlite3
    cur=con.cursor() # cursor helps to execute the sql queries
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text , description text)")
    con.commit()  # create course table 

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,password text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()  # create student table

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()  # create result table 

    cur.execute("CREATE TABLE IF NOT EXISTS employe(eid INTEGER PRIMARY KEY AUTOINCREMENT,fname text,lname text,contact text,email text,password text,photo BLOB)")
    con.commit() # create employe table 

    cur.execute("CREATE TABLE IF NOT EXISTS user(eid INTEGER PRIMARY KEY AUTOINCREMENT,fname text,lname text,contact text,email text,password text,photo BLOB)")
    con.commit() # create employe table 

    cur.execute("CREATE TABLE IF NOT EXISTS momo(email text)")
    con.commit() # create employe table 

    cur.execute("CREATE TABLE IF NOT EXISTS attendence(roll text , name text ,course text,date text , status text)")
    con.commit() # create employe table

    con.close()

create_db()