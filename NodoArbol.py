import matplotlib.pyplot as plt
import networkx as nx

class NodoArbol:
    def __init__(self, clave):
        self.izquierda = None
        self.derecha = None
        self.valor = clave

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = NodoArbol(clave)
        else:
            self._insertar(self.raiz, clave)

    def _insertar(self, raiz, clave):
        if clave < raiz.valor:
            if raiz.izquierda is None:
                raiz.izquierda = NodoArbol(clave)
            else:
                self._insertar(raiz.izquierda, clave)
        else:
            if raiz.derecha is None:
                raiz.derecha = NodoArbol(clave)
            else:
                self._insertar(raiz.derecha, clave)

    def recorrido_inorden(self, raiz):
        return self._recorrido_inorden(raiz, [])

    def _recorrido_inorden(self, raiz, resultado):
        if raiz:
            resultado = self._recorrido_inorden(raiz.izquierda, resultado)
            resultado.append(raiz.valor)
            resultado = self._recorrido_inorden(raiz.derecha, resultado)
        return resultado

    def visualizar(self):
        def agregar_aristas(grafico, raiz):
            if raiz:
                if raiz.izquierda:
                    grafico.add_edge(raiz.valor, raiz.izquierda.valor)
                    agregar_aristas(grafico, raiz.izquierda)
                if raiz.derecha:
                    grafico.add_edge(raiz.valor, raiz.derecha.valor)
                    agregar_aristas(grafico, raiz.derecha)


        G = nx.Graph(self.grafo)
        plt.figure(figsize=(8, 6))  # Especificar el tamaño de la figura
        nx.draw(G, with_labels=True)
        plt.show()