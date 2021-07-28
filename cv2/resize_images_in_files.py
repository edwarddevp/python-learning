import cv2
import glob

images = glob.glob('*jpg')

for image in images:
    img = cv2.imread(image)
    resized_image = cv2.resize(img, (100, 100))
    cv2.imshow("hey", resized_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("image"+image, resized_image)
