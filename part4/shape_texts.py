import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]= 255,0,0
# line(src,start_point,end_point,color,line_width)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

# 矩形 (src,start_point,end_point,color,line_width/cv2.FILLED(填充))
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.rectangle(img,(0,0),(250,300),(0,0,255),cv2.FILLED)

# 圆形 (src,圆心，半径，color,line_width)
# cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.circle(img,(400,50),30,(255,255,0),cv2.FILLED)

# 文本框 (src,text,point,font,比例尺(一般为1),color,line_width)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
 
cv2.imshow("Image",img)
cv2.waitKey(0)