import cv2 # this  is for using images and for accessing web cam
import pydub # this is for accessing sounds and to get the alarm
import winsound #it is also same as the pydub
cam = cv2.VideoCapture(0) #we started capturing video... '0 ' is for saying that we are using our in built web cam
while cam.isOpened():  #when the camera opens,
    ret, frame1 = cam.read()  #we are saying the computer to take 1 frame
    ret, frame2 = cam.read() # in this we taking another frame... it contious till the camera turn offs
    diff = cv2.absdiff(frame1, frame2) # finding the difference between the 2 frames..
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) #converting the taken video/frames into gray colourscape for computer
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # to avoid the blurrs in the video
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # to reduce the unnecessary noise in the video
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #taking the outline of the images in video
   # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:  # checking whether the thing is unnecessary like insects and bugs or the humans or other things
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) # drawing the outline to the objects
        #pydub.PlaySound('alert wav', pydub.SND_ASYNC)
        winsound.Beep(500, 200)# playing the sound
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('my cam', frame1)# showing the video to the user
    cv2.imshow('Granny Cam',diff)

