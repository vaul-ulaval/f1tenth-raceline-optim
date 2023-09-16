import argparse
import os
import sys

import numpy as np
from skimage.morphology import skeletonize
import matplotlib.pyplot as plt
import yaml
import scipy
from PIL import Image
import os
import pandas as pd

parser = argparse.ArgumentParser(
    prog='gen-centerline',
    description='This is a wrapper program to help generate .csv centerlines from .pgm maps')

parser.add_argument('--map-path', required=True,
                    help='Path to the .pgm map file')
parser.add_argument('--output-file', required=False, default='',
                    help='By default, it will put the centerline csv at the same path as the image, but you can put another output path')
parser.add_argument('--thresold', required=False, type=float, default=0.5,
                    help='This is the value used to filter out after the euclidian filter. Play with it if you see "hairy" lines in the graph')
parser.add_argument(
    '--debug', action='store_true', required=False, help='With debug on, it will print graphs for every step of the generation')
parser.add_argument('--reverse', action='store_true', required=False, default=False,
                    help='Will reverse the order of the centerline points (By default its clockwise)')
args = parser.parse_args()

# Reading arguments
map_path: str = args.map_path
file_name = map_path.replace('.pgm', '')

map_yaml_path: str = f"{file_name}.yaml"
is_debug: bool = args.debug
should_reverse_centerline: bool = args.reverse
thresold: float = args.thresold
output_path: str = args.output_file

# Validating arguments
if not os.path.isfile(map_path):
    print('Error! This map file does not exists')
    sys.exit(-1)
elif not map_path.endswith('.pgm'):
    print('Error! The map must have the ".pgm" extension')
    sys.exit(-1)
elif not os.path.isfile(map_yaml_path):
    print('Error! The map file must have a .yaml with the same name')
    sys.exit(-1)

if output_path == '':
    output_path = f"{file_name}.csv"

# Reading yaml file
with open(map_yaml_path, 'r') as yaml_stream:
    try:
        map_metadata = yaml.safe_load(yaml_stream)
        map_resolution = map_metadata['resolution']
        origin = map_metadata['origin']
    except yaml.YAMLError as ex:
        print(ex)
        sys.exit(-1)

# Reading raw .pgm image
raw_map_img = np.array(Image.open(
    map_path).transpose(Image.FLIP_TOP_BOTTOM))
raw_map_img = raw_map_img.astype(np.float64)

if is_debug:
    plt.figure(figsize=(10, 10))
    plt.title('Raw map img')
    plt.imshow(raw_map_img, cmap='gray', origin='lower')
    plt.show()

# =====================================================================================================
# Conversion starting
# =====================================================================================================


# grayscale -> binary. Converts grey to black
map_img = raw_map_img.copy()
map_img[map_img <= 210.] = 0
map_img[map_img > 210.] = 1

if is_debug:
    plt.figure(figsize=(10, 10))
    plt.title('Gray scale image')
    plt.imshow(map_img, cmap='gray', origin='lower')
    plt.show()

# Calculate Euclidean Distance Transform (tells us distance to nearest wall)
dist_transform = scipy.ndimage.distance_transform_edt(map_img)

if is_debug:
    plt.figure(figsize=(10, 10))
    plt.title(
        'After euclidian distance transform (tells us distance to nearest wall)')
    plt.imshow(dist_transform, cmap='gray', origin='lower')
    plt.show()

# Threshold the distance transform to create a binary image
centers = dist_transform > thresold*dist_transform.max()
centerline = skeletonize(centers)

plt.figure(figsize=(10, 10))
plt.title('Make sure that there are no hairy lines on this graph. If so either clean the map so it is more curvy or increase thresold')
plt.imshow(centerline, origin='lower', cmap='gray')
plt.show()

centerline_dist = np.where(centerline, dist_transform, 0)
if is_debug:
    plt.figure(figsize=(10, 10))
    plt.title('Centerline with track width encoded')
    plt.imshow(centerline_dist, origin='lower', cmap='gray')
    plt.show()


