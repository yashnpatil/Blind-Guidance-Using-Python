import mysql.connector as con
import sys
import mysql



def delete(id):
    db = con.connect(host="localhost", port=3306, user="root", password="", database="db_blind_master")
    cur=db.cursor()

    
    query="delete from  tbl_relatives where id="+str(id)
    
    cur.execute(query)
    db.commit()


def delete1(id):
    db = con.connect(host="localhost", port=3306, user="root", password="", database="db_blind_master")
    cur=db.cursor()

    
    query="delete from  tbl_relatives where id="+str(id)
    
    cur.execute(query)
    db.commit()

def conn4():
    db=con.connect(host="localhost", port=3306, user="root", password="", database="db_blind_master")
    cur = db.cursor()
    
    
    if mysql.connector.connect():
        print("Database is Connected")
        cur.execute("select * from tbl_relatives")
        data = cur.fetchall()
        #for row in data:
        print (data)




def conn5(id,name,mobile,relation):
    db = con.connect(host="localhost", port=3306, user="root", password="", database="db_blind_master")
    cur=db.cursor()

    #id, name, mobile, address, crime_details, adh_, em_, crime_code
    query="insert into tbl_relatives(id,name,relation,mobile) values(%s,%s,%s,%s)"
    value=[id,name,relation,mobile]
    cur.execute(query,value)
    db.commit()
    #tkMessageBox.showinfo("Information", "Person Added Successfull")
    







        
        

    

