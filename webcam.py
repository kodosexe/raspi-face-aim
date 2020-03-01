import cv2
import sys
import RPi.GPIO as GPIO

cascPath = "/home/pi/Webcam-Face-Detect/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(0, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

fireOF = 0
fireDir = 5
lftRgtOF = 6
lftRgtDir = 13
upDwnOF = 19
upDwnDir = 26


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #Draw a rectangle in the middle
    cv2.rectangle(frame, (318,238), (322, 242), (0,0,255), 2)
    cv2.rectangle(frame, (280, 200), (360, 280), (0, 255, 255), 2)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	#print("Face Detected")
        #Calculate Center
        xCenter = x + (w/2)
        yCenter = y + (h/2)
        #Draw Rectangle in Center
        cv2.rectangle(frame, (xCenter-2, yCenter-2), (xCenter+2, yCenter+2), (0,0,255), 2)
        if xCenter > 360 and xCenter <= 680:
            cv2.putText(frame, "Right", (x-5,y-5), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))
            GPIO.output(lftRgtDir, GPIO.HIGH)
            GPIO.output(lftRgtOF, GPIO.HIGH)
	    print("Right")
        elif xCenter < 280 and xCenter > 0:
            cv2.putText(frame, "Left", (x,y-5), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))
            GPIO.output(lftRgtDir, GPIO.LOW)
            GPIO.output(lftRgtOF, GPIO.HIGH)
	    print("Left")
        else:
            GPIO.output(lftRgtOF, GPIO.LOW)
            
        if yCenter > 280 and yCenter < 480:
            cv2.putText(frame, "Down", (x,y-25), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))
            GPIO.output(upDwnDir, GPIO.HIGH)
            GPIO.output(upDwnOF, GPIO.HIGH)
	    print("Down")
        elif yCenter < 200 and yCenter > 0:
            cv2.putText(frame, "Up", (x,y-25), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))
            GPIO.output(upDwnDir, GPIO.LOW)
            GPIO.output(upDwnOF, GPIO.HIGH)
	    print("Up")
        else:
            GPIO.output(upDwnOF, GPIO.LOW)
            
        if xCenter < 360 and xCenter > 280 and yCenter < 280 and yCenter > 200:
            cv2.putText(frame, "FIRE", (x,y-25), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0))
            GPIO.output(fireDir, GPIO.HIGH)
            GPIO.output(fireOF, GPIO.HIGH)
	    print("Fire")
        else:
            GPIO.output(fireOF, GPIO.LOW)


    if len(faces) == 0:
        GPIO.output(fireOF, GPIO.LOW)
        GPIO.output(upDwnOF, GPIO.LOW)
        GPIO.output(lftRgtOF, GPIO.LOW)
        
    # Display the resulting frame
    #cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
