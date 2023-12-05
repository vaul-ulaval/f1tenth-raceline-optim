from __future__ import annotations
from typing import Tuple
from attr import dataclass
import yaml
import os
from PIL import Image
import numpy as np
import scipy
from skimage.morphology import skeletonize
import sys

@dataclass
class MapYamlContent:
    map_resolution: float
    origin:  (float, float, float) # (x, y, z)
    
@dataclass
class ImageCenterline:
    waypoints: list[Tuple[int, int]] # (x, y)
    track_widths: list[Tuple[int, int]] # (w_right, w_left)

@dataclass
class RealCenterline:
    waypoints: list[Tuple[float, float]] # (x, y)
    track_widths: list[Tuple[float, float]] # (w_right, w_left)


def read_map_yaml(yaml_file_path: str) -> MapYamlContent:
    if not os.path.isfile(yaml_file_path):
        raise ValueError(f"File {yaml_file_path} does not exists")
    elif not yaml_file_path.endswith('.yaml'):
        raise ValueError(f"File {yaml_file_path} must have the .yaml extension")

    with open(yaml_file_path, 'r') as yaml_stream:
        map_metadata = yaml.safe_load(yaml_stream)
        map_resolution = map_metadata['resolution']
        origin = map_metadata['origin']

        return MapYamlContent(map_resolution, origin)
    

def read_map_pgm(pgm_file_path: str) -> np.ndarray:
    if not os.path.isfile(pgm_file_path):
        raise ValueError(f"File {pgm_file_path} does not exists")
    elif not pgm_file_path.endswith('.pgm'):
        raise ValueError(f"File {pgm_file_path} must have the .pgm extension")

    raw_map_img = np.array(Image.open(pgm_file_path).transpose(Image.FLIP_TOP_BOTTOM))
    raw_map_img = raw_map_img.astype(np.float64)

    return raw_map_img


def read_centerline_csv(csv_file_path: str) -> RealCenterline:
    if not os.path.isfile(csv_file_path):
        raise ValueError(f"File {csv_file_path} does not exists")
    elif not csv_file_path.endswith('.csv'):
        raise ValueError(f"File {csv_file_path} must have the .csv extension")

    waypoints_np = []
    track_widths_np = []

    with open(csv_file_path, 'r') as csv_stream:
        for line in csv_stream.readlines():
            x, y, w_left, w_right = line.split(',')
            waypoints_np.append((float(x), float(y)))
            track_widths_np.append((float(w_left), float(w_right)))

    return RealCenterline(waypoints_np, track_widths_np)


def write_centerline_csv(csv_file_path: str, centerline: RealCenterline):
    if not csv_file_path.endswith('.csv'):
        raise ValueError(f"File {csv_file_path} must have the .csv extension")

    with open(csv_file_path, 'w') as csv_stream:
        csv_stream.write('x_m,y_m,w_tr_right_m,w_tr_left_m\n')
        for x, y, w_right, w_left in zip(centerline.waypoints, centerline.track_widths):
            csv_stream.write(f"{x},{y},{w_right},{w_left}\n")


def gen_centerline_from_img(map_img: np.ndarray, thresold: float, should_reverse_centerline: bool) -> ImageCenterline:
    # grayscale -> binary. Converts grey to black
    img_copy: Image = map_img.copy()
    img_copy[map_img <= 210.] = 0
    img_copy[map_img > 210.] = 1

    # Calculate Euclidean Distance Transform (tells us distance to nearest wall)
    dist_transform: np.ndarray = scipy.ndimage.distance_transform_edt(map_img)

    # Threshold the distance transform to create a binary image
    centers: np.ndarray = dist_transform > thresold * dist_transform.max()
    centerline: np.ndarray = skeletonize(centers)

    # Only put distance values directly on the centerline
    NON_EDGE = 0.0
    centerline_dist: np.ndarray = np.where(centerline, dist_transform, NON_EDGE)

    # Find a proper starting position for DFS
    starting_point: (int, int) | None = None
    for x in range(centerline_dist.shape[1]):
        for y in range(centerline_dist.shape[0]):
            if (centerline_dist[y][x] != NON_EDGE):
                starting_point = (x, y)
                break

        if starting_point is not None:
            break

    if starting_point is None:
        raise ValueError("Could not find a starting point for the DFS")

    # Use DFS to extract the outer edge
    sys.setrecursionlimit(20000)
    DIRECTIONS: list[(int, int)] = [(0, -1), (-1, 0),  (0, 1), (1, 0),
                                    (-1, 1), (-1, -1), (1, 1), (1, -1)]

    visited: dict[(int, int), bool]= {}
    centerline_points: list[(int, int)] = []
    track_widths: list[(int, int)] = []

    def dfs(point: (int, int)):
        if point in visited:
            return
        
        visited[point] = True

        x, y = point
        centerline_points.append(np.array(point))

        track_width = centerline_dist[y][x]
        track_widths.append(np.array(track_width, track_width))

        for dx, dy in DIRECTIONS:
            candidate_point = x + dx, y + dy
            candidate_x, candidate_y = candidate_point
            candidate_dist = centerline_dist[candidate_y][candidate_x]

            if (candidate_dist != NON_EDGE and candidate_point not in visited):
                dfs(candidate_point)

    dfs(starting_point)

    # Reversing centerline, if necessary
    if should_reverse_centerline:
        centerline_points = centerline_points[::-1]

    return ImageCenterline(centerline_points, track_widths)


def convert_centerline_to_real(centerline: ImageCenterline, yaml_content: MapYamlContent) -> RealCenterline:
    waypoints_np = np.array(centerline.waypoints)
    track_widths_np = np.array(centerline.track_widths)

    # Calculate map parameters
    orig_x, orig_y, _ = yaml_content.origin
    map_resolution = yaml_content.map_resolution

    # Get the distance transform
    waypoints_np *= map_resolution
    waypoints_np += np.array([orig_x, orig_y])

    track_widths_np *= map_resolution

    return RealCenterline(waypoints_np.tolist(), track_widths_np.tolist())


def convert_centerline_to_image(centerline: RealCenterline, yaml_content: MapYamlContent) -> ImageCenterline:
    waypoints_np = np.array(centerline.waypoints)
    track_widths_np = np.array(centerline.track_widths)

    # Calculate map parameters
    orig_x, orig_y, _ = yaml_content.origin
    map_resolution = yaml_content.map_resolution

    # Get the distance transform
    waypoints_np -= np.array([orig_x, orig_y])
    waypoints_np /= map_resolution

    track_widths_np /= map_resolution

    return ImageCenterline(waypoints_np.tolist(), track_widths_np.tolist())