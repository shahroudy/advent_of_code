from itertools import product
from typing import Callable, Dict, List, Set, Tuple, Union

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
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int) -> "Point":
        return Point(self.x * scalar, self.y * scalar)

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def manhattan_dist(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

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
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point3D") -> "Point3D":
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: int) -> "Point3D":
        return Point3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other: "Point3D") -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def manhattan_dist(self, other: "Point3D") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

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
