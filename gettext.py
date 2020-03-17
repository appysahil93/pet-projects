# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:18:36 2020

@author: 691928
"""

#python program to get text extracted from a Image

#to get text from a image we use OCR (Optical Chanracter Recognition) technique
#to get text using OCR in python there is a library called "Tesseract". 
#Tesseract is an OCR engine for various OS, and used to get text from various source such as image, video, gifs.
#install tesseract .exe application in system to use tesseract OCR

#import modules

from PIL import Image #PIL => Pyhton Image Library
import pytesseract

#include tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  #add the path where tesseract is installed

#create an image object of Image class of PIL library with image path
img = Image.open(r"‪C:\Users\691928\Desktop\image1.jpg")

#pass image/image  object into pytesseract module also provide language, as pytesseract is trained in many language
text = pytesseract.image_to_string(img, lang = "eng")
 
#print the extracted text
print(text)


