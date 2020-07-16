import cv2
import numpy as np

img = cv2.imread("part5/cards.jpg")
 
width,height = 250,350
# 原图的四个点坐标
pts1 = np.float32([[111,219],[287,188],[352,440],[154,482]])
# 转换后的四个点坐标，点坐标位置需要对应
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
# 获得透视转换矩阵
matrix = cv2.getPerspectiveTransform(pts1,pts2)
# 获得目标图像(src,matrix,(width,height))
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
 
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)