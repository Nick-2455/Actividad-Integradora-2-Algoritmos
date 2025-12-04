# Problema 1 — Cableado óptimo de colonias (Árbol de expansión mínima)

**Descripción**

- **Objetivo**: Dado un grafo no dirigido y ponderado que representa colonias (nodos) y las distancias (en kilómetros) factibles para tender cableado (pesos en las aristas), encontrar la forma óptima de conectar las colonias con fibra óptica de manera que cualquier par de colonias pueda comunicarse. Esto equivale a calcular un Árbol de Expansión Mínima (MST) del grafo.

**Entrada**

- Un archivo de texto que contiene la matriz de adyacencia del grafo. Cada fila corresponde a una línea del archivo y contiene n enteros separados por espacios. El valor `0` indica que no hay arista directa entre dos nodos; cualquier otro entero positivo indica el peso (distancia en km) de la arista.
- Ejemplo de ruta de archivo: `data/inputsProblema1/inputProblema1.txt`.

Formato del archivo (matriz n x n):

```
0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0
```

**Salida**

- El costo total (suma de pesos) del cableado necesario para conectar todas las colonias (el coste del MST).
- La lista de aristas que componen el MST (pares de nodos y el peso de la arista).

Ejemplo de salida esperada para el archivo anterior:

- Costo total para cablear las colonias: `16` km
- Aristas en el MST: 4 aristas (cada una representada como `(nodo_u, nodo_v, peso)`).

**Algoritmo recomendado**

- Una implementación natural y eficiente para este problema es el algoritmo de Prim (o alternativamente Kruskal). En el código del repositorio se emplea Prim con una cola de prioridad (heap), obteniendo complejidad O(E log V) en términos de aristas E y nodos V.

**Restricciones y supuestos**

- Matriz cuadrada de tamaño `n x n` (n ≥ 1).
- Pesos enteros no negativos; `0` significa ausencia de arista. La diagonal debe ser `0`.
- El grafo puede ser conexo o no; si no hay forma de conectar todos los nodos, el algoritmo devolverá el MST del componente conectado que alcance desde el nodo inicial.

**Complejidad**

- Tiempo: O(E log V) usando un heap (Prim). Si se parte de matriz de adyacencia y se recorren todos los posibles vecinos, el coste práctico puede aproximarse a O(V^2) para grafos densos.
- Espacio: O(V^2) si se almacena la matriz de adyacencia; O(V) adicional para estructuras auxiliares (claves, padres, visitados).

**Ejemplo de uso**

- Para ejecutar la función `resolver_problema1` incluida en `algorithms/problema1.py` con el archivo de ejemplo:

```powershell
python -c "from algorithms.problema1 import resolver_problema1; resolver_problema1(r'data/inputsProblema1/inputProblema1.txt')"
```

Salida esperada (resumen):

```
Costo total para cablear las colonias: 16 km
Aristas en el arbol de expansion minima (MST):
(0, 1, 2)
(1, 2, 3)
(0, 3, 6)
(1, 4, 5)
```

**Referencias Bibliograficas**

- DSA Prim’s Algorithm. (s. f.). W3Schools.com. https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

- GeeksforGeeks. (2025c, agosto 29). Prim’s Algorithm for Minimum Spanning Tree (MST). GeeksforGeeks. https://www.geeksforgeeks.org/dsa/prims-minimum-spanning-tree-mst-greedy-algo-5/

- Algorithms for Competitive Programming. (2025, 30 junio). Algorithms For Competitive Programming. https://cp-algorithms.com/graph/mst_prim.html 