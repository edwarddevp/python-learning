import cv2
import glob

types = ('*.jpg', '*.png')  # the tuple of file types
images = []
for files in types:
    images.extend(glob.glob(files))

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for imagepath in images:
    image = cv2.imread(imagepath)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image,
                                          scaleFactor=1.5,
                                          minNeighbors=5)

    for x, y, w, h in faces:
        image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

    resized_image = cv2.resize(image, (600, 600))
    cv2.imshow("Face Rectangule", resized_image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
