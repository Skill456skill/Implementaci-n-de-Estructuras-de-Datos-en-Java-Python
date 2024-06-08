class Pila:
    def __init__(self):
        self.pila = []

    def push(self, elemento):
        self.pila.append(elemento)

    def pop(self):
        return self.pila.pop() if self.pila else None

    def peek(self):
        return self.pila[-1] if self.pila else None

    def esta_vacia(self):
        return len(self.pila) == 0