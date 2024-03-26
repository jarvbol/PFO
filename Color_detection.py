import cv2
import numpy as np


cv2.namedWindow( "result" ) 
cap = cv2.VideoCapture(2)
crange = [0,0,0, 0,0,0]
color = "";

color_red=(0,0,255)
color_blue=(255,0,0)
try:
    while True:
        flag, img = cap.read()
        height,widht=img.shape[:2]
        Centr_X=int(widht/2)
        Centr_Y=int(height/2)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        
        # Формирование начального и конечного цвета фильтра.
        lower_green = np.array((64, 135, 120), np.uint8)
        upper_green = np.array((97, 255, 255), np.uint8)

        lower_blue = np.array((89, 86, 93), np.uint8)
        upper_blue = np.array((145, 255, 255), np.uint8)

        lower_yellow = np.array((14, 10, 175), np.uint8)
        upper_yellow = np.array((45, 255, 255), np.uint8)

        lower_red = np.array((0, 50, 20), np.uint8)
        upper_red = np.array((20, 253, 255), np.uint8)


        # Наложение фильтра на кадр в модели HSV.
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        moments_green=cv2.moments(mask_green,1)
        moments_blue=cv2.moments(mask_blue,1)
        moments_yellow=cv2.moments(mask_yellow,1)
        moments_red=cv2.moments(mask_red,1)

        dArea_green = moments_green['m00']
        dArea_blue = moments_blue['m00']
        dArea_yellow = moments_yellow['m00']
        dArea_red = moments_red['m00']

        dM01_green = moments_green['m01']
        dM10_green = moments_green['m10']
        dArea_GREEN = moments_green['m00']

        # Определение цвета.
        if dArea_green > 20000: color = "Green"
        elif dArea_blue > 20000: color = "Blue"
        elif dArea_yellow > 20000: color = "Yellow"
        elif dArea_red > 20000: color = "Red"
        else: color = "Unknown"

        cv2.putText(img, "Detected color: " + color, (10,30),cv2.FONT_HERSHEY_SIMPLEX,1,color_blue,2)
        # Определение расстояния от центра области зрения до центра фигуры.
        if dArea_GREEN>100:
            x=int(dM10_green / dArea_GREEN)
            y=int(dM01_green / dArea_GREEN)
            
            cv2.circle(img,(x,y),5,color_blue,2)
            cv2.putText(img,"x%d;y%d" % (x,y),(x+10,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,color_blue,2)
            
            cv2.circle(img,(Centr_X,Centr_Y),5,color_red,2)
            cv2.putText(img,"x%d;y%d" % (Centr_X-x,Centr_Y-y),(Centr_X+10,Centr_Y-10),cv2.FONT_HERSHEY_SIMPLEX,1,color_red,2)
            
            cv2.line(img,(x,y),(Centr_X,Centr_Y),color_blue,2)
    
        cv2.imshow('Origin',img)
        cv2.imshow('Result green', mask_green)
        cv2.imshow('Result blue', mask_blue)
        cv2.imshow('Result yellow', mask_yellow)
        cv2.imshow('Result red', mask_red)
        
        ch = cv2.waitKey(5)
        if ch == 27:
            break
    

except KeyboardInterrupt:
    print(' Exit pressed Ctrl+C')
    cv2.destroyAllWindows() 
