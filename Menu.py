from NodoArbol import ArbolBinario
from Grafo import Grafo
from Pila import Pila
from Cola import Cola
from GrafoDijkstra import GrafoDijkstra


class Menu:
    def __init__(self):
        self.grafo = Grafo()
        self.arbol_binario = ArbolBinario()
        self.pila = Pila()
        self.cola = Cola()
        self.grafo_dijkstra = GrafoDijkstra()
        self.opciones = {
            "1": self.menu_bfs,
            "2": self.menu_dfs,
            "3": self.menu_arbol_binario,
            "4": self.menu_dijkstra,
            "5": self.menu_pila,
            "6": self.menu_cola,
            "7": self.menu_arbol_b_mas,
            "0": self.salir_programa
        }

    def mostrar_menu(self):
        print("""
        Menú Principal
        1. Búsqueda en anchura (BFS)
        2. Búsqueda en profundidad (DFS)
        3. Árboles binarios
        4. Algoritmo de Dijkstra
        5. Pilas
        6. Colas
        7. Árboles B+
        0. Salir
        """)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida.".format(opcion))

    def menu_bfs(self):
        print("\nSubmenú BFS")
        print("1. Insertar Arista")
        print("2. Búsqueda en Anchura")
        print("3. Visualizar Grafo")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            u = input("Ingrese el nodo de origen: ")
            v = input("Ingrese el nodo de destino: ")
            self.grafo.agregar_arista(u, v)
        elif opcion == "2":
            inicio = input("Ingrese el nodo de inicio: ")
            resultado = self.grafo.bfs(inicio)
            print("Nodos visitados en BFS:", resultado)
        elif opcion == "3":
            self.grafo.visualizar()
            # Agregar visualización después de cualquier operación
        elif opcion == "0":
            return
        else:
            print("Opción no válida.")

    def menu_dfs(self):
        print("\nSubmenú DFS")
        print("1. Insertar Arista")
        print("2. Búsqueda en Profundidad")
        print("3. Visualizar Grafo")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            u = input("Ingrese el nodo de origen: ")
            v = input("Ingrese el nodo de destino: ")
            self.grafo.agregar_arista(u, v)
        elif opcion == "2":
            inicio = input("Ingrese el nodo de inicio: ")
            resultado = self.grafo.dfs(inicio)
            print("Nodos visitados en DFS:", resultado)
        elif opcion == "3":
            self.grafo.visualizar()
            # Agregar visualización después de cualquier operación
        elif opcion == "0":
            return
        else:
            print("Opción no válida.")

    def menu_arbol_binario(self):
        print("\nSubmenú Árboles Binarios")
        print("1. Insertar Nodo")
        print("2. Visualizar Árbol")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            clave = int(input("Ingrese el valor del nodo: "))
            self.arbol_binario.insertar(clave)
        elif opcion == "2":
            self.arbol_binario.visualizar()
            # Agregar visualización después de cualquier operación
        elif opcion == "0":
            return
        else:
            print("Opción no válida.")


    def menu_dijkstra(self):
        print("\nSubmenú Dijkstra")
        print("1. Insertar Arista")
        print("2. Ejecutar Dijkstra")
        print("3. Visualizar Grafo")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            u = input("Ingrese el nodo de origen: ")
            v = input("Ingrese el nodo de destino: ")
            peso = int(input("Ingrese el peso de la arista: "))
            self.grafo_dijkstra.agregar_arista(u, v, peso)
        elif opcion == "2":
            inicio = input("Ingrese el nodo de inicio: ")
            distancias = self.grafo_dijkstra.dijkstra(inicio)
            print("Distancias desde el nodo", inicio, ":", distancias)
        elif opcion == "3":
            self.grafo_dijkstra.visualizar()
            # Agregar visualización después de cualquier operación
        elif opcion == "0":
            return
        else:
            print("Opción no válida.")

    def menu_pila(self):
        print("\nSubmenú Pilas")
        print("1. Apilar (Push)")
        print("2. Desapilar (Pop)")
        print("3. Mostrar Elemento Superior (Peek)")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            elemento = input("Ingrese el elemento a apilar: ")
            self.pila.push(elemento)
        elif opcion == "2":
            elemento = self.pila.pop()
            print("Elemento desapilado:", elemento)
        elif opcion == "3":
            elemento = self.pila.peek()
            print("Elemento superior de la pila:", elemento)
        elif opcion == "0":
            return
        else:
            print("Opción no válida.")


    def menu_cola(self):
        print("\nSubmenú Colas")
        print("1. Encolar (Enqueue)")
        print("2. Desencolar (Dequeue)")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            elemento = input("Ingrese el elemento a encolar: ")
            self.cola.enqueue(elemento)
        elif opcion == "2":
            elemento = self.cola.dequeue()
            print("Elemento desencolado:", elemento)
        elif opcion == "0":
            return
        else:
            print("Opción no válida.")

    def menu_arbol_b_mas(self):
        print("\nSubmenú Árboles B+ (Simplificado)")
        print("1. Insertar Nodo")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            clave = int(input("Ingrese el valor del nodo: "))
            # Implementar inserción en árbol B+ (Simplificado)
            print("Nodo insertado:", clave)
        elif opcion == "0":
            return
        else:
            print("Opción no válida.")

    def salir_programa(self):
      print("Saliendo del programa.")
      exit(0)


if __name__ == "__main__":
    Menu().ejecutar()
