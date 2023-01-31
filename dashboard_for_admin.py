import cv2
import numpy as np 
import sqlite3
import os
from PIL import ImageTk
from tkinter import *

from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import tkinter.messagebox
global var
from tkinter import messagebox
import TrainModule
from dbConnection import conn5
from PIL import ImageTk,Image

global screen

    
def main_screen():
    global screen3
    screen3=Tk()
    
    C= Canvas(screen3, height=250, width=300)
    filename = ImageTk.PhotoImage(Image.open('186040.gif'))
    background_label = Label(screen3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.create_image(0,0,anchor=NW, image=filename)
    C.pack()
    screen3.title("DASHBOARD")
    screen3.geometry('720x720')
    filename.image2 =ImageTk.PhotoImage(Image.open('186040.gif'))
    #image = ImageTk.PhotoImage(image2)
    #w = filename.image2.width()
    #h = filename.image2.height()
    screen3.geometry('%dx%d+0+0' % (1200,700))
    Label(screen3, text="Blind Person Guidance System", bg="white", height=2, width=250,font=("Arial Bold", 24)).pack()

    tool_bar = Frame(width=50, height=185, bg='white')
    tool_bar.pack(side='left', fill='both', padx=1, pady=1, expand=True)
 
    filter_bar = Frame(width=50, height=185, bg='lightgrey')
    filter_bar.pack(side='right', fill='both', padx=1, pady=1, expand=True)


    
  


    #Label(screen3, text="", bg="white").pack()
    b5 =  Button(tool_bar,text="Add Relative's Record",height=2,width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=attend)
    
    b5.pack(padx=5, pady=5)
    Label(screen3, text="", bg="white").pack()
    b6=Button(filter_bar,text="Train Model",height=2,width=50,bg="black",fg="red",font=("Arial Bold", 15),command=train_model)
    b6.pack(padx=5, pady=5)
    #Label(screen3, text="", bg="white").pack()
    b7= Button(tool_bar, text="View Relatives",height=2,width=50,bg="black",fg="yellow",font=("Arial Bold", 15),command=view_attendance)
    b7.pack(padx=5, pady=5)
    #Label(screen3, text="", bg="white").pack()
    b8 = Button(filter_bar, text="BUTTON INPUT", height=2, width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=open_user)
    b8.pack(padx=5, pady=5)


    b9= Button(tool_bar, text="VOICE INPUT",height=2,width=50,bg="black",fg="yellow",font=("Arial Bold", 15),command=open_voice)
    b9.pack(padx=5, pady=5)
    #Label(screen3, text="", bg="white").pack()
    b10 = Button(filter_bar, text="Exit", height=2, width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=screen3.destroy)
    b10.pack(padx=5, pady=5)



    C= Canvas(screen3)
    
    background_label = Label(screen3, image=filename)
    C.pack()
    

    

    Label(screen3, text="", bg="green").pack()
    b9 =  Button(screen3,text="Exit",height=2,width=50,bg="Black",fg="green",font=("Arial Bold", 15),command=screen3.destroy)
    b9.pack()




def open_user():
    import user_dashboard2
   
def open_voice():
    import speetch
    

def train_model():
    TrainModule.train1()
import FaceRecognation
def mark_attnd():
    
    FaceRecognation.mark_attend()

def view_attendance():
    import view_relatives


def attend():
    global screen3
    global name1_
    global mobile1_
    global relation1_
   
    global variable
    screen3=Toplevel(screen3)


 

    
    screen3.configure(background='white')
    screen3.geometry('1280x720')
    Label(screen3, text="Relative Addition", font=("Arial Bold", 25),bg="grey",width=250,height=2).pack()
    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    
    name = Label(screen3, text="Name", height=2, bg="white",font=("Arial Bold", 11))
    name.pack()
    name1_ = Entry(screen3, width=60)
    name1_.pack()
   
   
    mobile = Label(screen3, text="Mobile", height=2, bg="white",font=("Arial Bold", 11))
    mobile.pack()
    mobile1_ = Entry(screen3, width=60)
    mobile1_.pack()

    class_ = Label(screen3, text="Relation", height=2, bg="white",font=("Arial Bold", 11))
    class_.pack()
    relation1_ = Entry(screen3, width=60)
    relation1_.pack()

    Label(screen3, text="", bg="white").pack()
    Label(screen3, text="", bg="white").pack()
    login = Button(screen3, text="Add Record", height=2, width=30,command=record_faces,bg="black",fg="white",font=("Arial Bold", 13))
    login.pack()





def record_faces():
    a=name1_.get()
    b=mobile1_.get()
    c=relation1_.get()
    
    
    print(a)
    path1 = 'dataset'
    model_detector='opencv_face_detector.pbtxt'
    imagePaths = [os.path.join(path1,f) for f in os.listdir(path1)]
    print(imagePaths)
  
    id=1;
    for imagePath in imagePaths:
    
    
        print(os.path.split(imagePath)[-1].split('.')[2])

    
        ID = int(os.path.split(imagePath)[-1].split('.')[2])
        if ID>id:
            id=ID
    if not os.path.exists('./dataset'):
        os.makedirs('./dataset')
#c = conn.cursor()
    face_cascade = cv2.CascadeClassifier('haar.xml')
    cap = cv2.VideoCapture(0)
    #uname = input("Enter your name: ")

    sampleNum = id+20
    while True:
      ret, img = cap.read()
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      for (x,y,w,h) in faces:
        id = id+1
        cv2.imwrite("dataset/User."+str(a)+"."+str(id)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.waitKey(100)
        conn5(id,a,b,c) 
      cv2.imshow('img',img)
      cv2.waitKey(1);
      if id > sampleNum:
         break
    cap.release()
    messagebox.showinfo("Information", "Relatives Info Added Successfully")
    
    #conn.commit()
    #conn.close()
    cv2.destroyAllWindows()
  


main_screen()
screen3.mainloop()
