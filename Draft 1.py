#Starting off with Priority Queue to initialise the list to store the station names 
# where the lowest distance = highest priority 
#Version before AI fixed my bugs

class PriorityQueue :
    def __init__(self, data=None) :
        self.queue = []
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
