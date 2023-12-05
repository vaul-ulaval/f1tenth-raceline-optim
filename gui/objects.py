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

@dataclass
class Raceline:
    name: str
    color: str
    xs: list
    ys: list

