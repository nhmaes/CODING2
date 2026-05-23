# IMLPEMENTIN BASIC LINEAR ALGEBRA


#Starting off with Priority Queue to initialise the list to store the station names 
# where the lowest distance = highest priority 
#Version AFTER AI fixed my bugs

class PriorityQueue :
    def __init__(self, data=None) :
        self._queue = []
        if data :
            if data :
                for item in data:
                    self.add(item)


    def add(self,data) :
        self._queue.append(data)
        self._queue.sort(key=lambda x: x[1], reverse=True)
    
    def is_empty(self) :
        return len(self._queue) == 0
    
    def get(self):
        if not self.is_empty() :
            return self._queue.pop()
        return None
    
    def __repr__(self):
        return f"PriorityQueue({self._queue[::-1]})"

#setting up station nodes, each node holds a name,
#a link to the neighbouring station


class StationNode :
    def __init__(self,name: str) :
        self.name = name
        self.prev : "StationNode | None" = None
        self.next : "StationNode | None" = None

# what i use next is the repr method which i read online to be method is a special 
# Python method that defines how an object represents itself as a string, 
# particularly in the Python interpreter's console or when you call repr() on the object

    def __repr__(self):
        return f"Station({self.name!r})"
    
#CONCLUSION FOR PRIORITY QUEUE AND STATION NODE: 
# I have set up a priorirty queue to bascually organise the distance of the stations where
# priority actually represenrs distance
# Then I set up the manually implemented StationNode class which basically stores the
# name of the station + the link to the next one


# now im going to set up the graph class which is 
# basically a dictionary of station nodes and their neighbours

class DistrictLine :
    def __init__(self):
        self.head : "StationNode | None" = None
        self.tail : "StationNode | None" = None
        self._index : dict[str, StationNode] = {}

    def append(self, name: str) -> StationNode:
        node = StationNode(name)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node
        self._index[name] = node
        return node
    
    def get_node(self,name:str) :
        return self._index.get(name)
    
    def all_station_names(self) -> list[str]:
        names = []
        cur = self.head
        while cur:
            names.append(cur.name)
            cur = cur.next
        return names
    #cur means current -- as a point of reference down the distrcit line/linked list

#CONCLUSION FOR DISTRICT LINE SET UP
# I have set up where the stations kind of go on the sidstrict line , bascically where the head and tail f the line are,
# making sure that they don t actally have a data pointing to the node previously or after since
# since Richmond and Tower hill are terminals, they don't have a station/ data key pointing to the prev or next one


#now i am setting up the adacency list which is basically a graph :
# the nodes are vertices and the edges are links between the stations
class Graph:
    def __init__(self):
        self._adj: dict[str, dict[str, int]] = {}

    def add_edge(self, u: str, v: str, weight: int):
        self._adj.setdefault(u, {})[v] = weight
        self._adj.setdefault(v, {})[u] = weight

    def neighbours(self, station: str) -> dict[str, int]:
        return self._adj.get(station, {})
    
    def shortest_path(self, start: str, end: str) :
        dist : dict[str, int] = {start: 0}
        prev : dict[str, str | None] = {start: None}
        visited : set[str] = set()  

        pq = PriorityQueue()
        pq.add((start, 0))

        while not pq.is_empty():
            station, d = pq.get()

            if station in visited:        
                continue
            visited.add(station)          

            if station == end:
                break

            for neighbour, weight in self.neighbours(station).items():
                if neighbour not in visited:  
                    new_dist = d + weight
                    if new_dist < dist.get(neighbour, float("inf")):
                        dist[neighbour] = new_dist
                        prev[neighbour] = station
                        pq.add((neighbour, new_dist))

        path = []
        cur = end
        while cur is not None:
            path.append(cur)
            cur = prev.get(cur)
        path.reverse()
        return path, dist.get(end, float("inf"))

    
#Now im going to basically kind of buld the line, 
#i also decied to moe the list i created down here as it is easier since i originally created it at the top

