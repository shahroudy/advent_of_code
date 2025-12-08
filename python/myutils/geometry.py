import math
from itertools import product
from typing import Callable, Dict, Generator, List, Set, Tuple, Union

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

# 4D Masks for 8, 80, 81 directions
MASK8_4D = [
    [-1, 0, 0, 0],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, -1],
    [0, 0, 0, 1],
]
MASK80 = [[i, j, k, l] for i, j, k, l in product(range(-1, 2), repeat=4) if i or j or k or l]
MASK81 = [[i, j, k, l] for i, j, k, l in product(range(-1, 2), repeat=4)]


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

    def __mul__(self, factor: Union[int, float, "Point"]) -> "Point":
        if isinstance(factor, Point):
            return Point(self.x * factor.x, self.y * factor.y)
        else:
            return Point(self.x * factor, self.y * factor)

    def __eq__(self, other: "Point") -> bool:
        x, y = (other.x, other.y) if isinstance(other, Point) else other
        return self.x == x and self.y == y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __lt__(self, other: "Point") -> int:
        other_tuple = other.tuple if isinstance(other, Point) else tuple(other)
        return self.tuple < other_tuple

    def distance_squared(self, other: "Point") -> int:
        x, y = (other.x, other.y) if isinstance(other, Point) else other
        return (self.x - x) ** 2 + (self.y - y) ** 2

    def distance(self, other: "Point") -> float:
        return self.distance_squared(other) ** 0.5

    def manhattan_dist(self, other: "Point") -> int:
        x, y = (other.x, other.y) if isinstance(other, Point) else other
        return abs(self.x - x) + abs(self.y - y)

    def manhattan_range(self, distance: int) -> Generator["Point", None, None]:
        for dx in range(-distance, distance + 1):
            for dy in range(-distance + abs(dx), distance + 1 - abs(dx)):
                yield Point(self.x + dx, self.y + dy)

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

    def wrap_around(self, caller) -> "Point":
        self.x %= caller.cols
        self.y %= caller.rows

    def reflect(self, **kwargs) -> "Point":
        reflected = Point(self.x, self.y)
        if "x" in kwargs:
            axis_x = kwargs["x"]
            reflected.x = axis_x - (reflected.x - axis_x)
        if "y" in kwargs:
            axis_y = kwargs["y"]
            reflected.y = axis_y - (reflected.y - axis_y)
        if "p" in kwargs:
            axis_point = kwargs["p"]
            px, py = (axis_point.x, axis_point.y)
            reflected.x, reflected.y = px - (reflected.x - px), py - (reflected.y - py)
        return reflected

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

    def __mul__(self, factor: Union[int, float, "Point3D"]) -> "Point3D":
        if isinstance(factor, Point3D):
            return Point3D(self.x * factor.x, self.y * factor.y, self.z * factor.z)
        else:
            return Point3D(self.x * factor, self.y * factor, self.z * factor)

    def __eq__(self, other: "Point3D") -> bool:
        cx, cy, cz = (other.x, other.y, other.z) if isinstance(other, Point3D) else other
        return self.x == cx and self.y == cy and self.z == cz

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Point3D({self.x}, {self.y}, {self.z})"

    def __lt__(self, other: "Point3D") -> int:
        other_tuple = other.tuple if isinstance(other, Point3D) else tuple(other)
        return self.tuple < other_tuple

    def distance_squared(self, other: "Point3D") -> int:
        cx, cy, cz = (other.x, other.y, other.z) if isinstance(other, Point3D) else other
        return (self.x - cx) ** 2 + (self.y - cy) ** 2 + (self.z - cz) ** 2

    def distance(self, other: "Point3D") -> float:
        return self.distance_squared(other) ** 0.5

    def manhattan_dist(self, other: "Point3D") -> int:
        cx, cy, cz = (other.x, other.y, other.z) if isinstance(other, Point3D) else other
        return abs(self.x - cx) + abs(self.y - cy) + abs(self.z - cz)

    def manhattan_range(self, distance: int) -> Generator["Point3D", None, None]:
        for dx in range(-distance, distance + 1):
            for dy in range(-distance + abs(dx), distance + 1 - abs(dx)):
                for dz in range(-distance + abs(dx) + abs(dy), distance + 1 - abs(dx) - abs(dy)):
                    yield Point3D(self.x + dx, self.y + dy, self.z + dz)

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

    def wrap_around(self, caller) -> "Point3D":
        self.x %= caller.cols
        self.y %= caller.rows
        self.z %= caller.planes

    def reflect(self, **kwargs) -> "Point3D":
        reflected = Point3D(self.x, self.y, self.z)
        if "x" in kwargs:
            axis_x = kwargs["x"]
            reflected.x = axis_x - (reflected.x - axis_x)
        if "y" in kwargs:
            axis_y = kwargs["y"]
            reflected.y = axis_y - (reflected.y - axis_y)
        if "z" in kwargs:
            axis_z = kwargs["z"]
            reflected.z = axis_z - (reflected.z - axis_z)
        if "p" in kwargs:
            axis_point = kwargs["p"]
            px, py, pz = (axis_point.x, axis_point.y, axis_point.z)
            reflected.x, reflected.y, reflected.z = (
                px - (reflected.x - px),
                py - (reflected.y - py),
                pz - (reflected.z - pz),
            )
        return reflected

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


