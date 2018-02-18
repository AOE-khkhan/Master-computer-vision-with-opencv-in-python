import cv2
import numpy as np

image = cv2.imread('Lenna.png')
cv2.imshow('original',image)

#create a matrix of ones, then multiply it by a scalar of 100
#This gives a matrix with same dimension of our image with all values being 100
M = np.ones(image.shape,dtype = "uint8") * 75

#We use this to add this matrix M, to our image
#notice the increase of brightness

added = cv2.add(image, M)
cv2.imshow('Added',added)
cv2.waitKey(0)
cv2.destroyAllWindows()

subtracted = cv2.subtract(image,M)
cv2.imshow('substract',subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()