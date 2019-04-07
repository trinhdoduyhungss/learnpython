import cv2
import numpy as np
img = cv2.imread("ovuong.png")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.resize(img2, (20, 20))
x2= np.array(img2)
#print(x2)
count = 0
for i in range(len(x2)):
   for y in range(len(x2[i])):
       if (x2.item((i,y)) == 90):
           count += 1
           #print('x2.item(('+str(i)+','+str(y)+')) '+str(count))


print((count+count/4)/4 +1) #2 dòng một ô, mỗi ô = 4 lần 90