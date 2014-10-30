'''
@author: Cristopher Freitas
@contact: cgsf@ic.ufal.br
'''
BASE_PATH = '/home/cristopher/Dropbox/Research/PIBITI-2014-1015/'

class Experiment(object):
    
    def __init__(self):
        self.tracks = []        
    '''
    This method get the Kinovea Tracks and set to a array list.
    '''
    def get_tracks(self):
        import xml.etree.ElementTree as ET
        tree = ET.parse(BASE_PATH + 'galloping_horse.kva')
        root = tree.getroot()
        children = root.find('Tracks')
        i = 0
        for c in children.iter('Track'):
            for _track in c.iter('TrackPositionList'):
                i+=1
                #print "==============track" + str(i) + "============="
                xs = []
                ys = []
                ts = []
                for tr in _track:
                    #X's coordinate
                    x = tr.attrib.get('UserX')
                    l = len(x)
                    x = x[0:l-3]
                    x = int(x)
                    #Y's coordinate
                    y = tr.attrib.get('UserY')
                    l = len(y)
                    y = y[0:l-3]
                    y = int(y)
                    #T's time in seconds.
                    t = tr.attrib.get('UserTime')
                    l = len(t)
                    t = t[l-5:l-3] + t[l-2:l]
                    t = float(t)
                    t = t * 0.01
                    #Setting a list for each coordinate.
                    xs.append(x)
                    ys.append(y)
                    ts.append(t)
                    
                track = [xs,ys,ts]
                #print len(track)
                self.tracks.append(track)
                #print len(self.tracks)
        return self.tracks
    
    def optimize_tracks(self):
        import matplotlib.pyplot as plt
        import numpy as np
                
        for track in self.tracks:
            x, y, t = np.asarray(track)
            sy = np.convolve(y, np.ones(10)/10)
            plt.xlabel('eixo x')
            plt.ylabel('eixo y')
            x = x[10:len(y)]
            sy = sy[10:len(y)]
            plt.plot(x,sy)
                    
        plt.show()
                
if __name__ == '__main__':
    experiment = Experiment()
    experiment.get_tracks()
    experiment.optimize_tracks()
    
