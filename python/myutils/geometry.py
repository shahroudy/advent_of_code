import math
from itertools import product
from typing import Callable, Dict, List, Set, Tuple, Union

from numpy import sign

# Some useful direction constants
DIRECTIONS = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}
TURN_LEFT = {"e": "n", "n": "w", "w": "s", "s": "e"}
TURN_RIGHT = {"e": "s", "s": "w", "w": "n", "n": "e"}
TURN_REVERSE = {"e": "w", "w": "e", "n": "s", "s": "n"}
DIR_CHARS = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
DIR_CHARS_TURN_LEFT = {">": "^", "^": "<", "<": "v", "v": ">"}
DIR_CHARS_TURN_RIGHT = {">": "v", "v": "<", "<": "^", "^": ">"}
DIR_CHARS_TURN_REVERSE = {">": "<", "<": ">", "^": "v", "v": "^"}

# 2D Masks for 4, 8, 9 and X directions
MASK4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
MASK8 = [[i, j] for i, j in product(range(-1, 2), repeat=2) if i or j]
MASK9 = [[i, j] for i, j in product(range(-1, 2), repeat=2)]
MASKX = [[1, 1], [-1, -1], [1, -1], [-1, 1]]

# 3D Masks for 6, 26, 27 and X directions
MASK6 = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
MASK26 = [[i, j, k] for i, j, k in product(range(-1, 2), repeat=3) if i or j or k]
MASK27 = [[i, j, k] for i, j, k in product(range(-1, 2), repeat=3)]
MASKX3D = [
    [1, 1, 1],
    [-1, -1, -1],
    [1, -1, 1],
    [-1, 1, -1],
    [1, 1, -1],
    [-1, -1, 1],
    [1, -1, -1],
    [-1, 1, 1],
]


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        x, y = (other.x, other.y) if isinstance(other, Point) else other
        return Point(self.x + x, self.y + y)

    def __sub__(self, other: "Point") -> "Point":
        x, y = (other.x, other.y) if isinstance(other, Point) else other
        return Point(self.x - x, self.y - y)

    def __mul__(self, scalar: int) -> "Point":
        return Point(self.x * scalar, self.y * scalar)

    def __eq__(self, other: "Point") -> bool:
        x, y = (other.x, other.y) if isinstance(other, Point) else other
        return self.x == x and self.y == y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def manhattan_dist(self, other: "Point") -> int:
        x, y = (other.x, other.y) if isinstance(other, Point) else other
        return abs(self.x - x) + abs(self.y - y)

    def is_inside(self, caller) -> bool:
        return 0 <= self.x < caller.cols and 0 <= self.y < caller.rows

    def n4(self) -> List["Point"]:
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK4]

    def n8(self) -> List["Point"]:
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK8]

    def n9(self) -> List["Point"]:
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK9]

    def nx(self) -> List["Point"]:
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASKX]

    def rotate(self, angle: int) -> "Point":
        if angle in (90, -270):
            self.x, self.y = self.y, -self.x
        elif angle in (180, -180):
            self.x, self.y = -self.x, -self.y
        elif angle in (270, -90):
            self.x, self.y = -self.y, self.x
        else:
            angle_radians = math.radians(-angle)  # Negative angle because of the coordinate system
            qx = math.cos(angle_radians) * self.x - math.sin(angle_radians) * self.y
            qy = math.sin(angle_radians) * self.x + math.cos(angle_radians) * self.y
            self.x, self.y = qx, qy

    def rotate_around(self, center: "Point", angle: int) -> "Point":
        cx, cy = (center.x, center.y) if isinstance(center, Point) else center
        if angle in (90, -270):
            self.x, self.y = cx - cy + self.y, cy + cx - self.x
        elif angle in (180, -180):
            self.x, self.y = 2 * cx - self.x, 2 * cy - self.y
        elif angle in (270, -90):
            self.x, self.y = cx + cy - self.y, cy - cx + self.x
        else:
            angle_radians = math.radians(-angle)  # Negative angle because of the coordinate system
            px, py = self.x - cx, self.y - cy
            qx = cx + math.cos(angle_radians) * px - math.sin(angle_radians) * py
            qy = cy + math.sin(angle_radians) * px + math.cos(angle_radians) * py
            self.x, self.y = qx, qy

    def normalize(self) -> "Point":
        return Point(sign(self.x), sign(self.y))

    @property
    def tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def NORTH(self) -> "Point":
        return Point(self.x, self.y - 1)

    def SOUTH(self) -> "Point":
        return Point(self.x, self.y + 1)

    def EAST(self) -> "Point":
        return Point(self.x + 1, self.y)

    def WEST(self) -> "Point":
        return Point(self.x - 1, self.y)


