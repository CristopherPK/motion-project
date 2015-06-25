'''
Created on May 12, 2015

@author: cristopher
@contact: cgsf@ic.ufal.br
'''

import cv2
import numpy as np

'''
Alogorithm adaptation from example found on the internet.
'''
lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict( maxCorners = 200,
                       qualityLevel = 0.01,
                       minDistance = 7)

class Stabilizer:
    def __init__(self):
        self.cap = cv2.VideoCapture("videos/video.mkv")
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.frame_idx = 0
        
    def getPrevTransform(self):
        ret, prev = self.cap.read()
        prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        
        p0 = cv2.goodFeaturesToTrack(prev_gray, mask = None, **feature_params)
               
        while(True):
            ret, cur = self.cap.read()
            #print cur
            if cur is None:
                break
            
            cur_gray = cv2.cvtColor(cur,cv2.COLOR_BGR2GRAY)          
            
            #print prev_corner          
            
            img0, img1 = prev_gray, cur_gray
            
            # calculate optical flow
            p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
                      
            # Select good points
            good_new = p1[st==1]
            good_old = p0[st==1]

            T = cv2.estimateRigidTransform(good_new, good_old, False)
                        
            print "---"
            
#             for i in st.size():
#                 if st[i] is not None:
#                     prev_corner2.push_back(prev_corner[i]);
#                     cur_corner2.push_back(cur_corner[i]);
#             
#             ''' translation + rotation only '''
#                     
#             T = cv2.estimateRigidTransform(prev_corner2, cur_corner2, False)
# 
#             if T.data() is None:
#                 last_T.copyTo(T)
#                 
#             T.copyTo(last_T)
#             
#             dx = T.at(0,2)
#             dy = T.at(1,2)
#             da = atan2(T.at(1,0), T.at(0,0))
#             
#             prev_to_cur_transform.pushback(TransformParam(dx,dy,da))
#             
#             cur.copyTo(prev)
#             
#             prev_gray = cur_grey.copy()
#             
#             k = k + 1

if __name__ == '__main__':
    Stabilizer().getPrevTransform()