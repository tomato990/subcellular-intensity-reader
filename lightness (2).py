import matplotlib.pyplot as plt
from pylsm import lsmreader
import cv2
import numpy as np


img = cv2.imread("AVG_C1-PBD-4-ctrl0009.tif")
imS = cv2.resize(img, (800, 800))

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img,(x,y),100,(255,0,0),-1)
        #print mouseX,mouseY
        mouseX,mouseY = [],[]
        #print x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        mouseX.append(x)
        mouseY.append(y)
        #print x, y
mouseX = []
mouseY = []
#img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',imS)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break
pointNum = len(mouseY)
print(len(mouseY))
jump = 1.0*pointNum/30
twentyX,twentyY = [],[]
for i in range(30):
    n = int(round(jump*i))
    #print n
    twentyX.append(mouseX[n])
    twentyY.append(mouseY[n])
print("\n")

for i in range(len(twentyX)):
    print(imS[twentyY[i]][twentyX[i]][1])