STATIONS_WITH_DISTANCES = [
    # (station_name, minutes_to_next that are ALSO distance priority organisation)
    ("Richmond",          3),
    ("Kew Gardens",       3),
    ("Gunnersbury",       3),
    ("Turnham Green",     2),
    ("Stamford Brook",    2),
    ("Ravenscourt Park",  2),
    ("Hammersmith",       3),
    ("Barons Court",      2),
    ("West Kensington",   2),
    ("Earl's Court",      2),
    ("High Street Kensington", 3),
    ("Notting Hill Gate", 3),
    ("Bayswater",         2),
    ("Paddington",        3),
    ("Edgware Road",      2),
    ("Baker Street",      2),
    ("Great Portland Street", 1),
    ("Euston Square",     1),
    ("King's Cross St. Pancras", 3),
    ("Farringdon",        2),
    ("Barbican",          1),
    ("Moorgate",          2),
    ("Liverpool Street",  2),
    ("Aldgate",           2),
    ("Tower Hill",        0), 
]

def build_line () :
    line = DistrictLine()
    graph = Graph()

#this "_"(the underscore in the for loop) is Python's convention for a throwaway variable, 
# meaning I don't rlly need this value right now.
    for name, _ in STATIONS_WITH_DISTANCES:
        line.append(name)


    for i, (name, minutes) in enumerate(STATIONS_WITH_DISTANCES[:-1]):
        next_name = STATIONS_WITH_DISTANCES[i + 1][0]
        graph.add_edge(name, next_name, minutes)

    return line, graph

##conclision since my last one :
# I have set up the graph class which is basically a dictionary of station nodes and their neighbours
# I have also set up the shortest path method which is basically Dijkstra's algorithm to find the shortest path between two stations (even though its not really necessary) but it is important for basically giving us a path in general
# I have also set up the build line method which is basically building the line and the graph based on the list of stations and their distances that I created earlier

#route display setup : using set thoery to label the stops

