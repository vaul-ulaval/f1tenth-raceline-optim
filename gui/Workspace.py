import glob
import os
from dataclasses import Raceline, Map, Centerline
import random

class Workspace():
    _centerlines = []
    _maps = []
    _racelines = []

    PATH = "**/racetracks/"


    def loadRacelines(self):
        for dirpath, _, files in os.walk('.'):  
            for filename in files: 
                file_path = os.path.join(dirpath, filename) 
                if filename.endswith('.raceline'): 
                    with open(file_path) as f:
                        xs = []
                        ys = [] 
                        for line in f.readlines():
                            x, y, _, _ = line.split(",")
                            xs.append(float(x))
                            ys.append(float(y))   
                        self._racelines.append(Raceline(filename, self.generateColor(), xs, ys))
    
    def loadMaps(self):
        for dirpath, _, files in os.walk('.'):  
            for filename in files: 
                file_path = os.path.join(dirpath, filename) 
                if filename.endswith('.pgm'): 
                    
    
    def generateColor(self):
        return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    def getCenterlines(self):
        return self._centerlines
    
    def getMaps(self):
        return self._maps

    
    def getRacelines(self):
        return self._racelines