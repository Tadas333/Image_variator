import imutils

import cv2
import numpy as np
from PIL import Image
import glob, os
from decimal import Decimal
import fileinput
import shutil

path = 'pic1.jpeg'

os.chdir("C:/Users/tadas.orentas/Desktop/PROJECTS/Maritime/Image_variator/test1")
c = "C:/Users/tadas.orentas/Desktop/PROJECTS/Maritime/Image_variator/test1"
p = "C:/Users/tadas.orentas/Desktop/PROJECTS/Maritime/Image_variator/test1"

for name in glob.glob("*.txt"):   
    newname = str(name.replace(".xml", ""))
    os.rename(name, newname)




for file in glob.glob("*.JPG"):
    
    img = cv2.imread(file)
    print(file)
    #cv2.imshow('control', img)
    a =str(file)
    txtfile = a.replace(".jpg", ".txt")
    shutil.copyfile(c + "/" + txtfile, p + "/f1" + txtfile)
    print(txtfile)
    f1txtfile = "f1" + txtfile
    data = []
    with open(f1txtfile,"r") as f:
        data = f.readlines() # readlines() returns a list of items, each item is a line in your file

   
    for i in range(len(data)):
        #print(data[i]) # print line 5
        count = 0
        cord = ""

        for space in data[i]:
            if space ==' ':
                count = count + 1
                if count == 2:
                    break
                cord = ""
            else:
                cord = cord + space
        #print(cord)    
        ncord = 1 - (float(cord))
        y = Decimal(ncord)
        newcord = str(y.quantize(Decimal('0.000001')))
        


        with fileinput.FileInput(f1txtfile, inplace=True, backup='') as file1:
            for line in file1:
                print(line.replace(cord, newcord), end='')


    image_flip1 = cv2.flip(img, 1)
    image_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB )
    image_GRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
    image_invert = cv2.bitwise_not(img)
    image_blur= cv2.blur(img,(10,10)) 
    

    

    # # Displaying the image 
    # #cv2.imshow('RGB', image_RGB)
 


    # (h, w) = img.shape[:2]
    # (cX, cY) = (w // 2, h // 2)
    # # rotate our image by 45 degrees around the center of the image
    # M = cv2.getRotationMatrix2D((cX, cY), 5, 1.0)
    # mm = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
    # rotated1 = cv2.warpAffine(img, M, (w, h))
    # rotated2 = cv2.warpAffine(img, mm, (w, h))
    # #cv2.imshow('rotated1', rotated1)
    # #cv2.imshow('rotated2', rotated2)
    
    filename1 = 'f1' + file
    filename2 = 'RGB' + file
    filename3 = 'GRAY' + file
    filename4 = 'INVERT' + file
    filename5 = 'BLUR' + file
    # filename5 = file + '15.jpg'
    # filename6 = file + '16.jpg'
    # filename7 = file + '17.jpg'
    # filename8 = file + '18.jpg'
    # # Using cv2.imwrite() method
    # # Saving the image
    # os.chdir("C:/Users/tadas.orentas/Desktop/boat_Imiges/saved")
    cv2.imwrite(filename1, image_flip1)

    cv2.imwrite(filename2, image_RGB)
    shutil.copyfile(c + "/" + txtfile, p + "/RGB" + txtfile)

    cv2.imwrite(filename3, image_GRAY)
    shutil.copyfile(c + "/" + txtfile, p + "/GRAY" + txtfile)

    cv2.imwrite(filename4, image_invert)
    shutil.copyfile(c + "/" + txtfile, p + "/INVERT" + txtfile)

    cv2.imwrite(filename5, image_blur)
    shutil.copyfile(c + "/" + txtfile, p + "/BLUR" + txtfile)
    # cv2.imwrite(filename5, image_flip2)
    # cv2.imwrite(filename6, image_flip3)
    # cv2.imwrite(filename7, rotated1)
    # cv2.imwrite(filename8, rotated2)
  
    # os.chdir("C:/Users/tadas.orentas/Desktop/boat_Imiges/test1")

    cv2.waitKey(0) & 0xFF == ord('q')

