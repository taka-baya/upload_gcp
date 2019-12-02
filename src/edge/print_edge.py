import os
import cv2
import numpy
import imutils

img1 = cv2.imread('edge_before.jpg')
img2 = cv2.imread('background.jpg')

img3 = cv2.resize(img2 , (1268,937))

print(img1.shape)
print(img3.shape)

result = cv2.Canny(img1, 400, 600)

print(result.shape)
backtorgb = cv2.cvtColor(result,cv2.COLOR_GRAY2RGB)

#for i in range(0,936):
#	for j in range(0,ß1267):
#		for k in range(0,2):
#			if backtorgb[i][j][k] != 0:
#				print("i:{0}, j:{1} ,k{2}".format(i,j,k))

for i in range(937):
	for j in range(0,1268):
		if(backtorgb[i][j][0] != 0):
			backtorgb[i][j] = [0,0,255]

#backtorgb[255,255,255] = [0,0,255]

print(backtorgb.shape)

blended = cv2.addWeighted(src1=img3,alpha=0.8,src2=backtorgb,beta=1.9,gamma=0)

cv2.imshow("image",blended)
cv2.waitKey(0)