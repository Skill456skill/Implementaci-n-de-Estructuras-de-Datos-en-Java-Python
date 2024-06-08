import networkx as nx
import heapq
import matplotlib.pyplot as plt

class GrafoDijkstra:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v, peso):
        if u in self.grafo:
            self.grafo[u].append((v, peso))
        else:
            self.grafo[u] = [(v, peso)]

    def dijkstra(self, inicio):
        heap = [(0, inicio)]
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0

        while heap:
            distancia_actual, nodo_actual = heapq.heappop(heap)

            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in self.grafo[nodo_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(heap, (distancia, vecino))

        return distancias

    def visualizar(self):
        G = nx.Graph()
        for nodo in self.grafo:
            for vecino, peso in self.grafo[nodo]:
                G.add_edge(nodo, vecino, weight=peso)
        posicion = nx.spring_layout(G)
        nx.draw(G, posicion, with_labels=True)
        etiquetas = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, posicion, edge_labels=etiquetas)
        plt.show()