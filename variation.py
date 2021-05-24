import imutils

import cv2
import numpy as np
from PIL import Image
import glob, os

path = 'pic1.jpeg'

os.chdir("C:/Users/tadas.orentas/Desktop/boat_Imiges/test1")

for file in glob.glob("*.JPEG"):
    
    img = cv2.imread(file)
    cv2.imshow('control', img)
    image_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB )
    image_GRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )


    image_flip1 = cv2.flip(img, 1)
    image_flip2 = cv2.flip(image_RGB, 1)
    image_flip3 = cv2.flip(image_GRAY, 1) 
    # Displaying the image 
    #cv2.imshow('RGB', image_RGB)
    #cv2.imshow('GRAY', image_GRAY)
    #cv2.imshow('flip1', image_flip1)
    #cv2.imshow('flip2', image_flip2)
    #cv2.imshow('flip3', image_flip3)


    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # rotate our image by 45 degrees around the center of the image
    M = cv2.getRotationMatrix2D((cX, cY), 5, 1.0)
    mm = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
    rotated1 = cv2.warpAffine(img, M, (w, h))
    rotated2 = cv2.warpAffine(img, mm, (w, h))
    #cv2.imshow('rotated1', rotated1)
    #cv2.imshow('rotated2', rotated2)

    filename1 = file + '11.jpg' 
    filename2 = file + '12.jpg'
    filename3 = file + '13.jpg'
    filename4 = file + '14.jpg'
    filename5 = file + '15.jpg'
    filename6 = file + '16.jpg'
    filename7 = file + '17.jpg'
    filename8 = file + '18.jpg'
    # Using cv2.imwrite() method
    # Saving the image
    os.chdir("C:/Users/tadas.orentas/Desktop/boat_Imiges/saved")
    cv2.imwrite(filename1, img)
    cv2.imwrite(filename2, image_RGB)
    cv2.imwrite(filename3, image_GRAY)
    cv2.imwrite(filename4, image_flip1)
    cv2.imwrite(filename5, image_flip2)
    cv2.imwrite(filename6, image_flip3)
    cv2.imwrite(filename7, rotated1)
    cv2.imwrite(filename8, rotated2)
  
    os.chdir("C:/Users/tadas.orentas/Desktop/boat_Imiges/test1")

    #cv2.waitKey(0) & 0xFF == ord('q')

