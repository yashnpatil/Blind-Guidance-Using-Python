from gtts import gTTS 
import os 
from PIL import Image
import pytesseract

import speech_recognition as sr
import numpy as np
import cv2

def text_rec():
    print(sr.__version__) # just to print the version not required
    r = sr.Recognizer()
    my_mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index
    with my_mic as source:
        print("Say now!!!!")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source) #take voice input from the microphone
  
    if 'read' in r.recognize_google(audio):
        cap = cv2.VideoCapture(0)
  #  videoCaptureObject.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
   # videoCaptureObject.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        result = True
        while(result):
            ret,frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) 
            cv2.imshow('frame',frame)
        #if 'take' in r. recognize_google(audio):
            cv2.imwrite("./sample1.jpeg",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            result = False
            cap.release()
            cv2.destroyAllWindows()


    im = Image.open('C:/Users/prath/Downloads/BLIND_PERSON_TEXT_OBJECT_FACE_VOICE/sample1.jpeg')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(im, lang = 'eng')

    f=open("text.txt","w+")
    f.write(text)
    f.close()
   
    f=open('C:/Users/prath/Downloads/BLIND_PERSON_TEXT_OBJECT_FACE_VOICE/text.txt') 
    mytext=f.read()
  
    language = 'en'
  
    myobj = gTTS(text=mytext, lang=language, slow=False) 
  
    myobj.save("welcome.mp3") 
  
    os.system("start welcome.mp3")  
#print(text)


#text_rec()
