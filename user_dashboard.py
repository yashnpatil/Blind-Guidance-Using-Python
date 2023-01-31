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
##    w = filename.image2.width()
##    h = filename.image2.height()
    screen3.geometry('%dx%d+0+0' % (1200,700))
    Label(screen3, text="Blind Person Guidance System", bg="Gray", height=2, width=250,font=("Arial Bold", 24)).pack()

    tool_bar = Frame(width=50, height=185, bg='lightgrey')
    tool_bar.pack(side='left', fill='both', padx=1, pady=1, expand=True)
 
    filter_bar = Frame(width=50, height=185, bg='lightgrey')
    filter_bar.pack(side='right', fill='both', padx=1, pady=1, expand=True)


    
  


    #Label(screen3, text="", bg="white").pack()
    b5 =  Button(tool_bar,text="Object Detection",height=2,width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=object_detection)
    
    b5.pack(padx=5, pady=5)
    Label(screen3, text="", bg="white").pack()
    b6=Button(filter_bar,text="Person Detection",height=2,width=50,bg="black",fg="red",font=("Arial Bold", 15),command=person_detection)
    b6.pack(padx=5, pady=5)
    #Label(screen3, text="", bg="white").pack()
    b7= Button(tool_bar, text="Text Recognation",height=2,width=50,bg="black",fg="yellow",font=("Arial Bold", 15),command=text_detection)
    b7.pack(padx=5, pady=5)
    #Label(screen3, text="", bg="white").pack()
    b8 = Button(filter_bar, text="Exit", height=2, width=50,bg="black",fg="blue",font=("Arial Bold", 15),command=screen3.destroy)
    b8.pack(padx=5, pady=5)



    C= Canvas(screen3)
    
    background_label = Label(screen3, image=filename)
    C.pack()
    

    

    Label(screen3, text="", bg="green").pack()
    b9 =  Button(screen3,text="Exit",height=2,width=50,bg="Black",fg="green",font=("Arial Bold", 15),command=screen3.destroy)
    b9.pack()





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
    
main_screen()

