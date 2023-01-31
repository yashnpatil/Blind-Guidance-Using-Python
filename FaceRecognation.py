import cv2
import numpy as np 
import sqlite3

import mysql.connector as con
import os
#conn = sqlite3.connect('database.db')
#c = conn.cursor()
import datetime
import time 
from datetime import timedelta
def mark_attend():
  name=""
  fname = "recognizer/trainingData.yml"
  if not os.path.isfile(fname):
    print("Please train the data first")
    exit(0)
  face_cascade = cv2.CascadeClassifier('haar.xml')
  cap = cv2.VideoCapture(0)
  recognizer = cv2.face.LBPHFaceRecognizer_create()
  recognizer.read(fname)
  if True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
      ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
      #print(conf)
      nn=log(ids)
      
      
      #print(nn)
      for i in nn:
        print (i[1])
        name=i[1]
        
                
        
      
      
      
      
   
      if conf < 100:
        cv2.putText(img, name, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
      else:
        cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.imshow('Face Recognizer',img)
    time.sleep(5)
    
  cap.release()
  cv2.destroyAllWindows()
  return name


def log(id):
    flag=str(id)
    db = con.connect(host="localhost", user="root", password="", database="db_blind_master")
    cur = db.cursor()
    
    query="select * from tbl_relatives where id='"+flag+"'"
    cur.execute(query)
    names=cur.fetchall()
    for row in names:
       return names
       #print(row[1])

    #print(names)
    db.commit()
    #if(len(names)>0):
     #   return row
    #else:
     #   return 'no record'

