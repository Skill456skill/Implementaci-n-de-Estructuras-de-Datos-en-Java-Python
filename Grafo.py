from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v):
        if u in self.grafo:
            self.grafo[u].append(v)
        else:
            self.grafo[u] = [v]

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        while cola:
            vertice = cola.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                cola.extend(set(self.grafo[vertice]) - visitados)
        return visitados

    def dfs(self, inicio):
        visitados, pila = set(), [inicio]
        while pila:
            vertice = pila.pop()
            if vertice not in visitados:
                visitados.add(vertice)
                pila.extend(set(self.grafo[vertice]) - visitados)
        return visitados

    def visualizar(self):
      G = nx.Graph(self.grafo)
      plt.figure(figsize=(8, 6))  # Especificar el tamaño de la figura
      nx.draw(G, with_labels=True)
      plt.show()
