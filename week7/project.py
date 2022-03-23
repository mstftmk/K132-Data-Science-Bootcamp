from math import ceil
import cv2
import numpy as np
from scipy.misc import face


def ascii(): #turns photos into ASCII.
    cap = cv2.VideoCapture(0) # 0 -> first webcam
    
    chars = "".join(list(reversed('Ñ@#W$9876543210?!abc;:+=-,._  ')))

    while(True):
        ret, img = cap.read() # ret -> return: True or False
    
        # img resize
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(gray, dsize=(80,80), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("video", resize)  
        
        for i in resize:
            for j in i:
                print(chars[min(ceil(j/128*len(chars)), len(chars)-1)], end='')
            print()
    
        if cv2.waitKey(30) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    

def face_detect(): #Face and eye detection.

    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
    eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        print(ret)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('img', img)

        if cv2.waitKey(30) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def background_reduction(): # you can detect motions with this function.
    cap = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while(1):
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)
    
        cv2.imshow('fgmask',frame)
        cv2.imshow('frame',fgmask)

    
        if cv2.waitKey(30) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def edge_detect(first_threshold=100, second_treshold=100): #You can set thresholds for edges.
    cap = cv2.VideoCapture(0)

    while(1):
        _, frame = cap.read()

        cv2.imshow('Original',frame)
        edges = cv2.Canny(frame, first_threshold, second_treshold)
        cv2.imshow('Edges',edges)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()

def blur(): #blurring.
    cap = cv2.VideoCapture(0)

    while(1):
        _, frame = cap.read() 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        lower_red = np.array([100,150,0],np.uint8)  # it is hard to find these values
        upper_red = np.array([140,255,255],np.uint8)
    
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask= mask)
        kernel = np.ones((15,15),np.float32)/225
        smoothed = cv2.filter2D(res,-1,kernel) # simple averaging
        blur = cv2.GaussianBlur(res, (15,15), 0)
        median = cv2.medianBlur(res, 15)
        bilateral = cv2.bilateralFilter(res, 15, 75, 75)

        cv2.imshow('frame',frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        cv2.imshow('smoothed', smoothed)
        cv2.imshow('blur', blur)
        cv2.imshow('median', median)
        cv2.imshow('bilateral', bilateral)


        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()
    
def photo_thresholding(image='images/bookpage.jpg', min_treshold=10, max_treshold=255): #you can set photo destination. And you can set min and max thresholds.
    img = cv2.imread(image) # read image

    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(grayscaled, min_treshold, max_treshold, cv2.THRESH_BINARY)
    th = cv2.adaptiveThreshold(grayscaled, max_treshold, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) 

    cv2.imshow('original', img) #original photo.
    cv2.imshow('threshold', threshold) #after threshold.
    cv2.imshow('gaussian', th) #after adapted gaussian.

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def color_filter(upper_RGB=[100,150,0], lower_RGB=[140,255,255]): #default= blue. You can change that.
    cap = cv2.VideoCapture(0)
    
    #lower_red = np.array([30,150,50])   You can use that args to filter red color.
    #upper_red = np.array([255,255,180])

    while(1):
        _, frame = cap.read() 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        lower = np.array(lower_RGB,np.uint8)  # it is hard to find these values
        upper = np.array(upper_RGB,np.uint8)
    
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(frame, frame, mask= mask)

        cv2.imshow('frame',frame) # original capture
        cv2.imshow('mask',mask) # shows chosen area with gray scale.
        cv2.imshow('res',res) # shows result.
    
        if cv2.waitKey(5) & 0xFF == ord('q'): #You can quit with "q".
            break

    cv2.destroyAllWindows()
    cap.release()  
    
#color_filter()
#ascii()
#face_detect()
#photo_thresholding()
#blur()
#edge_detect()
#background_reduction()
