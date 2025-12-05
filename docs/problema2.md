# Problema 2 — Ruta más corta (visitar cada colonia y regresar al origen)

**Descripción**

- **Objetivo**: Dado un grafo no dirigido y ponderado que representa colonias (nodos) y las distancias (en kilómetros) factibles para ser visitadas, encontrar la ruta más corta posible, visitando cada colonia y regresando a la colonia de origen. Esto equivale a implementar el problema del viajero (TSP).

**Entrada**

- Un archivo de texto que contiene la matriz de adyacencia del grafo. Cada fila corresponde a una línea del archivo y contiene n enteros separados por espacios. El valor `0` indica que no hay arista directa entre dos nodos; cualquier otro entero positivo indica el peso (distancia en km) de la arista.

Formato del archivo (matriz n x n):

```
0 23 0 45 0
23 0 13 26 27
0 13 0 10 35
45 26 10 0 2
0 27 35 2 0
```

**Salida**

- La lista de nodos de la ruta más corta.
- La distancia mínima de la ruta más corta.

Ejemplo de salida esperada para el archivo anterior:

- Ruta: `['A', 'C', 'B', 'D', 'E', 'A']`
- Distancia mínima: `41` km

**Algoritmo recomendado**

- Esta implementación es la versión de fuerza bruta de TSP, el cual tiene una complejidad temporal de O(!n), mientras que existen otra implementación donde se utiliza programación dinámica, .

**Restricciones y supuestos**

- Matriz cuadrada de tamaño `n x n` (n ≥ 1).
- Pesos enteros no negativos; `0` significa ausencia de arista. La diagonal debe ser `0`.
- No es estrictamente necesario que todos los nodos estén conectados a cada uno. Pero es necesario todos los nodos estén conectados al menos a un nodo.

**Complejidad**

- Tiempo: O(n!) se itera sobre permutaciones para encontrar las diferentes rutas posibles.
- Espacio: O(n) se llenan n direcciones de memoria al crear listas de la ruta más corta, .

**Ejemplo de uso**

- Para ejecutar la función `resolver_problema2` incluida en `algorithms/problema2.py` con el archivo de ejemplo:

```powershell
python -c "from algorithms.problema2 import resolver_problema2; resolver_problema2(r'data/inputsProblema2/inputProblema2_1.txt')"
```

Salida esperada (resumen):

```
Ruta: ['A', 'C', 'B', 'D', 'E', 'A']
Distancia mínima: 41 km
```

**Referencias Bibliograficas**

- DSA The Traveling Salesman Problem. (s. f.). W3Schools. https://www.w3schools.com/dsa/dsa_ref_traveling_salesman.php

- Durán, M. A. (2025). TSP. Tecnológico de Monterrey. https://experiencia21.tec.mx/courses/601041/pages/tsp-2?module_item_id=38802846

- Python chr() Function. (s. f.). W3Schools. https://www.w3schools.com/python/ref_func_chr.asp