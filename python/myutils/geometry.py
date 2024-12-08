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

    @property
    def tuple(self):
        return (self.x, self.y)

    # Common grid directions
    @staticmethod
    def NORTH():
        return Point(0, -1)

    @staticmethod
    def SOUTH():
        return Point(0, 1)

    @staticmethod
    def EAST():
        return Point(1, 0)

    @staticmethod
    def WEST():
        return Point(-1, 0)


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

    @property
    def tuple(self):
        return (self.x, self.y, self.z)

    # Common grid directions
    @staticmethod
    def NORTH():
        return Point3D(0, -1, 0)

    @staticmethod
    def SOUTH():
        return Point3D(0, 1, 0)

    @staticmethod
    def EAST():
        return Point3D(1, 0, 0)

    @staticmethod
    def WEST():
        return Point3D(-1, 0, 0)

    @staticmethod
    def UP():
        return Point3D(0, 0, 1)

    @staticmethod
    def DOWN():
        return Point3D(0, 0, -1)
