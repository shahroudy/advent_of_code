from itertools import product

# Some usefule direction constants
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

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int):
        return Point(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def manhattan_dist(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def is_inside(self, cols, rows):
        return 0 <= self.x < cols and 0 <= self.y < rows

    def neighbors_4(self):
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK4]

    def neighbors_8(self):
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK8]

    def neighbors_9(self):
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK9]

    def neighbors_x(self):
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASKX]

    @property
    def tuple(self):
        return (self.x, self.y)

    def NORTH(self):
        return Point(self.x, self.y - 1)

    def SOUTH(self):
        return Point(self.x, self.y + 1)

    def EAST(self):
        return Point(self.x + 1, self.y)

    def WEST(self):
        return Point(self.x - 1, self.y)


class Point3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: int):
        return Point3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def manhattan_dist(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def is_inside(self, cols, rows, planes):
        return 0 <= self.x < cols and 0 <= self.y < rows and 0 <= self.z < planes

    def neighbors_6(self):
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK6]

    def neighbors_26(self):
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK26]

    def neighbors_27(self):
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK27]

    def neighbors_x(self):
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASKX3D]

    @property
    def tuple(self):
        return (self.x, self.y, self.z)

    def NORTH(self):
        return Point3D(self.x, self.y - 1, self.z)

    def SOUTH(self):
        return Point3D(self.x, self.y + 1, self.z)

    def EAST(self):
        return Point3D(self.x + 1, self.y, self.z)

    def WEST(self):
        return Point3D(self.x - 1, self.y, self.z)

    def UP(self):
        return Point3D(self.x, self.y, self.z + 1)

    def DOWN(self):
        return Point3D(self.x, self.y, self.z - 1)
