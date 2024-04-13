import sys
class Grafo:
    def __init__(self):
        self.vertices = {}  # Diccionario para almacenar los vértices y sus adyacencias con pesos

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}  # Se agrega un nuevo vértice al grafo

    def agregar_arista(self, vertice1, vertice2, peso):
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.vertices[vertice1][vertice2] = peso  # Se agrega una arista con peso entre dos vértices
        self.vertices[vertice2][vertice1] = peso  # La arista es bidireccional, por lo que se añade en ambas direcciones

    def dijkstra(self, origen):
        # Inicialización de las distancias: Se crea un diccionario donde la distancia a cada vértice desde el origen es inicializada a infinito.
        distancias = {vertice: sys.maxsize for vertice in self.vertices}

        # Inicialización de las rutas: Se crea un diccionario donde se almacenarán las rutas más cortas desde el origen a cada vértice.
        rutas = {vertice: [] for vertice in self.vertices}

        # La distancia al vértice origen se establece como 0, ya que es el punto de partida del algoritmo.
        distancias[origen] = 0

        # Conjunto para almacenar los vértices que ya han sido visitados.
        visitados = set()

        # Se sigue iterando mientras no se hayan visitado todos los vértices del grafo.
        while len(visitados) < len(self.vertices):
            # Seleccionar el vértice no visitado más cercano, es decir, aquel con la distancia mínima desde el origen.
            vertice_actual = min(
                (v for v in self.vertices if v not in visitados),
                key=lambda v: distancias[v]
            )

            # Marcar el vértice actual como visitado, para evitar volver a visitarlo.
            visitados.add(vertice_actual)

            # Explorar los vecinos del vértice actual.
            for vecino, peso in self.vertices[vertice_actual].items():
                # Calcular la nueva distancia desde el origen al vecino pasando por el vértice actual.
                nueva_distancia = distancias[vertice_actual] + peso

                # Actualizar la distancia si la nueva distancia es menor que la distancia actual almacenada para el vecino.
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    # Actualizar la ruta más corta para llegar al vecino.
                    # La ruta al vecino es la ruta al vértice actual más el vecino.
                    rutas[vecino] = rutas[vertice_actual] + [vecino]

        # Devolver las distancias y rutas más cortas calculadas.
        return distancias, rutas


def main():
    grafo = Grafo()  # Crear un nuevo grafo

    grafo.agregar_arista('A', 'B', 10)
    grafo.agregar_arista('A', 'C', 8)
    grafo.agregar_arista('A', 'D', 15)
    grafo.agregar_arista('B', 'E', 15)
    grafo.agregar_arista('C', 'J', 14)
    grafo.agregar_arista('C', 'G', 15)
    grafo.agregar_arista('D', 'I', 15)
    grafo.agregar_arista('D', 'G', 6)
    grafo.agregar_arista('E', 'H', 30)
    grafo.agregar_arista('E', 'J', 8)
    grafo.agregar_arista('G', 'I', 7)
    grafo.agregar_arista('G', 'F', 8)
    grafo.agregar_arista('J', 'F', 9)
    grafo.agregar_arista('J','H',  18)
    grafo.agregar_arista('F', 'L', 15)
    grafo.agregar_arista('I', 'K', 10)
    grafo.agregar_arista('K', 'L', 10)
    grafo.agregar_arista('H', 'L', 15)



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


        distancias, rutas = grafo.dijkstra(origen)  # Obtener las distancias y rutas más cortas desde el origen
        distancia_final = distancias[destino]  # Obtener la distancia más corta al destino
        ruta_final = rutas[destino] + [destino]  # Obtener la ruta más corta al destino

        print(f"La distancia más corta de {origen} a {destino} es {distancia_final}.")
        print("La ruta más corta es:", ' -> '.join(ruta_final))

if __name__ == "__main__":
    main()
