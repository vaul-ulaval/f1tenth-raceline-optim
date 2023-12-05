import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import yaml
import sys
import argparse

parser = argparse.ArgumentParser(
    prog='visualise-raceline',
    description='Visualise your raceline')
parser.add_argument('--map-path', required=True,
                    help='Path to the .pgm map')
parser.add_argument('--raceline-path', help='Path to the raceline generated with the gen-raceline wrapper')
args = parser.parse_args()

map_path: str = args.map_path
raceline_path: str = args.raceline_path

map_metadata_path = map_path.replace(".pgm", ".yaml")
with open(map_metadata_path, 'r') as yaml_stream:
    try:
        map_metadata = yaml.safe_load(yaml_stream)
        map_resolution = map_metadata['resolution']
        origin = map_metadata['origin']
    except yaml.YAMLError as ex:
        print(ex)
        sys.exit(-1)

def scale_point(x, y):
    orig_x = origin[0]
    orig_y = origin[1]
    x -= orig_x
    y -= orig_y

    x /= map_resolution
    y /= map_resolution
    return x, y

# Map data
raw_map_img = np.array(Image.open(
    map_path).transpose(Image.FLIP_TOP_BOTTOM))
raw_map_img = raw_map_img.astype(np.float64)

# Centerline data
track_path = map_path.replace(".pgm", ".csv")
raw_data = pd.read_csv(track_path)
xs_centerline = raw_data["# x_m"].values
ys_centerline = raw_data["y_m"].values
xs_centerline, ys_centerline = scale_point(xs_centerline, ys_centerline)


# Raceline data
raceline_data = open(raceline_path, "r")
xs_raceline = []
ys_raceline = []
raceline_data_lines = raceline_data.readlines()
for line in raceline_data_lines:
    x, y, _, _ = line.split(",")
    x = float(x)
    y = float(y)
    x, y = scale_point(x, y)
    xs_raceline.append(x)
    ys_raceline.append(y)




plt.figure(figsize=(10, 10))
plt.imshow(raw_map_img, cmap="gray", origin="lower")

plt.plot(xs_centerline, ys_centerline)
plt.plot(xs_raceline, ys_raceline)
plt.show()