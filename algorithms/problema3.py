from collections import deque
from .problema1 import leerGrafoDesdeArchivo


"""
Algoritmo de Edmonds-Karp para calcular el flujo máximo entre dos nodos.

Parámetros:
    capacidad: list(list()) -> matriz con las capacidades máximas entre nodos
    source: int -> nodo inicial
    sink: int -> nodo final

Retorna:
    max_flow: int

Complejidades computacionales y sus razones:
    Tiempo: O(V * E^2)
        En Edmonds-Karp, cada aumento de flujo usa BFS: O(E).
        Se realizan a lo más O(E * V) incrementos.
        Total: O(V * E^2).
    Espacio: O(V^2)
        Se almacena la matriz residual y estructuras auxiliares.
"""

def edmonds_karp(capacidad, source, sink):
    n = len(capacidad)

    # Matriz residual
    residual = [fila[:] for fila in capacidad]

    max_flow = 0

    while True:
        padre = [-1] * n
        padre[source] = source
        flujo_camino = bfs_encontrar_camino(residual, padre, source, sink)

        if flujo_camino == 0:
            break

        max_flow += flujo_camino

        nodo = sink
        while nodo != source:
            anterior = padre[nodo]
            residual[anterior][nodo] -= flujo_camino
            residual[nodo][anterior] += flujo_camino
            nodo = anterior

    return max_flow


"""
Búsqueda BFS para encontrar un camino aumentante.

Parámetros:
    residual: list(list()) -> matriz residual
    padre: list -> para reconstruir el camino
    source: int
    sink: int

Retorna:
    flujo_encontrado: int

Complejidades:
    Tiempo: O(V + E), donde la matriz se recorre implícitamente.
    Espacio: O(V) por las estructuras auxiliares.
"""

def bfs_encontrar_camino(residual, padre, source, sink):
    n = len(residual)
    visitado = [False] * n
    visitado[source] = True

    cola = deque()
    cola.append((source, float("inf")))

    while cola:
        nodo, flujo_actual = cola.popleft()

        for vecino in range(n):
            if not visitado[vecino] and residual[nodo][vecino] > 0:
                visitado[vecino] = True
                padre[vecino] = nodo
                nuevo_flujo = min(flujo_actual, residual[nodo][vecino])

                if vecino == sink:
                    return nuevo_flujo

                cola.append((vecino, nuevo_flujo))

    return 0


"""
Función principal para ejecutar el problema 3.

Parámetros:
    nombre_archivo: str -> archivo que contiene la matriz de capacidades

Retorna:
    No retorna, imprime el flujo máximo encontrado.

Complejidades:
    Tiempo: depende directamente de Edmonds-Karp: O(V * E^2)
    Espacio: O(V^2)
"""

def resolver_problema3(nombre_archivo):
    capacidad = leerGrafoDesdeArchivo(nombre_archivo)

    source = 0       # Primer nodo
    sink = len(capacidad) - 1   # Último nodo

    flujo_maximo = edmonds_karp(capacidad, source, sink)

    print(f"Flujo máximo entre {chr(source + 65)} y {chr(sink + 65)}: {flujo_maximo}")




"Referencias:"
"W3Schools.com. (s. f.). https://www.w3schools.com/dsa/dsa_algo_graphs_edmondskarp.php"