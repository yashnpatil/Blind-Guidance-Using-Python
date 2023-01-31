import numpy as np
import argparse
import cv2 as cv
import subprocess
import time
import os
from yolo_utils import infer_image, show_image
my_list = list()
import mysql.connector as con
import capture


FLAGS = []
memory_=[]
boxes = []
confidences = []
classIDs = []
classname = []
memory_names=['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']

##	# Get the labels
labels = open("./yolov3-coco/coco-labels").read().strip().split('\n')

	# Intializing colors to represent each label uniquely
colors = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

	# Load the weights and configutation to form the pretrained YOLOv3 model
net = cv.dnn.readNetFromDarknet("./yolov3-coco/yolov3.cfg", "./yolov3-coco/yolov3.weights")

	# Get the output layer names of the model
layer_names = net.getLayerNames()
layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        
##	    print ('Neither path to an image or path to video provided')
##	    print ('Starting Inference on Webcam')
def unique(list1): 
  
    # intilize a null list 
    unique_list = []
    for x in list1:
            if x not in unique_list:
                    unique_list.append(x)
    return unique_list
        
 
 

    

def counting():
        #time.sleep(3)
        capture.capture()
        count = 0
        try:
                img = cv.imread('saved_img.jpg')
                height, width = img.shape[:2]
        except:
                raise 'Image cannot be loaded!\n\
                        Please check the path provided!'

        finally:
                img,_,confidences, classidp, idxs = infer_image(net, layer_names, height, width, img, colors, labels, FLAGS)
                #show_image(img)
                count1=0
                count = (count + 1) % 6
                #print(classidp)
                namess=""
                print(classidp)
                class_id=unique(classidp)
                for ii in class_id:
                        namess=namess+","+memory_names[ii]
                        
##                        print(memory_)
##                        print(namess)
                return namess
                        
            
                
	# Do inference with given image'
     
                
#counting()

    
    
