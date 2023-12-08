import glob
import yaml
from inputs_helper.centerline import ImageCenterline, convert_centerline_to_real, read_map_yaml, write_centerline_csv
from .objects import Raceline, Map, Centerline
import random
import pandas as pd

class Workspace():
    _centerlines = []
    _maps = []
    _racelines = []

    PATH : str

    def __init__(self, workspace_path : str):
        self.PATH = workspace_path
        self.load_racelines()
        self.load_maps()
        self.load_centerlines()
        


    def load_racelines(self):
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
                    self._racelines.append(Raceline(name, "race_f1tenth_icra_2023_short.yaml", self.generate_color(), xs, ys))
    
    def load_maps(self):
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

    def load_centerlines(self):
        self._centerlines = []
        centerlines = glob.glob(self.PATH + "/centerlines/*")
            
        for centerline in centerlines:
            name = centerline.split("/")[-1]
            raw_data = pd.read_csv(centerline)
            xs = raw_data["x_m"].values
            ys = raw_data["y_m"].values
            width_right = raw_data["w_tr_right_m"].values
            width_left = raw_data["w_tr_left_m"].values

            self._centerlines.append(Centerline(name, xs, ys, width_right, width_left))            
    
    def save_centerline(self, name: str, img_centerline: ImageCenterline):
        csv_path = self.PATH + "/centerlines/" + name + ".csv"
        yaml_path = self.PATH + "/maps/" + name + ".yaml"
        
        map_yaml = read_map_yaml(yaml_path)
        real_centerline = convert_centerline_to_real(img_centerline, map_yaml)
        write_centerline_csv(csv_path, real_centerline)
    
    def generate_color(self):
        return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    def get_centerlines(self):
        return self._centerlines
    
    def get_maps(self):
        return self._maps
    
    def get_map(self, map_name : str) -> Map:
        for map in self._maps:
            if map.name == map_name:
                return map

    def get_centerline(self, centerline_name : str) -> Centerline:
        for centerline in self._centerlines:
            if centerline.name == centerline_name:
                return centerline
    
    def get_racelines(self):
        return self._racelines