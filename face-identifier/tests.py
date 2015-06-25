'''
Created on Sep 23, 2014

@author: cristopher
'''
import cv2

class Tests(object):
    
    def testImage(self):
        from scipy.ndimage.measurements import label
        
        src = cv2.imread("core/images/horse.jpg",0)    
        #ret, threshSrc = cv2.threshold(src,250,255,cv2.THRESH_BINARY)
        #blurredSrc = cv2.medianBlur(threshSrc, 9)
        #labeledSrc, numFeatures = label(blurredSrc)
        #cv2.addWeighted(src, 0.5, labeledSrc, 0.5, 0.0, dst)
        #src = labeledSrc
        
        cv2.namedWindow("Test", cv2.CV_WINDOW_AUTOSIZE)
        
        cv2.imshow("Test", src)
        
        cv2.waitKey()       
        
if __name__ == '__main__':
    tests = Tests()
    tests.testImage()
        
        
        