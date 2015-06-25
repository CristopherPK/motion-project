'''
Created on May 11, 2015

@author: cristopher
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('horse.png',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),3,1)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.imshow(dst)
plt.show()