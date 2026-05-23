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


