from dataclasses import dataclass

@dataclass
class Origin:
    x: float
    y: float

@dataclass
class Map:
    name: str
    image_path: str
    resolution: float
    origin: Origin

@dataclass
class Centerline:
    name: str
    xs: list
    ys: list
    track_width_right: list
    track_width_left: list

@dataclass
class Raceline:
    name: str
    map_name: str
    color: str
    xs: list
    ys: list

