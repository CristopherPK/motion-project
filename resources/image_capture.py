'''
Created on Sep 15, 2014

@author: cristopher
@contact: cristopherpk@gmail.com
'''
import cv2 as cv
import numpy as np

class Image(object):

    def read(self, image):
        '''
        Reading an image.
        @param image: String path to image.
        '''        
        _image = cv.imread(image)
        return _image
        
    def write(self, image, output):
        '''
        Writing an image.
        @param image: Image numpy array. 
        @param output: This string takes the name of output image and her type.
        '''
        if (cv.imwrite(output, image) is True):
            return True
        else:
            return False
        
    def toByteArray(self, image):
        '''
        Converting image numpy array to byte array.
        @param image: Image numpy array.
        '''
        print image
        byteArray = bytearray(image)
        return byteArray
    
    def toImage(self, byteArray, height, width, channel=0):
        '''
        Converting byte array to image through numpy array.
        @param byteArray: Byte array image.
        @param channel: Image color channel.
        '''
        _image = np.array(byteArray).reshape(height, width, channel)
        return _image
    
    
########################################################################
        
if __name__ == '__main__':
    img = Image()
#     image = img.read("images/image_1.png")
#     print type(image)
#     print Image().write(image,"images/GrayPicture.jpg")
     
#     byteImage = img.toByteArray(image)
#     
#     image2 = img.toImage(byteImage)
#     
#     print img.write(image2, "images/teste.png") 

     
    
        
    
    
    
        