def show_route(departure: str, destination: str, line: DistrictLine, graph: Graph):
    all_stations: set[str] = set(line.all_station_names())

    if departure not in all_stations:
        print(f"  '{departure}' is not on this line.")
        return
    if destination not in all_stations:
        print(f"  '{destination}' is not on this line.")
        return
    if departure == destination:
        print("  Departure and destination are the same station.")
        return

    path, total_time = graph.shortest_path(departure, destination)

    if not path or path[0] != departure:
        print("  No route found.")
        return
    
    route_set: set[str] = set(path)                       
    off_route_set: set[str] = all_stations - route_set     
    endpoints: set[str] = {departure, destination}

    print(f"\n  {'='*52}")
    print(f"  District Line  |  {departure} → {destination}")
    print(f"  Total journey time: ~{total_time} minutes")
    print(f"  Stations on route: {len(path) - 1} stop(s)")
    print(f"  {'='*52}") # '='*52 in the code, it uses Python's string repetition operator (*)
    # to repeat the = character 52 times, creating a line

    
    # after i set up a function that builds up cumulative travel times for each station on the route
    # It starts with cumulative = 0 and iterates through each station in the path using enumerate() 
    # to track the index. For stations after the first one (when i > 0), it retrieves the 
    # travel time between the previous station and the current one by calling graph.neighbours(path[i - 1]).get(station, 0)
    cumulative = 0
    pq = PriorityQueue()
    prev_dist = 0
    for i, station in enumerate(path):
        if i > 0:
            seg = graph.neighbours(path[i - 1]).get(station, 0)
            cumulative += seg
        pq.add((station, cumulative))

    ordered = []
    while not pq.is_empty():
        ordered.append(pq.get())

    print()
    for station, dist in ordered:
        if station == departure:
            tag = "  [DEPARTURE]"
        elif station == destination:
            tag = "  [DESTINATION]"
        else:
            tag = ""
        bar = "▓" * (dist // 2)
        print(f"  {dist:>3} min  {bar:<20}  {station}{tag}")

    print()
    print(f"  Stations skipped (not on your route): "
          f"{len(off_route_set)} station(s)")
    print(f"  Route set ∩ Line set = {len(route_set)} station(s)  ✓")
    print(f"  {'='*52}\n")


#FINALLLYYY setting up the main function that you sort of come up with at the very beginning of the porject
#but implement way after at the end as a conclusion to basically make the whole thing work

if __name__ == "__main__":
    line, graph = build_line()

    print("\n  District Line: Richmond → Tower Hill")
    print("  Available stations:")
    for i, name in enumerate(line.all_station_names(), 1):
        print(f"    {i:>2}. {name}")

    print()
    departure   = input("  Enter departure station: ").strip()
    destination = input("  Enter destination station: ").strip()

    show_route(departure, destination, line, graph)


#in order to implement linear transofrmations, i need to apply 2D properties/ cocnepts to the code
# give every station real x/y coordinates on a 2D map grid : build a Vector2D class —that supports addition and scalar multiplication
# build a Matrix2x2 class that supports matrix-vector multiplication
# use those to implement rotation, scaling, and translation as genuine linear transformations

from fnmatch import translate

import numpy as np
import math

#creating approximate coords ( XY ) for each stn

STATION_COORDS: dict[str, tuple[float, float]] = {
    "Richmond":                  (0.0,  0.0),
    "Kew Gardens":               (1.4,  0.3),
    "Gunnersbury":               (2.5,  0.4),
    "Turnham Green":             (3.4,  0.5),
    "Stamford Brook":            (4.1,  0.6),
    "Ravenscourt Park":          (4.8,  0.7),
    "Hammersmith":               (5.6,  0.5),
    "Barons Court":              (6.2,  0.2),
    "West Kensington":           (6.7,  0.0),
    "Earl's Court":              (7.2, -0.4),
    "High Street Kensington":    (7.6,  0.8),
    "Notting Hill Gate":         (8.4,  1.5),
    "Bayswater":                 (8.9,  1.7),
    "Paddington":                (9.5,  2.0),
    "Edgware Road":              (10.0, 2.1),
    "Baker Street":              (10.6, 2.5),
    "Great Portland Street":     (11.0, 2.8),
    "Euston Square":             (11.4, 3.0),
    "King's Cross St. Pancras":  (11.9, 3.3),
    "Farringdon":                (12.7, 2.9),
    "Barbican":                  (13.1, 2.8),
    "Moorgate":                  (13.6, 2.6),
    "Liverpool Street":          (14.1, 2.4),
    "Aldgate":                   (14.6, 2.1),
    "Tower Hill":                (15.0, 1.8),
}

#vector 2d implementation

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: float) -> "Vector2D":
        return self.__mul__(scalar)

    def __repr__(self) -> str:
        return f"Vector2D({self.x:.3f}, {self.y:.3f})"

    def as_array(self) -> np.ndarray:
        return np.array([self.x, self.y])


class Matrix2x2:
    def __init__(self, a: float, b: float, c: float, d: float):
        self._m = np.array([[a, b],
                            [c, d]], dtype=float)
        
    def apply(self, v: Vector2D) -> Vector2D:
        result = self._m @ v.as_array()  
        return Vector2D(result[0], result[1])

    def __matmul__(self, other: "Matrix2x2") -> "Matrix2x2":
        combined = self._m @ other._m
        a, b = combined[0]
        c, d = combined[1]
        return Matrix2x2(a, b, c, d)
    
    def __repr__(self) -> str:
        return (f"Matrix2x2(\n"
                f"  {self._m[0,0]:.4f}  {self._m[0,1]:.4f}\n"
                f"  {self._m[1,0]:.4f}  {self._m[1,1]:.4f}\n)")
    
    @staticmethod
    def rotation_matrix(degrees: float) -> "Matrix2x2":
        theta = math.radians(degrees)
        return Matrix2x2(
            math.cos(theta), -math.sin(theta),
            math.sin(theta),  math.cos(theta))
    
    @staticmethod
    def scaling_matrix(sx: float, sy: float) -> "Matrix2x2":
        return Matrix2x2(sx, 0.0, 0.0, sy)


