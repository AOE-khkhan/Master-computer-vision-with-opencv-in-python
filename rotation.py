import cv2
import numpy as np

image = cv2.imread('Lenna.png')

height, width = image.shape[:2]

#divided by 2 to rototate the image around its centre
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2),90,.5)
rotated_image = cv2.warpAffine(image, rotation_matrix,(width, height))
cv2.imshow('Rotated image',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


