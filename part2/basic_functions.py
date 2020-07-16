import cv2
import numpy as np

# 定义kernel,用于膨胀
kernel = np.ones((5, 5), dtype=np.uint8)

img = cv2.imread('part2/lena.png')
# 转灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 核大小必须为奇数，7*7   0是默认
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)

# canny边缘检测 设置两个阈值
img_canny = cv2.Canny(img, 150, 200)

# 膨胀 iterations越大，图像越粗
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)

# 腐蚀
img_erodeed = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow('gray', img_gray)
cv2.imshow('blur', img_blur)
cv2.imshow('canny', img_canny)
cv2.imshow('dilation', img_dilation)
cv2.imshow('eroded', img_erodeed)

cv2.waitKey(0)
