import cv2 
import pytesseract
import numpy as np
import threading
from pytesseract import Output
from gtts import gTTS
import subprocess

camera = cv2.VideoCapture(0)
ret, img = camera.read()

path = "images/"
count =  1

img_src = cv2.imread("images/1.jpg")

def get_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_detect(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

while True:
    name = path + str(count)+".jpg"
    ret, img = camera.read()
    cv2.imshow("img", img)

    if cv2.waitKey(10) & 0xFF == ord('c'):
        cv2.imwrite(name, img)
        print("Image Captured!")
        #Add thresholding,canny, or opening filters as necessary
        gray = get_gray(img_src) 
        bd = blur_detect(gray)
        print(bd)
        cv2.imshow("img",gray)
        t = pytesseract.image_to_string(img_src)
        if bd < 100 or t and t.strip() == ""  :
            subprocess.call(['espeak','Not Detected'])
        if t and t.strip() != "":
            print("Source Image: ",t)
            subprocess.call(['espeak',t])            
        if cv2.waitKey(0) & 0xFF == ord('q'):
	        break