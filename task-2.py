import networkx as nx
from collections import deque

class Graph:
    def __init__(self):
        self.G = nx.Graph()
        self.create_network()

    def create_network(self):
        stations = [
            "Центральний вокзал", "Площа Свободи", "Парк культури",
            "Торговий центр", "Університет", "Спортивна",
            "Індустріальна", "Лікарня", "Ринок", "Житловий масив"
        ]

        self.G.add_nodes_from(stations)

        routes = [
            ("Центральний вокзал", "Площа Свободи", 3),
            ("Площа Свободи", "Парк культури", 2),
            ("Парк культури", "Торговий центр", 4),
            ("Торговий центр", "Університет", 1),
            ("Університет", "Спортивна", 2),
            ("Спортивна", "Індустріальна", 5),
            ("Індустріальна", "Лікарня", 3),
            ("Лікарня", "Ринок", 2),
            ("Ринок", "Житловий масив", 4),
            ("Житловий масив", "Центральний вокзал", 6),
            ("Площа Свободи", "Університет", 3),
            ("Парк культури", "Спортивна", 4),
            ("Торговий центр", "Лікарня", 5),
            ("Університет", "Ринок", 4),
            ("Спортивна", "Житловий масив", 3)
        ]

        self.G.add_weighted_edges_from(routes)

    def dfs_path(self, start, end, path=None, visited=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        path.append(start)
        visited.add(start)

        if start == end:
            return path

        for neighbor in self.G.neighbors(start):
            if neighbor not in visited:
                new_path = self.dfs_path(neighbor, end, path.copy(), visited)
                if new_path:
                    return new_path

        return None

    def bfs_path(self, start, end):
        queue = deque([[start]])
        visited = {start}

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == end:
                return path

            for neighbor in self.G.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return None

    def compare_paths(self, start, end):
        print(f"\nПорівняння шляхів від {start} до {end}:")

        dfs_result = self.dfs_path(start, end)
        print("\nDFS шлях:")
        print(" -> ".join(dfs_result))

        bfs_result = self.bfs_path(start, end)
        print("\nBFS шлях:")
        print(" -> ".join(bfs_result))

if __name__ == "__main__":
    graph = Graph()
    graph.compare_paths("Центральний вокзал", "Університет")