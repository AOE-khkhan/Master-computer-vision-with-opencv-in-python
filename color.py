#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 01:59:17 2018

@author: life4code
"""
#importing
import cv2
import numpy as np

#BGR
img = cv2.imread("Lenna.png")
cv2.imshow("jos",img)
B, G, R = img[0, 0]
print B, G, R
print shape.img


#color space HSV
#infact HSV is very useful in color filtering
image = cv2.imread('Lenna.png')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:,:,0])
cv2.imshow('Saturation Channel', hsv_image[:,:,1])
cv2.imshow('Value channel', hsv_image[:,:,2])

cv2.waitKey()
cv2.destroyAllWindows()

#
#OpenCV split functions splites the image into each color index

image = cv2.imread("rbg.png")
B, G, R= cv2.split(image)

print B.shape
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()
#lets merge the image
merged = cv2.merge([R,G,B])
cv2.imshow("Merged",merged)
cv2.waitKey(0)
cv2.DestroyAllWindows()
#lets amplify the blue color
merged = cv2.merge([R+100,G,B])
cv2.imshow('Merged Amplify Blue Color',merged)
cv2.waitKey(0)
cv2.DestroyAllWindows()
#Lets create a matrix of zeros
#with the dimensions of the image h x w
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.DestroyAllWindows()






