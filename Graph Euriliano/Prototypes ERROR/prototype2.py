import numpy as np

class Grafo:
    def __init__(self, matriz_adyacencia):
        self.vertices = {}
        for i in range(len(matriz_adyacencia)):
            vertice = chr(65 + i)  # Convertir el índice a una letra mayúscula (A, B, C, ...)
            self.agregar_vertice(vertice)
            for j in range(len(matriz_adyacencia[i])):
                if matriz_adyacencia[i][j] == 1:
                    self.agregar_arista(vertice, chr(65 + j))

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append(destino)
            self.vertices[destino].append(origen)

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self):
        aristas = []
        for vertice, adyacentes in self.vertices.items():
            for adyacente in adyacentes:
                if (adyacente, vertice) not in aristas:
                    aristas.append((vertice, adyacente))
        return aristas

    def es_euleriano(self):
        grados = [len(adyacentes) for adyacentes in self.vertices.values()]
        pares_impares = sum(1 for grado in grados if grado % 2 != 0)
        if pares_impares == 0:
            return "El grafo es euleriano"
        elif pares_impares == 2:
            return "El grafo tiene un camino euleriano"
        else:
            return "El grafo no es euleriano"

    def encontrar_ruta_euleriana(self):
        if self.es_euleriano() in ["El grafo es euleriano", "El grafo tiene un camino euleriano"]:
            ruta = []
            stack = [next(iter(self.vertices))]
            while stack:
                vertice_actual = stack[-1]
                if self.vertices[vertice_actual]:
                    siguiente_vertice = self.vertices[vertice_actual].pop()
                    self.vertices[siguiente_vertice].remove(vertice_actual)
                    stack.append(siguiente_vertice)
                else:
                    ruta.append(stack.pop())
            return ruta[::-1]
        else:
            return "El grafo no es euleriano"


# Matriz de adyacencia del grafo
grafo_matriz = np.array([
    [0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0]
])

# Crear el grafo a partir de la matriz de adyacencia
grafo = Grafo(grafo_matriz)

# Imprimir los vértices y aristas del grafo
print("Vértices:", grafo.obtener_vertices())
print("Aristas:")
for arista in grafo.obtener_aristas():
    print(arista)

# Verificar si el grafo es euleriano y encontrar la ruta euleriana si es el caso
print(grafo.es_euleriano())
ruta_euleriana = grafo.encontrar_ruta_euleriana()
print("Ruta Euleriana:", ruta_euleriana)
