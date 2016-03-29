import matplotlib.pyplot as plt
import pylab
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('test.png')
lum_img = img[:,:,0]
plt.hist(lum_img.flatten(), 256, range=(0.0, 1.0), fc='k', ec='k')
pylab.show()
