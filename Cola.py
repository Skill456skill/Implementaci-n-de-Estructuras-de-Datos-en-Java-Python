class Cola:
    def __init__(self):
        self.cola = []

    def enqueue(self, elemento):
        self.cola.append(elemento)

    def dequeue(self):
        return self.cola.pop(0) if self.cola else None

    def esta_vacia(self):
        return len(self.cola) == 0