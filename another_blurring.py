import cv2
import numpy as np

image = cv2.imread('Lenna.png')

blur=cv2.blur(image,(3,3))
cv2.imshow('Blur',blur)

Gaussian = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Gaussian',Gaussian)

median =cv2.medianBlur(image, 5)
cv2.imshow('median', median)

bilateral = cv2.bilateralFilter(image, 9,75,75)
cv2.imshow('bilateral', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()