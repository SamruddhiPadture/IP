import imageio

def dodge(front,back):
  result = front*255/(255-back) 
  result[result>255] = 255
  result[back==255] = 255
  return result.astype('uint8')

import numpy as np
def grayscale(rgb):
  return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = imageio.imread("1.jpg")
g = grayscale(img)

i = 255-g
import scipy.ndimage
b = scipy.ndimage.filters.gaussian_filter(i,sigma=20)
final_img = dodge(b,g)

import matplotlib.pyplot as plt
plt.imshow(r, cmap="gray")

plt.imsave('converted.png', final_img, cmap='gray', vmin=0, vmax=255)

