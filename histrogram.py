#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:49:13 2018

@author: life4code
"""

import cv2
import numpy as np

#import matplotlib to create histrogram plots
from matplotlib import pyplot as plt

image = cv2.imread('Lenna.png')
histrogram = cv2.calcHist([image],[0],None,[256],[0,256])

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
#channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
#mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
#histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
#ranges : this is our RANGE. Normally, it is [0,256].

#plot a histrogram, ravel() flatens our image array which 2 dimensions array into 1 array
plt.hist(image.ravel(), 256, [0,256], plt.show)

#viewing seperate color channels 
color = ('b','g','r')

#we now seperate the colors and plot each in the histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color = col)
    plt.xlim([0,256])
    
plt.show()

