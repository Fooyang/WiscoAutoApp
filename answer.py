import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

# used for trackbars:
# def nothing(x):
#     pass

# trackbars defining lower and upper bounds for HSV values:
# cv.namedWindow('Trackbars')
# cv.resizeWindow('Trackbars',600,250)
# cv.createTrackbar('HueMin','Trackbars',0,180,nothing)
# cv.createTrackbar('HueMax','Trackbars',180,180,nothing)
# cv.createTrackbar('SatMin','Trackbars',0,255,nothing)
# cv.createTrackbar('SatMax','Trackbars',255,255,nothing)
# cv.createTrackbar('ValMin','Trackbars',0,255,nothing)
# cv.createTrackbar('ValMax','Trackbars',255,255,nothing)

# find HSV values for mask using trackbar:
# while True: 
#     img = cv.imread('Photos/red.png')
#     hmin = cv.getTrackbarPos('HueMin','Trackbars')
#     hmax = cv.getTrackbarPos('HueMax','Trackbars')
#     smin = cv.getTrackbarPos('SatMin','Trackbars')
#     smax = cv.getTrackbarPos('SatMax','Trackbars')
#     vmin = cv.getTrackbarPos('ValMin','Trackbars')
#     vmax = cv.getTrackbarPos('ValMax','Trackbars')
#     lower = np.array([hmin,smin,vmin])
#     higher = np.array([hmax,smax,vmax])
#     mask = cv.inRange(img, lower, higher)
#     final_result = cv.bitwise_and(img, img, mask=mask)
#     cv.imshow('Final Output', final_result)
#     cv.imshow('mask',mask)
#     cv.waitKey(1)

#result from finding HSV through trackbars:
    #lower - h = 0, s = 7, v = 135
    #high - h = 36, s = 56, v = 255

#import image
img = cv.imread('Photos/red.png')
#set low/high bounds
low_red = np.array([0,7,135])
high_red = np.array([36,56,255])
#mask image
mask = cv.inRange(img, low_red, high_red)

directory = r'C:\Users\felix\OneDrive\Desktop\Wisconsin Autonomous\Photos'
os.chdir(directory)

#show original and masked image
# cv.imshow('image',img)
# cv.imshow('mask',mask)

#resize so entire img can be viewed on screen
resized_original = cv.resize(img,(460,560))
resized = cv.resize(mask, (460, 560))
final_resized = cv.resize(img,(460,560))
# cv.imshow('resized',resized)
cv.imshow('resized', resized_original)

#split image in half to get end points for the left and right lines
left = resized[:, 0:460//2].copy()
right = resized[:, 460//2:460].copy()

cv.imshow('left',left)
cv.imshow('right',right)

left_highest = np.array([0,0])
left_lowest = np.array([0,0])
right_highest = np.array([0,0])
right_lowest = np.array([0,0])

#find left line end points by searching for cells not equal to zero (black)
for i in range(0,left.shape[0]):
     for j in range(0,left.shape[1]):
        if left[i,j] != 0:
            if left[left_highest[0],left_highest[1]] == 0:
                left_highest = np.array([i,j])
            elif left_highest[0] > i:
                left_highest = np.array([i,j])
            elif left_highest[0] == i:
                if left_highest[1] < j:
                    left_highest = np.array([i,j])
            
            if left[left_lowest[0],left_lowest[1]] == 0:
                left_lowest = np.array([i,j])
            elif left_lowest[0] < i:
                left_lowest = np.array([i,j])
print(left_highest)
print(left_lowest)

#find right line end points by searching for cells not equal to zero
for i in range(0,right.shape[0]):
     for j in range(0,right.shape[1]):
        if right[i,j] != 0:
            if right[right_highest[0],right_highest[1]] == 0:
                right_highest = np.array([i,j])
            elif right_highest[0] > i:
                right_highest = np.array([i,j])
            elif right_highest[0] == i:
                if right_highest[1] > j:
                    right_highest = np.array([i,j])
            
            if right[right_lowest[0],right_lowest[1]] == 0:
                right_lowest = np.array([i,j])
            elif right_lowest[0] < i:
                right_lowest = np.array([i,j])
            elif right_lowest[0] == i:
                if right_lowest[1] < j:
                    right_lowest = np.array([i,j])      
print(right_highest)
print(right_lowest)  

# highest and lowest pixel for cones on left side
# [184 145]
# [64 383]

# calculated slope: 120/238
# adjusted coordinates: [256,0] [0,511]

# highest and lowest pixel for cones on right side
# [282 149]
# [407 389]

# calculated slope: 125/240
# adjusted coordinates: [208,0] [460,495]

#drawing lines using highest and lowest pixel on cones (does not cover entire image)
#swap x and y pairs so the coordinates are actually x,y instead of y,x
# left_highest[0],left_highest[1] = left_highest[1],left_highest[0]
# left_lowest[0],left_lowest[1] = left_lowest[1],left_lowest[0]
# right_highest[0],right_highest[1] = right_highest[1] + 230,right_highest[0]
# right_lowest[0],right_lowest[1] = right_lowest[1] + 230,right_lowest[0]

# cv.line(final_resized,left_lowest,left_highest,(0,0,255),1)
# cv.line(final_resized,right_lowest,right_highest,(0,0,255),1)

# drawing line spanning the entire image
cv.line(final_resized,[0,511],[256,0],(0,0,255),1)
cv.line(final_resized,[460,495],[208,0],(0,0,255),1)

cv.imshow('final',final_resized)
cv.imwrite('answer.png', final_resized)
       
cv.waitKey(0)