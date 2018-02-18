import cv2
import numpy as np

image = cv2.imread('Lenna.png')
cv2.imshow('original', image)


kernel_3x3=np.ones((3,3),np.float32) / 9

#we use cv2.filter2D to convolve the kernel with an image
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 kernel blurring',blurred )

kernel_7x7 = np.ones((7,7),np.float32) / 49
blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('blurred2',blurred2)

cv2.waitKey(0)
cv2.destroyAllWindows()