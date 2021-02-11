import numpy as np
import cv2

img = cv2.imread("/home/arefmalek/Desktop/model/IMG/center_2021_01_15_12_53_06_325.jpg")
brightness_arr = img.sum(2)
new_img = img.copy()
new_img[brightness_arr < 400] = 0

new_img[100:, 40:280, :] = 0

gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

# gray = cv2.GaussianBlur(gray,(5,5),0)

edges = cv2.Canny(gray,100,200)

cv2.imwrite("idk.png", edges)