class Point4D:
    def __init__(self, x: int, y: int, z: int, w: int):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other: "Point4D") -> "Point4D":
        cx, cy, cz, cw = (
            (other.x, other.y, other.z, other.w) if isinstance(other, Point4D) else other
        )
        return Point4D(self.x + cx, self.y + cy, self.z + cz, self.w + cw)

    def __sub__(self, other: "Point4D") -> "Point4D":
        cx, cy, cz, cw = (
            (other.x, other.y, other.z, other.w) if isinstance(other, Point4D) else other
        )
        return Point4D(self.x - cx, self.y - cy, self.z - cz, self.w - cw)

    def __mul__(self, factor: Union[int, float, "Point4D"]) -> "Point4D":
        if isinstance(factor, Point4D):
            return Point4D(
                self.x * factor.x, self.y * factor.y, self.z * factor.z, self.w * factor.w
            )
        else:
            return Point4D(self.x * factor, self.y * factor, self.z * factor, self.w * factor)

    def __eq__(self, other: "Point4D") -> bool:
        cx, cy, cz, cw = (
            (other.x, other.y, other.z, other.w) if isinstance(other, Point4D) else other
        )
        return self.x == cx and self.y == cy and self.z == cz and self.w == cw

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z, self.w))

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self) -> str:
        return f"Point4D({self.x}, {self.y}, {self.z}, {self.w})"

    def __lt__(self, other: "Point4D") -> int:
        other_tuple = other.tuple if isinstance(other, Point4D) else tuple(other)
        return self.tuple < other_tuple

    def distance_squared(self, other: "Point4D") -> int:
        cx, cy, cz, cw = (
            (other.x, other.y, other.z, other.w) if isinstance(other, Point4D) else other
        )
        return (self.x - cx) ** 2 + (self.y - cy) ** 2 + (self.z - cz) ** 2 + (self.w - cw) ** 2

    def distance(self, other: "Point4D") -> float:
        return self.distance_squared(other) ** 0.5

    def manhattan_dist(self, other: "Point4D") -> int:
        cx, cy, cz, cw = (
            (other.x, other.y, other.z, other.w) if isinstance(other, Point4D) else other
        )
        return abs(self.x - cx) + abs(self.y - cy) + abs(self.z - cz) + abs(self.w - cw)

    def manhattan_range(self, distance: int) -> Generator["Point4D", None, None]:
        for dx in range(-distance, distance + 1):
            for dy in range(-distance + abs(dx), distance + 1 - abs(dx)):
                for dz in range(-distance + abs(dx) + abs(dy), distance + 1 - abs(dx) - abs(dy)):
                    for dw in range(
                        -distance + abs(dx) + abs(dy) + abs(dz),
                        distance + 1 - abs(dx) - abs(dy) - abs(dz),
                    ):
                        yield Point4D(self.x + dx, self.y + dy, self.z + dz, self.w + dw)

    def is_inside(self, caller) -> bool:
        return (
            0 <= self.x < caller.cols
            and 0 <= self.y < caller.rows
            and 0 <= self.z < caller.planes
            and 0 <= self.w < caller.hyperplanes
        )

    def n8(self) -> List["Point4D"]:
        return [
            Point4D(self.x + dx, self.y + dy, self.z + dz, self.w + dw)
            for dx, dy, dz, dw in MASK8_4D
        ]

    def n80(self) -> List["Point4D"]:
        return [
            Point4D(self.x + dx, self.y + dy, self.z + dz, self.w + dw) for dx, dy, dz, dw in MASK80
        ]

    def n81(self) -> List["Point4D"]:
        return [
            Point4D(self.x + dx, self.y + dy, self.z + dz, self.w + dw) for dx, dy, dz, dw in MASK81
        ]

    def wrap_around(self, caller) -> "Point4D":
        self.x %= caller.cols
        self.y %= caller.rows
        self.z %= caller.planes
        self.w %= caller.hyperplanes

    def reflect(self, **kwargs) -> "Point4D":
        reflected = Point4D(self.x, self.y, self.z, self.w)
        if "x" in kwargs:
            axis_x = kwargs["x"]
            reflected.x = axis_x - (reflected.x - axis_x)
        if "y" in kwargs:
            axis_y = kwargs["y"]
            reflected.y = axis_y - (reflected.y - axis_y)
        if "z" in kwargs:
            axis_z = kwargs["z"]
            reflected.z = axis_z - (reflected.z - axis_z)
        if "w" in kwargs:
            axis_w = kwargs["w"]
            reflected.w = axis_w - (reflected.w - axis_w)
        if "p" in kwargs:
            axis_point = kwargs["p"]
            px, py, pz, pw = (axis_point.x, axis_point.y, axis_point.z, axis_point.w)
            reflected.x, reflected.y, reflected.z, reflected.w = (
                px - (reflected.x - px),
                py - (reflected.y - py),
                pz - (reflected.z - pz),
                pw - (reflected.w - pw),
            )
        return reflected

    @property
    def tuple(self) -> Tuple[int, int, int, int]:
        return (self.x, self.y, self.z, self.w)


def connected_region(
    input_map: Union[Dict[Point, int], Set[Point], List[Point]],
    neighbors_func: Callable[[Point], List[Point]],
    connectivity_func: Callable[[Point, Point], bool],
    start: Point,
) -> Set[Point]:
    region = set()
    if isinstance(input_map, dict):
        labels = input_map
        points_to_process = set(input_map.keys())
    else:
        labels = {k: 0 for k in input_map}
        points_to_process = set(input_map)

    if start not in points_to_process:
        return region

    stack = [start]
    while stack:
        current = stack.pop()
        region.add(current)
        for neighbor in neighbors_func(current):
            if neighbor in points_to_process and connectivity_func(current, neighbor):
                points_to_process.remove(neighbor)
                stack.append(neighbor)
    return region


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
