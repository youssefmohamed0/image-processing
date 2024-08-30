import cv2
import numpy as np

img_path="images/test.jpg"

def get_range(color):
    c=np.uint8([[color]])

    hsvc = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lowerlimt = max(0,hsvc[0][0][0]-10), max(0,hsvc[0][0][1] -10), max(0,hsvc[0][0][2] - 10)        # if value is negative set it to 0
    upperlimt = min(255,hsvc[0][0][0]+10), min(255,hsvc[0][0][1] +10), min(255,hsvc[0][0][2] + 10)  # if value is over 255 set it to 255

    lowerlimt = np.array(lowerlimt, dtype=np.uint8)
    upperlimt = np.array(upperlimt, dtype=np.uint8)

    return lowerlimt, upperlimt

color_img=cv2.imread(img_path)

point=None
color=None
masked_image=None

def extract(event,x,y,flag,param):
    global point
    global color
    global masked_image
    if event == cv2.EVENT_LBUTTONDOWN:
        
        point = (y,x)
        color = color_img[point]

        hsv=cv2.cvtColor(color_img,cv2.COLOR_BGR2HSV)
        
        lower_color, upper_color = get_range(color)   # get color ranges in hsv (hue)

        mask = cv2.inRange(hsv, lower_color, upper_color) # create a mask using the obtained hsv ranges and the hsv converted image

        masked_image = cv2.bitwise_and(color_img,color_img,mask=mask)

        cv2.imshow("masked image",masked_image)



cv2.namedWindow('image')
cv2.setMouseCallback("image",extract)


while True:
    cv2.imshow("image",color_img)

    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()