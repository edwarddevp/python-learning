import cv2

img = cv2.imread('./smallgray.png', 0)
print(img)


cv2.imwrite('./newsmallgray.png', img)
