import itertools
from graphviz import Graph

class TSP:
    def __init__(self):
        self.cities = set()
        self.edges = {}

    def add_city(self, city):
        self.cities.add(city)

    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
            self.edges = {(c1, c2): dist for (c1, c2), dist in self.edges.items() if c1 != city and c2 != city}

    def add_edge(self, city1, city2, distance):
        if city1 in self.cities and city2 in self.cities:
            self.edges[(city1, city2)] = distance
            self.edges[(city2, city1)] = distance

    def solve_tsp(self):
        if len(self.cities) < 2:
            return [], 0

        cities = list(self.cities)
        shortest_path = None
        shortest_distance = float('inf')

        for path in itertools.permutations(cities):
            distance = sum(self.edges.get((path[i], path[i+1]), float('inf')) for i in range(len(path)-1))
            distance += self.edges.get((path[-1], path[0]), float('inf'))  # Return to start
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

        return list(shortest_path), shortest_distance

    def create_graph(self):
        dot = Graph(engine='neato')
        for city in self.cities:
            dot.node(city)
        for (city1, city2), distance in self.edges.items():
            if city1 < city2:  # Avoid duplicate edges
                dot.edge(city1, city2, label=str(distance))
        return dot