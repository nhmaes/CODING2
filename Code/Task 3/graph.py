class Graph:
    def __init__(self, vertices, edges):
        self.vertices = set(vertices)
        self.edges = edges

        self.adjacency_list = {}
        for vertex in vertices:
            self.adjacency_list[vertex] = []

            for edge in edges.keys():
                if vertex in edge:
                    for v in edge:
                        if v != vertex:
                            self.adjacency_list[vertex].append(v)
                            break

        self.incidence_matrix = {}
        for vertex in vertices:
            self.incidence_matrix[vertex] = {}

            for edge in edges.keys():
                if vertex in edge:
                    self.incidence_matrix[vertex][edge] = 1
                else:
                    self.incidence_matrix[vertex][edge] = 0

        self.adjacency_matrix = {}
        for vertex in vertices:
            self.adjacency_matrix[vertex] = {}

            for vertex2 in vertices:
                self.adjacency_matrix[vertex][vertex2] = 0

                for edge in edges.keys():
                    if (vertex != vertex2) and (vertex in edge) and (vertex2 in edge):
                        self.adjacency_matrix[vertex][vertex2] = 1

    def walk(self, source, target):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[source] = 0

        previous = {vertex: None for vertex in self.vertices}

        unvisited = [(0, source)]

        while unvisited:
            current_dist, current = min(unvisited)
            unvisited.remove((current_dist, current))

            if current == target:
                break

            for neighbour in self.adjacency_list[current]:
                edge = (current, neighbour) if (current, neighbour) in self.edges else (neighbour, current)
                new_dist = distances[current] + self.edges[edge]

                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist
                    previous[neighbour] = current
                    unvisited.append((new_dist, neighbour))

        path = []
        current = target
        while current is not None:
            path.insert(0, current)
            current = previous[current]

        return path
