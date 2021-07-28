import cv2

img = cv2.imread("img.jpg", 0)

resized_image = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
cv2.imshow("Friends", resized_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite("new_resized.jpg", resized_image)
