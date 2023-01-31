# Python program to translate 
# speech to text and text to speech 
  
  
import speech_recognition as sr 
import pyttsx3
import object_detection as od
import cv2
flag=False
#def object_detection():
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


# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      
      
# Loop infinitely for user to 
# speak

def call():
    global c_text

    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower()
            c_text=MyText
            
  
            print("Did you say "+MyText)
            SpeakText(MyText)
            #MyText.replace(" ","1")
            print(MyText)
            if(MyText=="person detection" or MyText=="person"):
                print("face Recognation Activated..")
                person_detection()

            if(MyText=="object detection" or MyText=="object"):
                print("Object Recognation Activated..")
                
                object_detection()
                

            if(MyText=="text" or MyText=="text"):
                print("Text Detection Activated..")
                text_detection()
                

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured")
        
       
        
        if(c_text=="person detection" or c_text=="person"):
                print("face Recognation Activated..")
                person_detection()

        if(c_text=="object detection" or c_text=="object"):
                print("Object Recognation Activated..")
                
                object_detection()
                

        if(c_text=="text recognation" or c_text=="text"):
                print("Text Detection Activated..")
            
while(1):
    print("...")
    
    call()
