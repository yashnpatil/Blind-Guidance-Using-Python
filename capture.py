import time
import cv2 
def capture():
        
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:
            try:
                check, frame = webcam.read()
        #print(check) #prints true as long as the webcam is running
        #print(frame) #prints matrix values of each framecd 
                #cv2.imshow("Captured", frame)
                time.sleep(2)
        
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                time.sleep(2)
                #print("saved")
                webcam.release()
            
                cv2.waitKey()

                cv2.destroyAllWindows()
            
                
                break
        
            except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break




