#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:04:28 2018

@author: life4code
"""

import cv2
import numpy as np
#create a black image
image = np.zeros((512,512,3), np.uint8)
#can we make this in black and white ?
image_bw = np.zeros((512,512),np.uint8)
cv2.imshow("Black Rectangle(color)",image)
cv2.imshow("Black Rectangle(B&W)",image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()
    


#lets draw a line!
#cv2.line(image,starting coordinate,ending coor, color, thickness)
image = np.zeros((512,512,3),np.uint8)
cv2.line(image,(200,200),(512,512),(255,127,0),5)
cv2.imshow("Blue Line",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#lest draw rectangle !
#cv2.rectange(image,starting vertex, opposite vertex, color, thickness)
image = np.zeros((512,512,3),np.uint8)
cv2.rectangle(image, (100,100),(300,250),(127,50,127),5)
cv2.imshow("rectange",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#lets draw a circle
#cv2.circle(image,center,radius,color,fill)
image =  np.zeros((512,512,3),np.uint8)
cv2.circle(image,(350,350),100,(15,75,50),-1)
cv2.imshow("circle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#lets draw a polygon
image = np.zeros((512,512,3),np.uint8)

#lets define 4 point
pts = np.array([[10,50],[400,50],[90,200],[50,500]], np.int32)
#lets now reshape our points in form required by polylines
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,0,255),3)
cv2.imshow("Polygon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#HOW BOUT ADDING TEXT COK!!!?
#cv2.putText(image,'text to display', bottom left starting point, font, font size, color, thickness)
image = np.zeros((512,512,3),np.uint8)

cv2.putText(image,'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2,(100,170,3),3)
cv2.imshow('KONTEXST', image)
cv2.waitKey(0)
cv2.destroyAllWindows()