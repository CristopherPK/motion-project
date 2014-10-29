import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
from datetime import time

BASE_PATH = '/home/cristopher/Dropbox/Research/PIBITI-2014-1015/'

tree = ET.parse(BASE_PATH + 'galloping_horse.kva')

root = tree.getroot()

children = root.find('Tracks')
i = 0

for c in children.iter('Track'):
    for _track in c.iter('TrackPositionList'):
        i+=1
        print "==============track" + str(i) + "============="
        track = (0,0,0)
        for tr in _track:
            x = tr.attrib.get('UserX')
            l = len(x)
            x = x[0:l-3]
            x = int(x)
            y = tr.attrib.get('UserY')
            l = len(y)
            y = y[0:l-3]
            y = int(y)
            t = tr.attrib.get('UserTime')
            l = len(t)
            t = t[l-5:l-3] + t[l-2:l]
            t = float(t)
            t = t * 0.01
            t = (x,y,t)
            print t