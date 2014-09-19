'''
Created on Sep 11, 2014

@author: cristopher
@contact: cristopherpk@gmail.com
'''

import cv2 as cv

class Video(object):
    
    def capture(self, videoName):
        '''
        Open the video and creates the opencv object VideoCapture
        '''
        videoCapture = cv.VideoCapture(videoName)
        return videoCapture
    
    def getFps(self, videoCapture):
        '''
        Get the video frame rate.
        '''
        fps = videoCapture.get(cv.cv.CV_CAP_PROP_FPS)
        return fps
    
    def getSize(self, videoCapture):
        '''
        Get the video size as a two dimension array.
        '''
        size = (int(videoCapture.get(cv.cv.CV_CAP_PROP_FRAME_WIDTH)),
                int(videoCapture.get(cv.cv.CV_CAP_PROP_FRAME_HEIGHT)))
        return size
    
    def write(self, videoName, videoCapture, fps, size):
        '''
        Write the video file.
        @param videoName: Video name for output file. Must to contain the file extension.
        @param fps: Video frame rate.
        @param size: Video size, two dimensions array width x height. 
        '''

        videoWriter = cv.VideoWriter(videoName, cv.cv.CV_FOURCC('I','4','2','0'), fps, size)
        '''
        cv2.cv.CV_FOURCC('I','4','2','0') : This is an uncompressed YUV, 4:2:0
                                            chroma subsampled. This encoding is widely compatible but produces large
                                            files. The file extension should be avi .
        '''
        success, frame = videoCapture.read()
        while success: # Loop until there are no more frames.
            videoWriter.write(frame)
            success, frame = videoCapture.read()
            
    def showVideo(self, videoCapture, videoName):
        cv.namedWindow(videoName)
        print 'Showing camera feed. Click window or press any key to stop.'
        success, frame = videoCapture.read()
        while success and cv.waitKey(1) == -1:
            cv.imshow(videoName, frame)
            success, frame = videoCapture.read()
        
        cv.destroyWindow(videoName)
            
########################################################################

if __name__ == '__main__':
                
    video = Video()
    videofile = video.capture("videos/Megamind.avi")
    fps = video.getFps(videofile)
    size = video.getSize(videofile)
    
    print fps, size
    
    video.showVideo(videofile,"Megamind")
    #video.write("videos/test.avi", videofile, 20, size) 