import cv2
import numpy

image = cv2.imread('Lenna.png')
height, width = image.shape[:2]

#lets get starting pixel coordinates (top left of cropping rectangle)
start_row, start_col = int(height * .25), int(width * .25)

#lets get the ending pixel coordinates (bottom right)
end_row, end_col = int(height * .75), int(height * .75)

#simply use indexing to crop out the rectangle we desire 
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.imshow('cropped image',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()