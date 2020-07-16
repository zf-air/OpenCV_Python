import cv2
import numpy as np
 
img = cv2.imread("part3/lambo.png")
# shape (height,width)
print(img.shape)
 
# resize(img,(width,height))
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)
 
# 裁剪 [height,width]
imgCropped = img[0:200,200:500]
 
cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
 
cv2.waitKey(0)