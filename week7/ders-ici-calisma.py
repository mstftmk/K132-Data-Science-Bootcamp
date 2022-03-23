from math import ceil
import cv2

caption = cv2.VideoCapture(0) # 0 -> first webcam

char = "".join(list(reversed('Ñ@#W$9876543210?!abc;:+=-,._  ')))

while(True):
    ret, img = caption.read() # ret -> return: True or False
    
    # img resize and show.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(gray, dsize=(80,80), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("video", resize)  
    
    # Here, we transform img to ascii chars.
    for i in resize:
        for j in i:
            print(char[min(ceil(j/128*len(char)), len(char)-1)], end='')
        print()
    
    # Here, we can close program with "q".
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

caption.release()
cv2.destroyAllWindows()