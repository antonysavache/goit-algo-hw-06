import networkx as nx

class WeightedGraph:
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

    def dijkstra_path(self, start, end):
        path = nx.dijkstra_path(self.G, start, end, weight='weight')
        distance = nx.dijkstra_path_length(self.G, start, end, weight='weight')
        return path, distance

    def find_all_shortest_paths(self):
        nodes = list(self.G.nodes())
        print("\nНайкоротші шляхи між усіма вершинами:")

        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                start = nodes[i]
                end = nodes[j]
                path, distance = self.dijkstra_path(start, end)
                print(f"\nВід {start} до {end}:")
                print(f"Шлях: {' -> '.join(path)}")
                print(f"Відстань: {distance} км")

if __name__ == "__main__":
    graph = WeightedGraph()
    graph.find_all_shortest_paths()