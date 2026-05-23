#Starting off with Priority Queue to initialise the list to store the station names 
# where the lowest distance = highest priority 
##Version before AI fixed my bugs


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

    
