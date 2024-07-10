import cv2
alg="haarcascade_frontalface_default.xml"   #assigning the xml file
h_cascade=cv2.CascadeClassifier(alg)
m_cam=cv2.VideoCapture(0)  #capturing the main camera

while True:
    _,frame=m_cam.read() #reading the frame
    gryscl=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #grayscale conversion
    face=h_cascade.detectMultiScale(gryscl, 1.3, 4)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)  #drawing the rectangle
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break
frame.release()
cv2.destroyAllWindows()

