import cv2, numpy, os


cam1=cv2.VideoCapture("cars\cars+cycle.avi")
cam2=cv2.VideoCapture("cars\cars.mp4")
cam3=cv2.VideoCapture("cars\carsss.avi")
carvid=cv2.CascadeClassifier("cars\cars.xml")


width,height=130,100

count=1

while count>0:
    ret, frame=cam1.read()
    
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars=carvid.detectMultiScale(grey,1.1,1)
    print(cars)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)




    cv2.imshow("webcam",frame)
    k=cv2.waitKey(10)
    if k==27:
        break



while count>0:
    ret, frame=cam2.read()
    
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars=carvid.detectMultiScale(grey,1.1,2)
    print(cars)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)




    cv2.imshow("webcam",frame)
    k=cv2.waitKey(10)
    if k==27:
        break



while count>0:
    ret, frame=cam3.read()
    
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars=carvid.detectMultiScale(grey,1.1,1)
    print(cars)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)




    cv2.imshow("webcam",frame)
    k=cv2.waitKey(10)
    if k==27:
        break
