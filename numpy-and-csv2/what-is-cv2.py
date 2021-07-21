import cv2

img = cv2.imread('./smallgray.png')
print(img)


cv2.imwrite('./newsmallgray.png', img)
