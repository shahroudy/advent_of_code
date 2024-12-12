from itertools import product

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
    """A class representing a 2D point with integer coordinates.

    This class provides basic operations for 2D point manipulation including arithmetic
    operations, distance calculations, and neighbor point generation.

    Attributes:
        x (int): The x-coordinate of the point
        y (int): The y-coordinate of the point

    Methods:
        __add__(other): Add two points coordinate-wise
        __sub__(other): Subtract two points coordinate-wise
        __mul__(scalar): Multiply point coordinates by a scalar
        __eq__(other): Check if two points are equal
        __hash__(): Generate hash value for the point
        __str__(): String representation of the point
        manhattan_dist(other): Calculate Manhattan distance to another point
        is_inside(cols, rows): Check if point is within given boundaries
        n4(): Get 4-connected neighbors (N,S,E,W)
        n8(): Get 8-connected neighbors (N,S,E,W,NE,NW,SE,SW)
        n9(): Get 9-connected neighbors (includes center point)
        nx(): Get diagonal neighbors (NE,NW,SE,SW)
        tuple: Property that returns coordinates as a tuple
        NORTH(): Get adjacent point to the north
        SOUTH(): Get adjacent point to the south
        EAST(): Get adjacent point to the east
        WEST(): Get adjacent point to the west
    """

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

    def n4(self):
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK4]

    def n8(self):
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK8]

    def n9(self):
        return [Point(self.x + dx, self.y + dy) for dx, dy in MASK9]

    def nx(self):
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
    """A class representing a point in 3D space with integer coordinates.

    This class provides basic operations for 3D point manipulation including arithmetic
    operations, comparison, and various neighbor calculations.

    Attributes:
        x (int): The x-coordinate
        y (int): The y-coordinate
        z (int): The z-coordinate

    Methods:
        __add__(other): Add two points component-wise
        __sub__(other): Subtract two points component-wise
        __mul__(scalar): Multiply point coordinates by a scalar
        __eq__(other): Check if two points are equal
        __hash__(): Generate hash value for the point
        __str__(): String representation of the point
        manhattan_dist(other): Calculate Manhattan distance to another point
        is_inside(cols, rows, planes): Check if point is within given bounds
        n6(): Get 6-connected neighbors (face adjacency)
        n26(): Get 26-connected neighbors (vertex adjacency)
        n27(): Get 27-connected neighbors (including self)
        nx(): Get cross-shaped neighbors
        tuple: Property that returns coordinates as tuple
        NORTH(): Get adjacent point to the north (negative y)
        SOUTH(): Get adjacent point to the south (positive y)
        EAST(): Get adjacent point to the east (positive x)
        WEST(): Get adjacent point to the west (negative x)
        UP(): Get adjacent point above (positive z)
        DOWN(): Get adjacent point below (negative z)
    """

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

    def n6(self):
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK6]

    def n26(self):
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK26]

    def n27(self):
        return [Point3D(self.x + dx, self.y + dy, self.z + dz) for dx, dy, dz in MASK27]

    def nx(self):
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


def find_connected_components(input_map, neighbors_func):
    """Find connected components in a map using depth-first search.

    This function identifies and labels connected components in either a dictionary or set of
    points, where connectivity is defined by a custom neighbor function. Points are considered
    connected if they are neighbors and have the same label value.

    Args:
        input_map (Union[dict, set, list]): Either a dictionary mapping points to their labels,
            or a set/list of points (in which case all points are considered to have the same
            label 0).
        neighbors_func (Callable): A function that takes a point and returns an iterable of its
            neighbors.

    Returns:
        tuple[dict, dict]: A tuple containing:
            - components (dict): Maps component IDs to sets of points in each component.
            - components_map (dict): Maps each point to its component ID.

    Examples:
        >>> # Example with a grid where neighbors are adjacent cells
        >>> grid = {Point(0,0): 1, Point(0,1): 1, Point(1,0): 1, (1,1): 0}
        >>> components, mapping = find_connected_components(grid, Point.n4)
    """
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


def outer_border(region, neighbors_func):
    """Calculate the outer border points and their directions relative to a region.

    Args:
        region (set): A set of points representing a region in space
        neighbors_func (callable): A function that takes a point and returns its neighboring points

    Returns:
        set: A set of tuples (point, direction) where:
            - point: A point adjacent to but outside the region
            - direction: Vector from the closest region point to this border point

    Example:
        >>> region = {Point(0,0), Point(1,0)}
        >>> border = outer_border(region, Point.n4)
    """
    border = set()
    for point in region:
        for neighbor in neighbors_func(point):
            if neighbor not in region:
                border.add((neighbor, neighbor - point))
    return border


def inner_border(region, neighbors_func):
    """Calculate the inner border points and their directions relative to a region.

    Args:
        region (set): A set of points representing a region in space
        neighbors_func (callable): A function that takes a point and returns its neighboring points

    Returns:
        set: A set of tuples (point, direction) where:
            - point: A point adjacent to but outside the region
            - direction: Vector from the closest region point to this border point

    Example:
        >>> region = {Point(0,0), Point(1,0)}
        >>> border = inner_border(region, Point.n4)
    """
    border = set()
    for point in region:
        for neighbor in neighbors_func(point):
            if neighbor not in region:
                border.add((point, point - neighbor))
    return border


def region_perimeter(region, neighbors_func):
    """Calculate the perimeter of a region in a 2D grid.

    The perimeter is defined as the number of cells that form the outer border of the region.

    Args:
        region (set): A set of coordinates representing cells in the region.
        neighbors_func (callable): A function that takes a coordinate and returns its neighboring coordinates.

    Returns:
        int: The perimeter of the region, measured in number of border cells.

    Example:
        >>> region = {Point(0,0), Point(0,1), Point(1,0), Point(1,1)}
        >>> region_perimeter(region, Point.n4)
    """
    return len(outer_border(region, neighbors_func))
