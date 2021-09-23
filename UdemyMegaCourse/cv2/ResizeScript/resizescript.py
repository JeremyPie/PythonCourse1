import cv2
import os

for file in os.listdir():
    if file.endswith('.jpg'): 
        cv2.imwrite('resized_' + file, cv2.resize(cv2.imread(file, 1), (100,100)))
