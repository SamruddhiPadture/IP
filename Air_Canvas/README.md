# Air_Canvas

Paint in the air with an object.

Step 1:
Choose the object you want to use as a brush. (I have chosen the cap of a sketchpen.)

Run Color_Range.py to get the lower and upper bound (range) of the color to be detected.
> python Color_Range.py

Check Color_Range.mp4 for demo

The program will capture an image using the webcam. Click on the pixel of which you want the values.


Step 2:
Run Air_Canvas.py
> python Air_Canvas.py

Check Air_Canvas_Demo.mp4 for demo

Use the upper and lower bounds which you have found out using the Color_Range.py.
Move around the object to draw. I have covered the other side of the cap with a paper, so that if i turn the cap around, it won't be detected.


> Screenshot:

![Screenshot](https://github.com/SamruddhiPadture/Air_Canvas/blob/master/SS.JPG)

References: https://towardsdatascience.com/tutorial-webcam-paint-opencv-dbe356ab5d6c

