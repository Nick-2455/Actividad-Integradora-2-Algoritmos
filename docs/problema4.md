# Problema 4: Selección de la Central Más Cercana y Generación de Polígonos Voronoi

### Documentación Técnica (Formato Markdown)

---

## 1. Descripción del problema

El objetivo es determinar, para cada nueva contratación (una casa con coordenadas en un plano 2D), **qué central es la más cercana**. Además, se debe construir una **representación geométrica** del área de influencia de cada central en forma de **polígonos**, derivada de una aproximación a un **diagrama de Voronoi**, aprovechando técnicas que sí se vieron en clase.

La solución implementada:

1. Calcula la central más cercana usando distancia euclidiana.
2. Genera regiones aproximadas de Voronoi mediante grid sampling.
3. Obtiene un polígono por central empleando Convex Hull (Monotone Chain).
4. Produce una visualización obligatoria.
5. Devuelve resultados estructurados para integrarse al programa principal.

Sí, todo esto en un solo módulo, sin que el `main.py` se ensucie las manos.

---

## 2. Fundamento teórico

### 2.1 Distancia Euclidiana

Para cada casa (p = (x_1, y_1)) y cada central (c = (x_2, y_2)), se calcula:

$$
d(p, c) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
$$

El punto se asigna a la central con menor distancia.

---

### 2.2 Aproximación a Diagramas de Voronoi

Un Voronoi exacto requiere estructuras avanzadas difíciles de implementar en un proyecto de tiempo limitado. Por ello se usa una **aproximación por muestreo de malla (grid sampling)**:

1. Se calcula un bounding box alrededor de las centrales.
2. Se genera un grid regular de puntos.
3. Cada punto del grid se asigna a la central más cercana.
4. Cada región se convierte en un polígono mediante Convex Hull.

Esta aproximación está respaldada por los contenidos del curso, especialmente:

- 4.1 Proximidad e intersección
- 4.3 Búsqueda geométrica
- 4.6 Algoritmos aleatorizados

---

### 2.3 Convex Hull (Monotone Chain)

Para cada región de Voronoi aproximada, se genera un polígono que encierra a los puntos usando el algoritmo de **Monotone Chain**, cuya complejidad es:

$$
O(n \log n)
$$

donde (n) es el número de puntos de la región.

---

### 2.4 Visualización

La visualización se genera usando `matplotlib`, con:

- puntos del grid coloreados por región,
- polígonos obtenidos del Convex Hull,
- centrales resaltadas (A, B, C...),

---

## 3. Flujo del algoritmo

### Entrada

- Lista de centrales: `[(x1, y1), (x2, y2), ...]`
- Lista de casas nuevas: `[(a1, b1), (a2, b2), ...]`

### Proceso

1. **Asignación de proximidad**

   - Para cada casa, se calcula la distancia a cada central.
   - La casa se asigna a la central más cercana.

2. **Generación de grid**

   - Se obtiene un bounding box.
   - Se crea un grid uniforme con un paso configurable.

3. **Asignación de grid a regiones**

   - Cada punto del grid se asigna a la central más cercana.
   - Se obtienen regiones discretas.

4. **Obtención de polígonos**

   - A cada región se le calcula su Convex Hull.

5. **Visualización**

   - Se grafican regiones, polígonos y centrales.

### Salida

1. Lista de asignaciones de casa → central.
2. Lista de polígonos para cada central.
3. Visualización completa.

---

## 4. Complejidad computacional

Sea:

- ( C ) = número de centrales
- ( H ) = número de casas
- ( G ) = número de puntos en el grid

### 4.1 Selección de central más cercana

Para cada casa:

$$
O(C)
$$

Total:

$$
O(H \cdot C)
$$

---

### 4.2 Asignación de grid

Para cada punto del grid:

$$
O(C)
$$

Total:

$$
O(G \cdot C)
$$

---

### 4.3 Cálculo del Convex Hull

Para una región con (P_i) puntos:

$$
O(P_i \log P_i)
$$

En el peor caso:

$$
O(G \log G)
$$

---

### Complejidad total

Aproximación:

$$
O(H \cdot C + G \cdot C + G \log G)
$$

Es eficiente y totalmente aceptable para un Voronoi aproximado.

---

## 5. Justificación académica

El problema aplica los siguientes conceptos :

- Proximidad entre puntos
- Algoritmos geométricos clásicos
- Convex Hull
- Búsqueda geométrica
- Aproximación a Voronoi
- Representación visual

La solución es modular, clara y se integra naturalmente al proyecto completo.

---

## 6. Ejemplo visual generado

La ejecución produce:

- Regiones bien separadas
- Polígonos convexos
- Centrales claramente identificadas
- Zonas de influencia diferenciadas
