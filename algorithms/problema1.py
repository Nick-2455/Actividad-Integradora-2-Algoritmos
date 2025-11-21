'''
1. Leer un archivo de entrada que contiene la informacion de un grafo representado en forma de una matriz de adyacencias con grafos ponderados.
El peso de cada arista es la distancia en kilometros entre colonia y colonia, por donde es factible meter cableado.
El programa debe desplegar cual es la forma mas optima de cablear con fibra optica conectando colonias de tal forma que se pueda compartir informacion entre cuales quiera dos colonias.

'''
# Algoritmo de Prim para encontrar el arbol de expansion minima (MST)

# Se importan las liberias necesarias
import numpy as np # Se necesita instalar con pip install numpy
import heapq
from typing import List, Tuple


'''
Funcion para leer el grafo desde un archivo y devolver la matriz de adyacencia

Parametros:
    nombreArchivo: str, nombre del archivo que contiene la matriz de adyacencia

Retorna:
    matrizAdyacencia: np.array, matriz de adyacencia del grafo

Complejidades computacionales:
    Tiempo: O(V^2) donde V es el numero de nodos en el grafo
    Espacio: O(V^2) para almacenar la matriz de adyacencia

Razon de las complejidades:
    Tiempo: Se lee cada elemento de la matriz de adyacencia una vez, lo que toma O(V^2) tiempo.
    Espacio: La matriz de adyacencia requiere O(V^2) espacio para almacenarse.
'''
def leerGrafoDesdeArchivo(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        lineas = archivo.readlines()
        matrizAdyacencia = []
        for linea in lineas:
            fila = list(map(int, linea.strip().split()))
            matrizAdyacencia.append(fila)
    return np.array(matrizAdyacencia)

'''
Funcion para ejecutar el algoritmo de Prim y encontrar el arbol de expansion minima (MST)

Parametros:
    matrizAdyacencia: np.array, matriz de adyacencia del grafo

Retorna:
    totalCosto: int, costo total del MST
    aristasMST: list, lista de aristas en el MST

Complejidades computacionales:
    Tiempo: O(E log V) donde E es el numero de aristas y V es el numero de nodos en el grafo
    Espacio: O(V) para almacenar los nodos visitados y la cola de prioridad

Razon de las complejidades:
    Tiempo: Cada arista se procesa una vez y se inserta en la cola de prioridad, lo que toma O(log V) tiempo por operacion.
    Espacio: Se necesita O(V) espacio para almacenar los nodos visitados y la cola de prioridad.
'''
def prim(matrizAdyacencia) :
    numNodos = matrizAdyacencia.shape[0]
    visitado = [False] * numNodos
    minHeap = [(0, 0)]  # (costo, nodo)
    totalCosto = 0
    aristasMST = []

    while minHeap:
        costo, nodoActual = heapq.heappop(minHeap)
        if visitado[nodoActual]:
            continue
        visitado[nodoActual] = True
        totalCosto += costo

        for vecino in range(numNodos):
            peso = matrizAdyacencia[nodoActual][vecino]
            if peso > 0 and not visitado[vecino]:
                heapq.heappush(minHeap, (peso, vecino))
                aristasMST.append((nodoActual, vecino, peso))

    return totalCosto, aristasMST

'''
Funcion principal para ejecutar el programa

parametros:
    ArchivoGrafo: str, nombre del archivo que contiene la matriz de adyacencia del grafo

Retorna:
    None

Complejidades computacionales:
    Tiempo: O(E log V) donde E es el numero de aristas y V es el numero de nodos en el grafo
    Espacio: O(V^2) para almacenar la matriz de adyacencia

Razon de las complejidades:
    Tiempo: Dominado por la ejecucion del algoritmo de Prim.
    Espacio: Dominado por el almacenamiento de la matriz de adyacencia.
'''
def primMain(ArchivoGrafo):
    matrizAdyacencia = leerGrafoDesdeArchivo(ArchivoGrafo)
    totalCosto, aristasMST = prim(matrizAdyacencia)

    print("Costo total para cablear las colonias:", totalCosto, "km")
    print("Aristas en el arbol de expansion minima (MST):")
    for arista in aristasMST:
        print(arista)