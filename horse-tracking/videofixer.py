'''
Created on Apr 27, 2015

@author: cristopher
'''

from core.managers import CaptureManager
from core.managers import WindowManager

import numpy as np
import cv2
from horse_tracking.stabilization import Stabilizer

class VideoFixer(object):
    
    def __init__(self, video):
        self._windowManager = WindowManager('VideoFixer', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(video), self._windowManager, False)
        self._stabilizer = Stabilizer(self._captureManager)
        
    def run(self):
        self._stabilizer.getPrevTransform()
               
    def show(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            print frame
            #if frame is not None:
                #self._stabilizer.getPrevTransform(frame)
                                            
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
    videoFixer = VideoFixer("videos/video.mkv")
    videoFixer.run()
        