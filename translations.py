import cv2
import numpy as np

image = cv2.imread("Lenna.png")
#store height and width of the image

height, width, = image.shape[:2]
quarter_height, quarter_width = height/4, width/4

#
# T = | 1 0 Tx |
#     | 0 1 Ty |
#T is our transformation matrix
T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])
#We use warpaffine to transform the image using matrix 
img_translation = cv2.warpAffine(image,T,(width,height))
cv2.imshow('Translation',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()