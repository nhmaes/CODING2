#Starting off with Priority Queue to initialise the list to store the station names 
# where the lowest distance = highest priority 

#these versions are made with mistakes as I could not figure ou =t how to turn off poroperly the AUTO SUGGEST feauture whoch is really annoying
# this meant that my code would would work between drafts but then not work because as an ensemble there 
# would be no coherence betwen certainuses of variables and methods since the AI would change them without me realising it and then I would have to go back and change them in other places which is really time consuming and frustrating
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
            return self._queue[-1]
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
        self.stations : dict[str, StationNode] = {}

    def append(self, name: str): 
        node = StationNode(name)
        if self.head :
            self.tail.next = node
            node.prev = self.tail
        else :
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

        pq = PriorityQueue([(start, 0)])
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
        graph.add_edge(name, STATIONS_WITH_DISTANCES[i + 1][0], minutes)

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
