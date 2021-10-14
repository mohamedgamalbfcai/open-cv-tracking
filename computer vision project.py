# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:54:00 2021

@author: mohamed gamal
"""

import cv2
#import numpy as np
#import matplotlib.pyplot as plt

#capturing video file
cap = cv2.VideoCapture("vehicles.mp4")

#background substitution to generate binary img
object_detector = cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=90)



while True:
    ret,frame =cap.read()
    height, width, _ = frame.shape
    #print(height,width)
    #extraxt region of interest
    roi = frame[200: 720,300: 1700]
    #mask identification
    mask= object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    contours, _ =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>100:
            cv2.drawContours (roi , [cnt] , -1 , (0,255,0) , 2)
            #x, y, w, h = cv2.boundingRect(cnt)
            #cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 4)
    cv2.imshow("roi",roi)
    cv2.imshow("highway",full frame)
    cv2.imshow("mask",mask)
    #cv2.imshow("highway",frame)
    key=cv2.waitKey(30)
    if key==27:
        break
cap.release()
cv2.destroyllWindows()
