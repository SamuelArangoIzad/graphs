import numpy as np
import random

def create_graph(adjacency_matrix):
    V = len(adjacency_matrix)
    graph = [[] for _ in range(V)]
    for i in range(V):
        for j in range(i + 1, V):
            if adjacency_matrix[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def DFS(graph, v, visited, edges_visited, cycle):
    visited[v] = True
    cycle.append(chr(v + 65))  # Convertir el número del nodo a letra
    for i in graph[v]:
        if (v, i) not in edges_visited:
            edges_visited.add((v, i))
            edges_visited.add((i, v))
            DFS(graph, i, visited, edges_visited, cycle)

def find_eulerian_cycle(graph):
    odd_degrees = sum(len(adj) % 2 for adj in graph)
    if odd_degrees != 0:
        return None
    visited = [False] * len(graph)
    start_node = random.randint(0, len(graph) - 1)
    cycle = []
    DFS(graph, start_node, visited, set(), cycle)
    cycle.append(chr(start_node + 65))  # Convertir el número del nodo a letra
    return cycle

# Matriz de adyacencia del grafo
grafo = np.array([
    [0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0]
])

graph = create_graph(grafo)

cycle = find_eulerian_cycle(graph)
print("\nRuta del grafo:")
if cycle:
    for node in cycle[:-1]:
        print(node + " -> ")
    print(cycle[-1])  # Imprime el último nodo sin " -> "
else:
    print("El grafo no tiene un ciclo euleriano")