# Find a proper starting position for DFS
NON_EDGE = 0.0
left_start_x = left_start_y = None
for x in range(centerline_dist.shape[1]):
    for y in range(centerline_dist.shape[0]):
        if (centerline_dist[y][x] != NON_EDGE):
            left_start_x, left_start_y = x, y
            break

    if left_start_x != None:
        break

# Use DFS to extract the outer edge
sys.setrecursionlimit(20000)

visited = {}
centerline_points = []
track_widths = []
# DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
# If you want the other direction first
DIRECTIONS = [(0, -1), (-1, 0),  (0, 1), (1, 0),
              (-1, 1), (-1, -1), (1, 1), (1, -1)]

starting_point = (left_start_x, left_start_y)


def dfs(point):
    if (point in visited):
        return
    visited[point] = True
    centerline_points.append(np.array(point))
    track_widths.append(np.array(
        [centerline_dist[point[1]][point[0]], centerline_dist[point[1]][point[0]]]))

    for direction in DIRECTIONS:
        if (centerline_dist[point[1] + direction[1]][point[0] + direction[0]] != NON_EDGE and (point[0] + direction[0], point[1] + direction[1]) not in visited):
            dfs((point[0] + direction[0], point[1] + direction[1]))


dfs(starting_point)


if is_debug:
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20, 5))
    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')
    ax4.axis('off')

    centerline_img = np.zeros(map_img.shape)
    for x, y in centerline_points[:len(centerline_points)//10]:
        centerline_img[y][x] = 255
    ax1.imshow(centerline_img, cmap='Greys', vmax=1, origin='lower')
    ax1.set_title("First 10% points")

    centerline_img = np.zeros(map_img.shape)
    for x, y in centerline_points[:len(centerline_points)//4]:
        centerline_img[y][x] = 255
    ax2.imshow(centerline_img, cmap='Greys', vmax=1, origin='lower')
    ax2.set_title("First 25% points")

    centerline_img = np.zeros(map_img.shape)
    for x, y in centerline_points[:int(len(centerline_points)/1.4)]:
        centerline_img[y][x] = 255
    ax3.imshow(centerline_img, cmap='Greys', vmax=1, origin='lower')
    ax3.set_title("First 50% points")

    centerline_img = np.zeros(map_img.shape)
    for x, y in centerline_points:
        centerline_img[y][x] = 1000
    ax4.imshow(centerline_img, cmap='Greys', vmax=1, origin='lower')
    ax4.set_title("All points")
    fig.tight_layout()
    plt.title('DFS result')
    plt.show()

# Reversing centerline, if necessary
if should_reverse_centerline:
    centerline_points = centerline_points[::-1]

# =====================================================================================================
# Convert track_widths to pandas and go from pixels to meters
# =====================================================================================================

track_widths_np = np.array(track_widths)
waypoints = np.array(centerline_points)
data = np.concatenate((waypoints, track_widths_np), axis=1)

# calculate map parameters
orig_x = origin[0]
orig_y = origin[1]
orig_s = np.sin(origin[2])
orig_c = np.cos(origin[2])

# get the distance transform
transformed_data = data
transformed_data *= map_resolution
transformed_data += np.array([orig_x, orig_y, 0, 0])

print(f'Output generated succesfully to {output_path}')
with open(output_path, 'wb') as fh:
    np.savetxt(fh, transformed_data, fmt='%0.4f', delimiter=',',
               header='x_m,y_m,w_tr_right_m,w_tr_left_m')


# =====================================================================================================
# Sanity check the final result
# =====================================================================================================
raw_data = pd.read_csv(output_path)
x = raw_data["# x_m"].values
y = raw_data["y_m"].values
wr = raw_data["w_tr_right_m"].values
wl = raw_data["w_tr_left_m"].values

x -= orig_x
y -= orig_y

x /= map_resolution
y /= map_resolution

plt.figure(figsize=(10, 10))
plt.imshow(map_img, cmap="gray", origin="lower")
plt.plot(x, y)
plt.title('Final centerline on the binary scale map')
plt.show()
