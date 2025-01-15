import networkx as nx
import matplotlib.pyplot as plt

class TransportNetwork:
    def __init__(self):
        self.G = nx.Graph()

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

    def visualize(self):
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.G)

        nx.draw(self.G, pos, with_labels=True, node_color='lightblue',
                node_size=1500, font_size=8, font_weight='bold')

        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        plt.title("Транспортна мережа міста")
        plt.axis('off')
        plt.show()

    def analyze(self):
        print("\nАналіз мережі:")
        print(f"Кількість станцій: {self.G.number_of_nodes()}")
        print(f"Кількість маршрутів: {self.G.number_of_edges()}")

        print("\nСтупінь вершин (кількість зв'язків для кожної станції):")
        for node in self.G.nodes():
            print(f"{node}: {self.G.degree(node)}")

if __name__ == "__main__":
    network = TransportNetwork()
    network.create_network()
    network.visualize()
    network.analyze()