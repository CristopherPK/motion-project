import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
from datetime import time

BASE_PATH = '/home/cristopher/Dropbox/Research/PIBITI-2014-1015/'

tree = ET.parse(BASE_PATH + 'galloping_horse.kva')

root = tree.getroot()

children = root.find('Tracks')
i = 0

t = time

for c in children.iter('Track'):
    for track in c.iter('TrackPositionList'):
        print "==============track============="
        i+=1
        for tr in track:
            x = tr.attrib.get('UserX')
            y = tr.attrib.get('UserY')
            t = tr.attrib.get('UserTime')
            print x,y,t

print i
