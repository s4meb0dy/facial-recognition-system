
import numpy as np
import cv2
import keyboard

def takePhoto():
    cap = cv2.VideoCapture(0)
    print('Press "s" for saving image')
    while(True):
        ret, frame = cap.read()
        cv2.imshow("Face", frame);
        if keyboard.is_pressed('s'):
            name = "image"
            cv2.imwrite('temp/' + str(name) + ".jpg", frame)
            print('image saved')
            break
        if cv2.waitKey(30) & 0xFF == ord('q'): # you can increase delay to 2 seconds here
            break
    cap.release()
    cv2.destroyAllWindows()
    return frame