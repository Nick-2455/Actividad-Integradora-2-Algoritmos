'''
1. Leer un archivo de entrada que contiene la informacion de un grafo representado en forma de una matriz de adyacencias con grafos ponderados.
El peso de cada arista es la distancia en kilometros entre colonia y colonia, por donde es factible meter cableado.
El programa debe desplegar cual es la forma mas optima de cablear con fibra optica conectando colonias de tal forma que se pueda compartir informacion entre cuales quiera dos colonias.

Para probar el algoritmo necesitas ejecutar el siguiente comando en la terminal:
```
python -c "from algorithms.problema1 import resolver_problema1; resolver_problema1(r'data/inputsProblema1/inputProblema1.txt')"

```

'''
# Algoritmo de Prim para encontrar el arbol de expansion minima (MST)

# Se importan las librerias necesarias
import heapq

'''
Función para leer el grafo desde un archivo que contiene una matriz de
adyacencia y devolver una representación como lista de adyacencia.

Parámetros:
    nombreArchivo (str): ruta al archivo que contiene la matriz de adyacencia;
        cada fila corresponde a un nodo y los valores enteros representan el
        peso (distancia). Un valor 0 indica ausencia de arista.

Retorna:
    dict: mapa de nodo -> lista de tuplas (vecino, peso). Ejemplo: {0: [(1,5),(2,3)], 1: [...], ...}

Complejidad:
    Tiempo: O(n^2) en el peor caso, donde n es el número de nodos (se procesan
        todos los elementos de la matriz de adyacencia).
    Espacio: O(n^2) en el peor caso si el grafo es denso; la representación
        retornada es una lista de adyacencia (mejor en grafos dispersos).
'''
def leerGrafoDesdeArchivo(nombreArchivo):
    grafo = {}
    
    with open(nombreArchivo, 'r') as archivo:
        lineas = archivo.readlines()
        
        lineasValidas = [l.strip() for l in lineas if l.strip()]
        
        for i, linea in enumerate(lineasValidas):
            valores = list(map(int, linea.split()))
            grafo[i] = []
            
            for j, peso in enumerate(valores):
                if peso > 0:
                    grafo[i].append((j, peso))

    if not grafo:
        return {}
    
    return grafo

'''
Funcion para ejecutar el algoritmo de Prim y encontrar el arbol de expansion minima (MST)

Parámetros:
    grafo (dict): mapa de nodo -> lista de tuplas (vecino, peso).

Retorna:
    totalCosto (int): suma de los pesos del MST.
    aristasMST (list): lista de tuplas (nodo_u, nodo_v, peso) que forman el MST.

Complejidades computacionales:
    Tiempo: O(E log V) usando una cola de prioridad, donde E es el número de aristas y V el número de nodos.
    Espacio: O(V + E) para estructuras auxiliares (visitados, heap y lista de aristas).

Razon de las complejidades:
    Tiempo: Cada arista se procesa una vez y se inserta en la cola de prioridad, lo que toma O(log V) tiempo por operacion.
    Espacio: Se necesita O(V + E) espacio para almacenar los nodos visitados, la cola de prioridad y la lista de aristas.
'''
def prim(grafo):

    if not grafo:
        return 0, []
    
    totalCosto = 0
    aristasMST = []
    visitado = set()

    minHeap = [(0, 0, -1)]  # (costo, nodo_actual, nodo_padre)

    while minHeap:
        peso, nodoActual, nodoPadre = heapq.heappop(minHeap)

        if nodoActual in visitado:
            continue

        visitado.add(nodoActual)

        if nodoPadre != -1:
            aristasMST.append((nodoPadre, nodoActual, peso))
            totalCosto += peso
        
        for vecino, pesoArista in grafo[nodoActual]:
            if vecino not in visitado:
                heapq.heappush(minHeap, (pesoArista, vecino, nodoActual))
    
    return totalCosto, aristasMST


'''
Función principal que resuelve el problema: carga el grafo desde archivo,
calcula el MST mediante Prim y muestra el resultado.

Parámetros:
    ArchivoGrafo (str): ruta al archivo que contiene la matriz de adyacencia.

Retorna:
    totalCosto (int): costo total del MST.
    aristasMST (list): lista de aristas en el MST.

Complejidad:
    Tiempo: O(E log V) debido a la llamada a prim(), donde E es el número de aristas y V el número de nodos.
    Espacio: O(V + E) para almacenar el grafo y las estructuras auxiliares en prim().
'''
def resolver_problema1(ArchivoGrafo):
    grafo = leerGrafoDesdeArchivo(ArchivoGrafo)
    totalCosto, aristasMST = prim(grafo)

    print("Costo total para cablear las colonias:", totalCosto, "km")
    print("Aristas en el arbol de expansion minima (MST):")
    for arista in aristasMST:
        print(arista)

    return totalCosto, aristasMST