class Point3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Point3D") -> "Point3D":
        cx, cy, cz = (other.x, other.y, other.z) if isinstance(other, Point3D) else other
        return Point3D(self.x + cx, self.y + cy, self.z + cz)

    def __sub__(self, other: "Point3D") -> "Point3D":
        cx, cy, cz = (other.x, other.y, other.z) if isinstance(other, Point3D) else other
        return Point3D(self.x - cx, self.y - cy, self.z - cz)

    def __mul__(self, scalar: int) -> "Point3D":
        return Point3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other: "Point3D") -> bool:
        cx, cy, cz = (other.x, other.y, other.z) if isinstance(other, Point3D) else other
        return self.x == cx and self.y == cy and self.z == cz

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def manhattan_dist(self, other: "Point3D") -> int:
        cx, cy, cz = (other.x, other.y, other.z) if isinstance(other, Point3D) else other
        return abs(self.x - cx) + abs(self.y - cy) + abs(self.z - cz)

    def is_inside(self, caller) -> bool:
        return (
            0 <= self.x < caller.cols and 0 <= self.y < caller.rows and 0 <= self.z < caller.planes
        )

    def n6(self) -> List["Point3D"]:
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK6]

    def n26(self) -> List["Point3D"]:
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK26]

    def n27(self) -> List["Point3D"]:
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK27]

    def nx(self) -> List["Point3D"]:
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASKX3D]

    @property
    def tuple(self) -> Tuple[int, int, int]:
        return (self.x, self.y, self.z)

    def NORTH(self) -> "Point3D":
        return Point3D(self.x, self.y - 1, self.z)

    def SOUTH(self) -> "Point3D":
        return Point3D(self.x, self.y + 1, self.z)

    def EAST(self) -> "Point3D":
        return Point3D(self.x + 1, self.y, self.z)

    def WEST(self) -> "Point3D":
        return Point3D(self.x - 1, self.y, self.z)

    def UP(self) -> "Point3D":
        return Point3D(self.x, self.y, self.z + 1)

    def DOWN(self) -> "Point3D":
        return Point3D(self.x, self.y, self.z - 1)


def find_connected_components(
    input_map: Union[Dict[Point, int], Set[Point], List[Point]],
    neighbors_func: Callable[[Point], List[Point]],
) -> Tuple[Dict[int, Set[Point]], Dict[Point, int]]:
    components = {}
    components_map = {}
    if isinstance(input_map, dict):
        labels = input_map
        points_to_process = set(input_map.keys())
    else:
        labels = {k: 0 for k in input_map}
        points_to_process = set(input_map)

    component_id = 0
    while points_to_process:
        current = points_to_process.pop()
        components_map[current] = component_id
        current_component = set()
        current_component.add(current)
        stack = [current]
        while stack:
            current = stack.pop()
            for neighbor in neighbors_func(current):
                if (
                    neighbor in points_to_process
                    and labels[neighbor] == labels[current]
                    and neighbor not in current_component
                ):
                    points_to_process.remove(neighbor)
                    current_component.add(neighbor)
                    components_map[current] = component_id
                    stack.append(neighbor)
        components[component_id] = current_component
        component_id += 1
    return components, components_map


def outer_border(
    region: Set[Point], neighbors_func: Callable[[Point], List[Point]]
) -> Set[Tuple[Point, Point]]:
    border = set()
    for point in region:
        for neighbor in neighbors_func(point):
            if neighbor not in region:
                border.add((neighbor, neighbor - point))
    return border


def inner_border(
    region: Set[Point], neighbors_func: Callable[[Point], List[Point]]
) -> Set[Tuple[Point, Point]]:
    border = set()
    for point in region:
        for neighbor in neighbors_func(point):
            if neighbor not in region:
                border.add((point, point - neighbor))
    return border


def region_perimeter(region: Set[Point], neighbors_func: Callable[[Point], List[Point]]) -> int:
    return len(outer_border(region, neighbors_func))
