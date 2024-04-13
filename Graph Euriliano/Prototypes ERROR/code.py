import numpy as np
import random

def create_graph(adjacency_matrix):
    V = len(adjacency_matrix)
    nodes = [chr(i + 65) for i in range(V)]  # Nombres de los nodos
    graph = [[] for _ in range(V)]
    for i in range(V):
        for j in range(i + 1, V):
            if adjacency_matrix[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    return nodes, graph

def DFS(nodes, graph, v, visited, edges_visited):
    visited[v] = True
    print(nodes[v], end=' ')
    for i in graph[v]:
        if (v, i) not in edges_visited:
            edges_visited.add((v, i))
            edges_visited.add((i, v))
            print(f"({nodes[v]}-{nodes[i]})", end=' ')
            DFS(nodes, graph, i, visited, edges_visited)

def is_connected(graph):
    visited = [False] * len(graph)
    start_node = random.randint(0, len(graph) - 1)
    DFS(nodes, graph, start_node, visited, set())
    return all(visited)

def is_eulerian(graph):
    if not is_connected(graph):
        return 0
    odd = sum(len(adj) % 2 for adj in graph)
    return 2 if odd == 0 else 1 if odd == 2 else 0

# Matriz de adyacencia del grafo
grafo = np.array([
    [0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0]
])

nodes, graph = create_graph(grafo)

result = is_eulerian(graph)
print("\nRuta del grafo:")
if result == 0:
    print("El grafo no es euleriano")
elif result == 1:
    print("\nEl grafo tiene un camino euleriano")
else:
    print("\nEl grafo tiene un ciclo euleriano")
