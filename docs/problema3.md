# Problema 3 — Flujo máximo de información entre dos colonias

**Descripción**

- **Objetivo**: Dado un grafo dirigido y ponderado donde cada arista representa la capacidad máxima de transmisión de datos entre dos colonias, determinar cuánto flujo máximo puede enviarse desde un nodo origen hasta un nodo destino.  
  Este problema corresponde al cálculo del flujo máximo en una red de transporte, y suele resolverse mediante el algoritmo de Edmonds–Karp (una implementación de Ford–Fulkerson usando BFS).

**Entrada**

- Un archivo de texto que contiene la matriz de capacidades del grafo.  
  Cada fila del archivo corresponde a una línea y contiene `n` enteros separados por espacios.  
  El valor `0` indica ausencia de capacidad entre dos nodos; un entero positivo representa la capacidad máxima de flujo (por ejemplo, en Mbps).

Formato del archivo (matriz n x n):

0 16 13 0 0 0
0 0 10 12 0 0
0 4 0 0 14 0
0 0 9 0 0 20
0 0 0 7 0 4
0 0 0 0 0 0


**Salida**

- Valor del flujo máximo desde el nodo inicial (siempre el primero del archivo, nodo A) hasta el nodo final (el último del archivo).
- El cálculo se muestra en la consola al ejecutar la función principal.

Ejemplo de salida esperada para el archivo anterior:


**Algoritmo recomendado**

- Se utiliza **Edmonds–Karp**, una variante del método de aumentos sucesivos de Ford–Fulkerson, que emplea búsqueda en anchura (BFS) para encontrar caminos aumentantes.
- Es un algoritmo estándar, fácil de implementar y con complejidad polinómica.

**Restricciones y supuestos**

- La matriz debe ser cuadrada (`n x n`), con `n ≥ 2`.
- Los valores deben ser enteros mayores o iguales a cero.
- `0` indica ausencia de capacidad directa entre dos nodos.
- El nodo de origen es el índice `0` (colonia A).
- El nodo destino es el índice `n−1` (última colonia).

**Complejidad**

- Tiempo: O(V · E²).  
  En Edmonds–Karp, cada augmenting path se obtiene con BFS y puede repetirse a lo largo del proceso.
- Espacio: O(V²), por las matrices residuales y estructuras auxiliares.

**Ejemplo de uso**

Para ejecutar la función `resolver_problema3` incluida en `algorithms/problema3.py` con un archivo de entrada:

```powershell
python -c "from algorithms.problema3 import resolver_problema3; resolver_problema3(r'data/inputsProblema3/inputProblema3.txt')"


Salida esperada:

Flujo máximo entre nodo inicial y nodo final: 23