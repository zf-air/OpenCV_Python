
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.png')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('imggray',img_gray)

cv2.waitKey(0)