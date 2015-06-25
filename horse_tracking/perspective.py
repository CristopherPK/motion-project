'''
Created on May 11, 2015

@author: cristopher
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/horse.png')
rows,cols,ch = img.shape

pts1 = np.float32([[0,525],[1920,650],[0,582],[1920,710]])
pts2 = np.float32([[0,0],[1920,0],[0,100],[1920,100]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(1920,1080))

#plt.subplot(121),plt.imshow(img),plt.title('Input')
#plt.subplot(122),plt.imshow(dst),plt.title('Output')

plt.imshow(dst)
plt.show()