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

#map_img : numpy.array

def gen_centerline(map_img_path,map_resolution, map_origin, threshold, reverse):

    '''
    Generate the centerline from a .pgm map.

            Parameters:
                    map_img (numpy.array): map image
                    map_resolution (float): map resolution.
                    map_origin (numpy.array): map origin.
                    threshold (float): threshold for the euclidean distance transform.
                    reverse (bool): reverse the order of the centerline points (By default its clockwise).

            Returns:
                    transformed_data (numpy.array): centerline points and track widths.
    '''

    map_img = np.array(Image.open(map_img_path).transpose(Image.FLIP_TOP_BOTTOM))
    map_img = map_img.astype(np.float64)

    # grayscale -> binary. Converts grey to black
    map_img[map_img <= 210.] = 0
    map_img[map_img > 210.] = 1

    # Calculate Euclidean Distance Transform (tells us distance to nearest wall)
    dist_transform = scipy.ndimage.distance_transform_edt(map_img)

    # Threshold the distance transform to create a binary image
    centers = dist_transform > threshold*dist_transform.max()
    centerline = skeletonize(centers)

    centerline_dist = np.where(centerline, dist_transform, 0)

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

    # Reversing centerline, if necessary
    if reverse:
        centerline_points = centerline_points[::-1]

    track_widths_np = np.array(track_widths)
    waypoints = np.array(centerline_points)
    data = np.concatenate((waypoints, track_widths_np), axis=1)

    # calculate map parameters
    orig_x = map_origin[0]
    orig_y = map_origin[1]

    # get the distance transform
    transformed_data = data
    transformed_data *= map_resolution
    transformed_data += np.array([orig_x, orig_y, 0, 0])

    return waypoints, track_widths_np, transformed_data


def display_centerline(map_img_path, waypoints):
    '''
    Display the centerline on the map.

            Parameters:
                    map_img (numpy.array): map image.
                    waypoints (numpy.array): centerline points.

            Returns:
                    displayed_img(numpy.array) : display the centerline on the map.
    '''

    map_img = np.array(Image.open(map_img_path).transpose(Image.FLIP_TOP_BOTTOM))
    map_img = map_img.astype(np.float64)

    # Display the waypoints on the map
    x = waypoints[:, 0]
    y = waypoints[:, 1]
    fig = plt.figure(figsize=(7, 3))
    plt.imshow(map_img, cmap="gray", origin="lower")
    plt.plot(x, y)
    plt.axis("off")
    plt.tight_layout()

    # Add an arrow to indicate direction
    arrow_start = waypoints[0]
    arrow_end = waypoints[10]  # You can adjust this index
    plt.arrow(arrow_start[0], arrow_start[1], arrow_end[0] - arrow_start[0], arrow_end[1] - arrow_start[1],
            head_width=5, head_length=5, fc='red', ec='red')
    
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)

    return image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

