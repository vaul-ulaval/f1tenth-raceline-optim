import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import yaml
import sys
import argparse

map_path = "/mnt/nas/maps/iros.pgm"
racelines_paths = [
    "/mnt/nas/maps/nl.raceline",
    "/mnt/nas/maps/jmf.raceline",
]



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
racelines_xs = []
racelines_ys = []
for raceline_path in racelines_paths:
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
	
	racelines_xs.append(xs_raceline)
	racelines_ys.append(ys_raceline)




plt.figure(figsize=(10, 10))
plt.imshow(raw_map_img, cmap="gray", origin="lower")

plt.plot(xs_centerline, ys_centerline)
for i  in range(len(racelines_xs)):
	plt.plot(racelines_xs[i], racelines_ys[i])
plt.show()