def translate(v: Vector2D, offset: Vector2D) -> Vector2D:
    return v + offset
    
def apply_transform_to_map(
    coords: dict[str, tuple[float, float]],
    matrix: Matrix2x2,
    offset: Vector2D | None = None,
) -> dict[str, Vector2D]:
    transformed: dict[str, Vector2D] = {}
    for name, (x, y) in coords.items():
        v = Vector2D(x, y)
        v = matrix.apply(v)
        if offset is not None:
            v = translate(v, offset)
        transformed[name] = v
    return transformed

def show_map_transforms(stations_on_route: list[str] | None = None):
    
    display = stations_on_route if stations_on_route else list(STATION_COORDS)

    print(f"\n  {'='*60}")
    print(f"  MAP TRANSFORMATION DEMO  (numpy-backed Matrix2x2 / Vector2D)")
    print(f"  {'='*60}")

    
    print("\n  [1] TRANSLATION  — shift map (+5 km east, +2 km north)")
    print(f"      Formula:  v' = v + offset   where offset = (5.0, 2.0)")
    offset = Vector2D(5.0, 2.0)
    identity = Matrix2x2(1, 0, 0, 1)  
    translated = apply_transform_to_map(STATION_COORDS, identity, offset)
    for name in display:
        orig = Vector2D(*STATION_COORDS[name])
        new  = translated[name]
        print(f"      {name:<30}  ({orig.x:6.2f}, {orig.y:5.2f})  →  ({new.x:6.2f}, {new.y:5.2f})")

        print("\n  [2] SCALING  — zoom map to 1.5× in both axes")
        print(f"      Matrix S:\n"
          f"        | 1.5   0 |\n"
          f"        |   0 1.5 |")
    S = Matrix2x2.scaling_matrix(1.5, 1.5)
    scaled = apply_transform_to_map(STATION_COORDS, S)
    for name in display:
        orig = Vector2D(*STATION_COORDS[name])
        new  = scaled[name]
        print(f"      {name:<30}  ({orig.x:6.2f}, {orig.y:5.2f})  →  ({new.x:6.2f}, {new.y:5.2f})")

    print("\n  [3] ROTATION  — rotate map 45° anti-clockwise")
    theta = 45
    R = Matrix2x2.rotation_matrix(theta)
    print(f"      Matrix R(45°):\n{R}")
    rotated = apply_transform_to_map(STATION_COORDS, R)
    for name in display:
        orig = Vector2D(*STATION_COORDS[name])
        new  = rotated[name]
        print(f"      {name:<30}  ({orig.x:6.2f}, {orig.y:5.2f})  →  ({new.x:6.2f}, {new.y:5.2f})")

    print("\n  [4] COMBINED TRANSFORM  — rotate 30° THEN scale 2× (S @ R)")
    R30  = Matrix2x2.rotation_matrix(30)
    S2   = Matrix2x2.scaling_matrix(2.0, 2.0)
    combined = S2 @ R30          # Matrix2x2.__matmul__ — one combined matrix
    print(f"      Combined matrix (S @ R):\n{combined}")
    combo_result = apply_transform_to_map(STATION_COORDS, combined)
    for name in display:
        orig = Vector2D(*STATION_COORDS[name])
        new  = combo_result[name]
        print(f"      {name:<30}  ({orig.x:6.2f}, {orig.y:5.2f})  →  ({new.x:6.2f}, {new.y:5.2f})")

    print(f"\n  {'='*60}\n")

if __name__ == "__main__":
    line, graph = build_line()

    print("\n  District Line: Richmond → Tower Hill")
    print("  Available stations:")
    for i, name in enumerate(line.all_station_names(), 1):
        print(f"    {i:>2}. {name}")

    print()
    departure   = input("  Enter departure station: ").strip()
    destination = input("  Enter destination station: ").strip()

    show_route(departure, destination, line, graph)
   
    path, _ = graph.shortest_path(departure, destination)
    if path and path[0] == departure:
        print("\n  (Showing transforms for your route stations only)")
        show_map_transforms(stations_on_route=path)
    else:
        show_map_transforms()