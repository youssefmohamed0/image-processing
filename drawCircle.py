import cv2
import matplotlib.pyplot
import numpy
import math

image_path="images/japan.jpg"

image=cv2.imread(image_path)

point1=None
point2=None

def draw_circle(event,x,y,flag,param):
    global point1,point2
    if event == cv2.EVENT_LBUTTONDOWN :
        if point1 is None:
            point1 = (x,y)
            print(point1)
        elif point2 is None:
            point2 = (x,y)
            print(point2)
    if point1 is not None and point2 is not None :
        c = ( int( ( point2[0] + point1[0] ) / 2 ) ,int( ( point2[1] + point1[1] ) / 2 ))
        cv2.circle( image ,c ,int( c[0] - min( point2[0] ,point1[0] ) ) ,(0,255,0) ,2 )


cv2.namedWindow('image')
cv2.setMouseCallback("image",draw_circle)


while True:
    cv2.imshow("image",image)

    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()