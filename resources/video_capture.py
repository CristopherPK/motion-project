'''
Created on Sep 11, 2014

@author: cristopher
'''

import cv2

class Video(object):
    
    def play(self,videoName,videoPath):

        cap = cv2.VideoCapture()
        cap.open(videoPath)    
        print cap.isOpened()        
        cv2.namedWindow(videoName, cv2.WINDOW_AUTOSIZE)
        #frames = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        #print frames                        
                              
        while cap.isOpened() is True:
            frame = cap.read()
            #print frame
            if frame[0] is False:
                break
            
            cv2.imshow(videoName, frame[1])
            
        cv2.waitKey(0)            

if __name__ == '__main__':
                
    Video().play("Megamind","/videos/Megamind.avi")