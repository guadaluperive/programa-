import tkinter as tk
from tkinter import messagebox

import heapq

class DijkstraVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Dijkstra Shortest Path Visualizer")

        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

        self.start_node = 'A'

        self.draw_graph()

        self.calculate_button = tk.Button(self.master, text="Calcular Ruta Más Corta", command=self.calculate_shortest_path)
        self.calculate_button.pack()

    def draw_graph(self):
        node_positions = {
            'A': (100, 100),
            'B': (300, 100),
            'C': (100, 300),
            'D': (300, 300)
        }

        for node in self.graph:
            x, y = node_positions[node]
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill='lightblue')
            self.canvas.create_text(x, y, text=node, font=('Arial', 12, 'bold'))

        for node in self.graph:
            x1, y1 = node_positions[node]
            for neighbor, weight in self.graph[node].items():
                x2, y2 = node_positions[neighbor]
                self.canvas.create_line(x1, y1, x2, y2, width=2, arrow=tk.LAST)

    def dijkstra(self):
        distances = {node: float('infinity') for node in self.graph}
        distances[self.start_node] = 0
        priority_queue = [(0, self.start_node)]
        path = {}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    path[neighbor] = current_node

        return distances, path

    def calculate_shortest_path(self):
        distances, path = self.dijkstra()
        messagebox.showinfo("Ruta Más Corta", f"Distancias más cortas desde el nodo {self.start_node}:\n{distances}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DijkstraVisualizer(root)
    root.mainloop()
