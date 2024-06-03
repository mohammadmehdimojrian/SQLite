import sqlite3
import datetime

def creat_table(con:sqlite3.Connection,cur:sqlite3.Cursor):
    cur.execute("CREATE TABLE IF NOT EXISTS Expenses(id integer primary key autoincrement,date TEXT,type,cost,explain)")
    con.commit()

def insert_table(con:sqlite3.Connection,cur:sqlite3.Cursor):
    print()
    cost=float(input("Enter your cost$: "))
    while True:
        try:
            year=int(input("Enter your year for cost: "))
            month=int(input("Enter your month for cost: "))
            day=int(input("Enter your day for cost: "))
            hour=int(input("Enter your hour for cost: "))
            minute=int(input("Enter your minute for cost: "))
            date=datetime.datetime(year,month,day,hour,minute)
            date=str(date)
            break
        except Exception:
            print("your date is not correct.......")
    type=input("Enter your type : ")
    explain=input("type your explain: ")
    entity=None,date,type,cost,explain
    cur.execute("INSERT INTO Expenses VALUES(?,?,?,?,?)",entity)
    con.commit()

def update_table(con:sqlite3.Connection,cur:sqlite3.Cursor):
    print()
    up_id=int(input("Enter the id for update: "))
    while True:
        print("which item do you like to update the ID details %i ?\n1-cost:\n2-date:\n3-type:\n4-explain:\n5-exit on update:"%up_id)
        num_up=int(input("Enter the num: "))
        if num_up==1:
            cost=int(input("Enter your new cost: "))
            cur.execute("UPDATE Expenses SET cost=%i WHERE id=%i"%(cost,up_id))
            con.commit()

        elif num_up==2:
            while True:
                print()
                try:
                    year =int(input("Enter your year for cost: "))
                    month =int(input("Enter your month for cost: "))
                    day =int(input("Enter your day for cost: "))
                    hour =int(input("Enter your hour for cost: "))
                    minute =int(input("Enter your minute for cost: "))
                    date =datetime.datetime(year, month, day, hour, minute)
                    date =str(date)
                    cur.execute("UPDATE Expenses SET date='%s' WHERE id=%i" %(date, up_id))
                    con.commit()
                    break
                except Exception:
                    print("The date is not correct!,please try again...")

        elif num_up==3:
            type_up=input("Enter your new type: ")
            cur.execute("UPDATE Expenses SET type= '%s' WHERE id= %i" %(type_up,up_id))
            con.commit()
        elif num_up==4:
            explainup=input("type new explain: ") 
            cur.execute("UPDATE Expenses SET explain= '%s' WHERE id=%i" %(explainup,up_id))
            con.commit()
        elif num_up==5:
            break

def delete_table(con:sqlite3.Connection,cur:sqlite3.Cursor):
    id_del_up=int(input("Enter your id for DELETE: "))
    cur.execute("DELETE FROM Expenses WHERE id=%i"%id_del_up)
    con.commit()
def viewer_table(con:sqlite3.Connection,cur:sqlite3.Cursor):
    print()
    cur.execute("SELECT * FROM Expenses")
    lis=cur.fetchall()
    for i in lis:
        print(i)

con=sqlite3.connect('mydb.db')
cur=con.cursor()
creat_table(con,cur)
while True:
    print()
    print("Enter your actvity:\n1-insert the cost\n2-view the cost\n3-update the cost\n4-delete the cost\n5-Exit")
    num=int(input("Enter your work: "))
    if num==1:
        insert_table(con,cur)
    elif num==2:
        viewer_table(con,cur)
    elif num==3:
        update_table(con,cur)
    elif num==4:
        delete_table(con,cur)
    elif num==5:
        exit()
    else:
        print("not found!,please try again...")
