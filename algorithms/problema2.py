"""
2. Debido a que las ciudades apenas están entrando al mundo tecnológico, se requiere que alguien 
visite cada colonia para ir a dejar estados de cuenta físicos, publicidad, avisos y notificaciones 
impresos. Por eso se quiere saber ¿cuál es la ruta más corta posible que visita cada colonia exactamente
una vez y al finalizar regresa a la colonia origen?

El programa debe desplegar la ruta a considerar, tomando en cuenta que la primera ciudad se le llamará A,
a la segunda B, y así sucesivamente.
"""

# Librería para realizar permutaciones al iterar.
from itertools import permutations
from .problema1 import leerGrafoDesdeArchivo

"""
Algoritmo de la ruta más corta hacia el punto de origen.

Parametros:
    grafo: list(list()) -> matriz hecha con listas

Retorna:
    ruta_corta: list, distancia_min: int

Complejidades computacionales y sus razones:
    Tiempo: O(n!) donde se itera en una permutación de n combinaciones posibles para encontrar la ruta.
    Espacio: O(n) donde se llenan n direcciones de memoria en arreglos unidimensionales.
"""
def TSP(grafo):
    N = len(grafo)
    distancia_min = float("inf")
    ruta_corta = []
    colonias = []

    # Llenar arreglo de colonias.
    for i in range(1, N):
        colonias.append(i)
    
    # Encontrar la ruta más corta.
    for p in permutations(colonias):
        ruta_actual = [0] + list(p)
        nodo_ruta_actual = 0
        distancia_ruta_actual = 0

        # Calcular la distancia de la ruta actual.
        for nodo in p:
            distancia_ruta_actual += grafo[nodo_ruta_actual][nodo]
            nodo_ruta_actual = nodo
        
        # Obtener la distancia más corta.
        distancia_ruta_actual += grafo[nodo_ruta_actual][0]
        
        if distancia_min > distancia_ruta_actual:
            distancia_min = distancia_ruta_actual
            ruta_corta = ruta_actual
    
    ruta_corta.append(0)
    return ruta_corta, distancia_min

"""
Convertir una ruta numérica a letras.

Parametros:
    ruta: list

Retorna:
    ruta_letras: list,

Complejidades computacionales y sus razones:
    Tiempo: O(n) donde se itera sobre n elementos en el arreglo.
    Espacio: O(n) donde se crean n direcciones de memoria en un nuevo arreglo.
"""
def ruta_nums_a_letras(ruta):
    ruta_letras = []
    for i in range(len(ruta)):
        ruta_letras.append(chr(ruta[i] + 65))
    return ruta_letras

def tsp_main(nombre_archivo):
    grafo = leerGrafoDesdeArchivo(nombre_archivo)

    # Si la función de lectura devuelve una lista de adyacencia (dict
    # con tuplas (vecino, peso)), convertirla a una matriz de adyacencia
    # para que TSP trabaje con valores numéricos.
    if isinstance(grafo, dict):
        N = len(grafo)
        # Crear matriz NxN inicializada con 0 (sin arista)
        matriz = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for vecino, peso in grafo.get(i, []):
                matriz[i][vecino] = peso
        grafo = matriz

    ruta, distancia_min = TSP(grafo)
    print(f"Ruta: {ruta_nums_a_letras(ruta)}\nDistancia mínima: {distancia_min}")

def resolver_problema2(nombre_archivo: str) -> None:
    """
    Función principal para el Problema 2.
    """
    tsp_main(nombre_archivo)


"""
Referencias:

- DSA The Traveling Salesman Problem. (s. f.). W3Schools. https://www.w3schools.com/dsa/dsa_ref_traveling_salesman.php
- Durán, M. A. (2025). TSP. Tecnológico de Monterrey. https://experiencia21.tec.mx/courses/601041/pages/tsp-2?module_item_id=38802846
- Python chr() Function. (s. f.). W3Schools. https://www.w3schools.com/python/ref_func_chr.asp
"""
