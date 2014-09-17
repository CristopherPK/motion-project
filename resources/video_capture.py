'''
Created on Sep 11, 2014

@author: cristopher
@contact: cristopherpk@gmail.com
'''

import cv2 as cv

class Video(object):
    
    def capture(self, video):
        videoCapture = cv.VideoCapture(video)
        return videoCapture
    
    def getFps(self, videoCapture):
        fps = videoCapture.get(cv.cv.CV_CAP_PROP_FPS)
        return fps
    
    def getSize(self, videoCapture):
        size = (int(videoCapture.get(cv.cv.CV_CAP_PROP_FRAME_WIDTH)),
                int(videoCapture.get(cv.cv.CV_CAP_PROP_FRAME_HEIGHT)))
        return size
    
    def write(self, video, fps, size):
        videoWriter = cv.VideoWriter(video, cv.cv.CV_FOURCC('I','4','2','0'), fps, size)
        return videoWriter

if __name__ == '__main__':
                
    Video().play("Megamind","/videos/Megamind.avi")