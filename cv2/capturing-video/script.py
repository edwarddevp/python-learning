# import cv2
# import time

# video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# while True:
#     check, frame = video.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow("Capture", frame)
#     # cv2.imshow("Capture 2", gray)
#     key = cv2.waitKey(1)

#     if key == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()

#  detect faces in video
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image,
                                          scaleFactor=1.2,
                                          minNeighbors=5)

    for x, y, w, h in faces:
        # frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        # frame = cv2.circle(frame, (x + (int(w/2)), y +
        #                            (int(h/2))), int(w/2), (0, 255, 0), 3)
        frame = cv2.ellipse(frame, (x + (int(w/2)), int((y + h) / 2) - 50),
                            (120, 30), 0, 0, 360, (0, 255, 0), 3)

    cv2.imshow("Capture", frame)
    # cv2.imshow("Capture 2", gray)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
