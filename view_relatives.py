from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from dbConnection import conn4
from dbConnection import delete1
import os
import mysql.connector as con
import math



def view_relatives():

    def selectItem(a):
        curItem = tree.focus()
        gg=tree.item(curItem)
        print (gg)
        x = gg["values"]
        print(x)
        y=x[0]
        
        delete1(y)
        window.destroy()
        window.after(1000,view_relatives)
    global window
    window=Tk()
    tree = ttk.Treeview(window)
    


    window.title("View Relatives Record")
    image2 =Image.open('grayscale.jpg')
    image1 = ImageTk.PhotoImage(image2)
    w = image1.width()
    h = image1.height()
    window.geometry('%dx%d+0+0' % (w,h))
    filename =ImageTk.PhotoImage(Image.open('grayscale.jpg'))

    Label(window, text="Relatives Details", bg="Grey", height=1, width=250,font=("Arial Bold", 20), command = conn4()).pack()



    
    

    tree["column"] = ("Relative Name", "Relation", "Mobile")
    
    tree.column("Relative Name", width=150)
    tree.heading("Relative Name", text="Relative Name")
    tree.column("Relation", width=100)
    tree.heading("Relation", text="Relation")
    tree.column("Mobile", width=100)
    tree.heading("Mobile", text="Mobile")
    
    tree.bind('<ButtonRelease-1>', selectItem)
    db=con.connect(host="localhost", port=3306, user="root", password="", database="db_blind_master")
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name,relation,mobile FROM tbl_relatives")
    row = cur.fetchall()

    cpt = 0
    for i in row:
        #print(i)
        tree.insert('', 'end', values=i)
        #values=row.values(lenght(row))
    cpt += 1 # increment the ID
    tree.pack()

    back_button = Button(window, text="Back",  height=1, width=20,bg="Blue",fg="white",font=("Arial Bold", 10), command=backandclose)
    back_button.pack()

    Label(window, text="Click on a data to delete", bg="red", fg="white", height=1, width=250,font=("Arial Bold", 12)).pack()
    




def backandclose():
    os.system('python dashboard.py')
    window.destroy()
    window.quit()


view_relatives()
        
    

     
