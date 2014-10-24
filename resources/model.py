'''
Created on Sep 24, 2014

@author: cristopher
'''

import cv2
import filters
from managers import WindowManager, CaptureManager
from trackers import HorseTracker

class Model(object):
    '''
    classdocs
    '''
    def __init__(self):
        self._windowManager = WindowManager('Cameo',self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture("videos/Megamind.avi"), 
                                              self._windowManager, False)
        self._faceTracker = HorseTracker()
        
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            if frame is not None:
                
                filters.pointMarkers(frame, frame)
                print frame
                                                              
                #TODO: Convert colored image to gray. 
                #TODO: Implement threshold (250,255)
                #TODO: Mediana filter
                #TODO: Labeling points
                #TODO: Draw the line between those points.
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    
    def onKeypress(self, keycode):
        """Handle a keypress.
        
        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        x      -> Start/stop drawing debug rectangles around faces.
        escape -> Quit.
        
        """
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(
                    'screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 120: # x
            self._shouldDrawDebugRects = \
                not self._shouldDrawDebugRects
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__ == '__main__':
    Model().run()
    
        