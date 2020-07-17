import cv2

# 加载级联分类器
faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 一定要加下面这一行，否则会发生错误
faceCascade.load('E:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread('part1/lena.png')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# # 检测人脸
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
# 遍历并绘制矩形框
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 
cv2.imshow("Result", img)
cv2.waitKey(0)