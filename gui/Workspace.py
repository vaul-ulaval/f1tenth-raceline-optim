import glob
import yaml
from objects import Raceline, Map, Centerline
import random
import csv

class Workspace():
    _centerlines = []
    _maps = []
    _racelines = []

    PATH : str

    def __init__(self, workspaccePath):
        self.PATH = workspaccePath
        self.loadRacelines()
        self.loadMaps()
        # self.loadCenterlines()
        


    def loadRacelines(self):
        self._racelines = []
        racelines = glob.glob(self.PATH + "/racelines/*")
        for raceline in racelines:
            name = raceline.split("/")[-1]
            if raceline.endswith('.raceline'): 
                with open(raceline) as f:
                    xs = []
                    ys = [] 
                    for line in f.readlines():
                        x, y, _, _ = line.split(",")
                        xs.append(float(x))
                        ys.append(float(y))   
                    self._racelines.append(Raceline(name, self.generateColor(), xs, ys))
    
    def loadMaps(self):
        self._maps = []
        maps = glob.glob(self.PATH + "/maps/*")
        for map in maps:
            name = map.split("/")[-1]
            if map.endswith('.yaml'): 
                with open(map) as yaml_stream:
                    map_metadata = yaml.safe_load(yaml_stream)
                    resolution = map_metadata['resolution']
                    origin = map_metadata['origin']
                    image_name = map_metadata['image']
                    image_path = self.PATH + "/maps/" + image_name

                    self._maps.append(Map(name, image_path, resolution, origin))
    
    def saveCenterline(self, name, data):
        header = ['x_m', 'y_m', 'w_tr_right_m', 'w_tr_left_m']
        file_path = self.PATH + "/centerlines/" + name + ".csv"
        with open(file_path, 'w', newline="") as file:
            csv_writer = csv.writer(file)

            csv_writer.writerow(header)
            for row in data:
                round_row = [round(elem, 3) for elem in row]
                csv_writer.writerow(round_row)

                    
    
    def generateColor(self):
        return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    def getCenterlines(self):
        return self._centerlines
    
    def getMaps(self):
        return self._maps
    
    def getMap(self, map_name : str) -> Map:
        for map in self._maps:
            if map.name == map_name:
                return map

    
    def getRacelines(self):
        return self._racelines