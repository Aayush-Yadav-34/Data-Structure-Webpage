from graphviz import Digraph

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                self.graph[v] = [adj for adj in self.graph[v] if adj != vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_util(start_vertex, visited)
        return visited

    def _dfs_util(self, vertex, visited):
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    def create_graph(self):
        dot = Digraph()
        for vertex in self.graph:
            dot.node(str(vertex))
            for adj in self.graph[vertex]:
                dot.edge(str(vertex), str(adj))
        return dot