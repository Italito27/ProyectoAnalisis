def cargar_grafo(archivo):
    grafo = {}
    with open(archivo, 'r') as f:
        for linea in f:
            origen, destino, peso = map(int, linea.strip().split(','))
            if origen not in grafo:
                grafo[origen] = {}
            if destino not in grafo:
                grafo[destino] = {}
            grafo[origen][destino] = peso
            grafo[destino][origen] = peso  # Para grafo no dirigido
    return grafo

import heapq

def prim(graph):
    T = []  # Conjunto de aristas del árbol generador mínimo
    B = set()  # Conjunto de nodos incluidos en el árbol generador mínimo

    # Selecciona un nodo arbitrario para empezar
    start_node = next(iter(graph))
    B.add(start_node)

    # Cola de prioridad para seleccionar la arista de menor peso
    edges = [(weight, start_node, v) for v, weight in graph[start_node].items()]
    heapq.heapify(edges)

    while len(B) < len(graph):
        weight, u, v = heapq.heappop(edges)
        if v not in B:
            B.add(v)
            T.append((u, v, weight))

            for next_v, next_weight in graph[v].items():
                if next_v not in B:
                    heapq.heappush(edges, (next_weight, v, next_v))

    return T

def guardar_resultado(aristas, archivo_salida):
    with open(archivo_salida, 'w') as f:
        for u, v, peso in aristas:
            f.write(f"{u},{v},{peso}\n")

# Cargar el grafo desde el archivo
grafo = cargar_grafo('C:/Users/Usuario iTC/Documents/Ciclo 4/Anlisis1/Grafo50.txt')

# Encontrar el árbol generador mínimo usando el algoritmo de Prim
arbol_generador_minimo = prim(grafo)

# Guardar el resultado en un archivo
guardar_resultado(arbol_generador_minimo, 'C:/Users/Usuario iTC/Documents/Ciclo 4/Anlisis1/ResultadoGrafo.txt')
