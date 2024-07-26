import heapq
import os

def cargar_grafo(archivo):
    """
    Carga un grafo desde un archivo.

    Parámetros:
        archivo: La ruta del archivo que contiene el grafo.

    Devuelve:
        Una tupla (N, A, longitud) donde N es el conjunto de nodos,
        A es el conjunto de aristas y longitud es un diccionario que asigna a cada arista su longitud.
    """
    N = set()
    A = set()
    longitud = {}

    with open(archivo, 'r') as f:
        for linea in f:
            origen, destino, peso = linea.strip().split(',')
            origen, destino, peso = int(origen), int(destino), int(peso)
            N.add(origen)
            N.add(destino)
            A.add((origen, destino))
            longitud[(origen, destino)] = peso

    return N, A, longitud

def Kruskal(G, longitud, dirigido=False):
    """
    Algoritmo de Kruskal para encontrar el árbol de recubrimiento mínimo.

    Parámetros:
        G: Una tupla (N, A) donde N es el conjunto de nodos y A es el conjunto de aristas.
        longitud: Un diccionario que asigna a cada arista su longitud.
        dirigido: Booleano que indica si el grafo es dirigido.

    Devuelve:
        Un conjunto que contiene las aristas del árbol de recubrimiento mínimo.
    """
    N, A = G
    n = len(N)  # Número de nodos
    T = set()  # Conjunto que contendrá las aristas del árbol de recubrimiento mínimo

    # Diccionario que almacena los conjuntos de nodos (para union-find con compresión de ruta)
    parent = {nodo: nodo for nodo in N}
    rank = {nodo: 0 for nodo in N}

    # Ordenar las aristas por longitudes crecientes
    A_ordenada = sorted(A, key=lambda arista: longitud[arista])

    def find(nodo):
        """
        Función que busca el representante del conjunto que contiene un nodo dado.
        Implementa compresión de ruta.
        """
        if parent[nodo] != nodo:
            parent[nodo] = find(parent[nodo])
        return parent[nodo]

    def union(nodo1, nodo2):
        """
        Función que fusiona dos conjuntos usando union por rango.
        """
        root1 = find(nodo1)
        root2 = find(nodo2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    # Bucle voraz
    for e in A_ordenada:
        u, v = e

        # Si los extremos de la arista pertenecen a diferentes conjuntos, fusionarlos y agregar la arista a T
        if find(u) != find(v):
            union(u, v)
            T.add(e)

        # Si ya tenemos n-1 aristas, terminamos
        if len(T) == n - 1:
            break

    return T

def guardar_resultado(T, longitud, archivo_salida):
    """
    Guarda las aristas del árbol de recubrimiento mínimo en un archivo.

    Parámetros:
        T: Conjunto de aristas del árbol de recubrimiento mínimo.
        longitud: Diccionario que asigna a cada arista su longitud.
        archivo_salida: La ruta del archivo donde se guardará el resultado.
    """
    with open(archivo_salida, 'w') as f:
        for arista in T:
            u, v = arista
            f.write(f"{u},{v},{longitud[arista]}\n")

# Cargar el grafo desde el archivo
archivo = 'C:/Users/Usuario iTC/Documents/Ciclo 4/Anlisis1/Grafo50.txt'
N, A, longitud = cargar_grafo(archivo)

# Grafo representado como una tupla
G = (N, A)

# Ejecución del algoritmo de Kruskal para un grafo no dirigido
T = Kruskal(G, longitud)

# Guardar las aristas del árbol de recubrimiento mínimo en un archivo
archivo_resultado = 'C:/Users/Usuario iTC/Documents/Ciclo 4/Anlisis1/ArbolMinimo.txt'
guardar_resultado(T, longitud, archivo_resultado)

print(f"Resultado guardado en {archivo_resultado}")
