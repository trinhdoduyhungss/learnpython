import cv2
import numpy as np
img = cv2.imread("ovuong.png")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.resize(img2, (20, 20))
x2= np.array(img2)
#print(x2)
count_do1 = 0
count_do2 = 0
count_trang = 0
for i in range(len(x2)):
   for y in range(len(x2[i])):
       if (x2.item((i,y)) == 90):
           count_do1 += 1
           #print('x2.item(('+str(i)+','+str(y)+')) '+str(count))
       if (x2.item((i,y)) == 91):
           count_do2 += 1
           # print('x2.item(('+str(i)+','+str(y)+')) '+str(count))
       elif (x2.item((i,y)) == 248):
           count_trang += 1

print('Số ô màu đỏ : ',(count_do1+count_do1/4+count_do2)/4 +1) #2 dòng một ô, mỗi ô = 4 lần 90
print('số ô mày trắng :', (count_trang+count_trang/4)/4)