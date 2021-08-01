import cv2
import pandas
from datetime import datetime

first_frame = None

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

status_list = [None, None]
times = []

df = pandas.DataFrame(columns=["Start", "End"])

while True:

    status = 0
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # remove noise and improve the accuracy of the difference
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)

    thres_frame = cv2.threshold(delta_frame, 30, 255, 0, cv2.THRESH_BINARY)[1]

    thres_frame = cv2.dilate(
        thres_frame, None, iterations=2)  # smooth threshold

    (cnts, _) = cv2.findContours(thres_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (w+w, h+y), (0, 255, 0), 3)

    status_list.append(status)

    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Color Frame", frame)
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thres_frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break


for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)


print(type(df["Start"][0]))
df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
