import cv2, time

first_frame=None
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    check, frame = video.read()


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 3)

    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(30)
    if key==ord('q'):
        break
    

video.release()
cv2.destroyAllWindows()

