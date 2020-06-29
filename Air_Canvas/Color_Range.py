import cv2
import numpy as np

image_hsv = None   # global
pixel = (0,0,0) # default

# mouse callback function
def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]

        #adjust the ranges(+-10, etc):
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[1] + 40])
        lower =  np.array([pixel[0] - 10, pixel[0] - 10, pixel[0] - 10])
        for i in range(0,3):
            if upper[i] > 255:
                upper[i] = 255
        print(lower, upper)
        
def main():
    global image_hsv, pixel
    
    camera = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = camera.read()
        # cv2.imwrite("NewPicture.jpg",frame)
        result = False
    camera.release()
    cv2.destroyAllWindows()

    image_src = frame
    if image_src is None:
        print ("The image read is None.")
        return
    cv2.imshow("BGR",image_src)

    cv2.namedWindow('hsv')
    cv2.setMouseCallback('hsv', pick_color)

    # Click into the hsv img , and look at values:
    image_hsv = cv2.cvtColor(image_src,cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",image_hsv)

    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

    
if __name__=='__main__':
    main()