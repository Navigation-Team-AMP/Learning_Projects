import numpy as np
import cv2

img = cv2.imread("openCV/center.jpg")
brightness_arr = img.sum(2)
new_img = img.copy()
new_img[brightness_arr < 200] = 0

gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

# gray = cv2.GaussianBlur(gray,(5,5),0)

edges = cv2.Canny(new_img,100,200)

print(edges)

cv2.imwrite("openCV/idk.png", edges)