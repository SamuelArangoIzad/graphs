import sys

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso):
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.vertices[vertice1][vertice2] = peso
        self.vertices[vertice2][vertice1] = peso

    def dijkstra(self, origen):
        distancias = {vertice: sys.maxsize for vertice in self.vertices}
        rutas = {vertice: [] for vertice in self.vertices}
        distancias[origen] = 0
        visitados = set()

        while len(visitados) < len(self.vertices):
            vertice_actual = min(
                (v for v in self.vertices if v not in visitados),
                key=lambda v: distancias[v]
            )

            visitados.add(vertice_actual)

            for vecino, peso in self.vertices[vertice_actual].items():
                nueva_distancia = distancias[vertice_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    # Aquí es donde se actualiza la ruta incorrectamente
                    # rutas[vecino] = rutas[vertice_actual] + [vertice_actual]
                    # Debería ser:
                    rutas[vecino] = rutas[vertice_actual] + [vecino]

        return distancias, rutas

def main():
    grafo = Grafo()

    grafo.agregar_arista('A', 'B', 10)
    grafo.agregar_arista('A', 'C', 8)
    grafo.agregar_arista('A', 'D', 15)
    grafo.agregar_arista('B', 'E', 15)
    grafo.agregar_arista('C', 'J', 14)
    grafo.agregar_arista('C', 'G', 15)
    grafo.agregar_arista('D', 'G', 6)
    grafo.agregar_arista('E', 'J', 8)
    grafo.agregar_arista('E', 'H', 30)
    grafo.agregar_arista('G', 'I', 7)
    grafo.agregar_arista('D', 'I', 15)
    grafo.agregar_arista('G', 'F', 8)
    grafo.agregar_arista('J', 'F', 9)
    grafo.agregar_arista('H', 'L', 15)
    grafo.agregar_arista('F', 'L', 15)
    grafo.agregar_arista('I', 'K', 10)
    grafo.agregar_arista('K', 'L', 10)
    grafo.agregar_arista('B', 'A', 10)
    grafo.agregar_arista('C', 'A', 8)
    grafo.agregar_arista('D', 'A', 15)
    grafo.agregar_arista('E', 'B', 15)
    grafo.agregar_arista('J', 'C', 14)
    grafo.agregar_arista('G', 'C', 15)
    grafo.agregar_arista('G', 'D', 6)
    grafo.agregar_arista('J', 'E', 8)
    grafo.agregar_arista('H', 'E', 30)
    grafo.agregar_arista('I', 'G', 7)
    grafo.agregar_arista('I', 'D', 15)
    grafo.agregar_arista('F', 'G', 8)
    grafo.agregar_arista('F', 'J', 9)
    grafo.agregar_arista('L', 'H', 15)
    grafo.agregar_arista('L', 'F', 15)
    grafo.agregar_arista('K', 'I', 10)
    grafo.agregar_arista('L', 'K', 10)

    while True:
        origen = input("Ingrese el punto inicial (A-L) o 'exit' para salir: ")
        if origen.lower() == 'exit':
            break
        if origen not in grafo.vertices:
            print("Punto inicial inválido.")
            continue

        destino = input("Ingrese el punto final (A-L): ")
        if destino not in grafo.vertices:
            print("Punto final inválido.")
            continue

        distancias, rutas = grafo.dijkstra(origen)
        distancia_final = distancias[destino]
        ruta_final = rutas[destino] + [destino]

        print(f"La distancia más corta de {origen} a {destino} es {distancia_final}.")
        print("La ruta más corta es:", ' -> '.join(ruta_final))

if __name__ == "__main__":
    main()
