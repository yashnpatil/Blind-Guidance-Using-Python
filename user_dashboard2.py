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
import speech_recognition as sr 
import pyttsx3

r = sr.Recognizer()  
  
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 

    
def main_screen2():
    global screen4
    screen4=Toplevel()

    C= Canvas(screen4, height=250, width=300)
    filename = ImageTk.PhotoImage(Image.open('186040.gif'))
    #background_label = Label(screen4, image=filename)
   # background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #C.create_image(0,0,anchor=NW, image=filename)
    #C.pack()
    screen4.title("DASHBOARD_2")
    screen4.geometry('720x720')
    filename.image2 =ImageTk.PhotoImage(Image.open('186040.gif'))
    #image = ImageTk.PhotoImage(image2)
##    w = filename.image2.width()
##    h = filename.image2.height()
    screen4.geometry('%dx%d+0+0' % (1200,700))
    Label(screen4, text="Blind Person Guidance System", bg="Gray", height=2, width=250,font=("Arial Bold", 24)).pack()

    tool_bar = Frame(width=50, height=185, bg='lightgrey')
    tool_bar.pack(side='left', fill='both', padx=1, pady=1, expand=True)
 
    filter_bar = Frame(width=50, height=185, bg='lightgrey')
    filter_bar.pack(side='right', fill='both', padx=1, pady=1, expand=True)


    
  






    C= Canvas(screen4)
    
    background_label = Label(screen4, image=filename)
    C.pack()
    
    Label(screen4, text="", bg="white").pack()
    b11 =  Button(screen4,text="Object Detection",height=2,width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=object_detection)
    b11.pack()
    
    Label(screen4, text="", bg="white").pack()
    b12=Button(screen4,text="Person Detection",height=2,width=50,bg="black",fg="red",font=("Arial Bold", 15),command=person_detection)
    b12.pack()

    #Label(screen3, text="", bg="white").pack()
    b13= Button(screen4, text="Text Recognation",height=2,width=50,bg="black",fg="yellow",font=("Arial Bold", 15),command=text_detection)
    b13.pack()

    Label(screen4, text="", bg="white").pack()
    b14 = Button(screen4, text="Exit", height=2, width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=screen4.destroy)
    b14.pack()
    

#    Label(screen4, text="", bg="green").pack()
 #   b15 =  Button(screen4,text="Exit",height=2,width=50,bg="Black",fg="green",font=("Arial Bold", 15),command=screen4.destroy)
 #   b15.pack()





import object_detection as od
def object_detection():
    objects=od.counting()
    print(objects)
    final=objects[1:]
    print("objects detected are "+final)
    SpeakText("objects detected are "+final)
    
    
    
import FaceRecognation
def person_detection():
    
    person=FaceRecognation.mark_attend()
    print("Person Detected is "+person)
    SpeakText("Person Detected is "+person)

##### Edited by me####

import image_example
def text_detection():
    text=image_example.text_rec()
    print(""+text)
    SpeakText(""+text)

##### Edited by me####


def backandclose():
    os.system('python dashboard.py')
    window.destroy()
    window.quit()
    
main_screen2()

