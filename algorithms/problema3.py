from collections import deque
print(">>> CARGANDO problema3.py CORRECTO <<<")


def edmonds_karp(capacidad, source, sink):
    n = len(capacidad)

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
            nodo = anterior

    return max_flow

def bfs_encontrar_camino(residual, padre, source, sink):
    n = len(residual)
    visitado = [False] * n
    visitado[source] = True

    cola = deque([(source, float("inf"))])

    while cola:
        nodo, flujo_actual = cola.popleft()

        # Recorrer vecinos siempre en orden ascendente
        for vecino in range(n):
            if not visitado[vecino] and residual[nodo][vecino] > 0:
                visitado[vecino] = True
                padre[vecino] = nodo
                nuevo_flujo = min(flujo_actual, residual[nodo][vecino])

                if vecino == sink:
                    return nuevo_flujo

                cola.append((vecino, nuevo_flujo))

    return 0


def leer_matriz_capacidades(nombre_archivo):
    capacidad = []
    with open(nombre_archivo, "r") as f:
        for linea in f:
            nums = linea.strip().split()
            if not nums:
                continue
            fila = [int(x) for x in nums]

            # Validación obligatoria
            if capacidad and len(fila) != len(capacidad[0]):
                raise ValueError(
                    f"ERROR: La matriz no es cuadrada. "
                    f"Fila con {len(fila)} columnas, debería tener {len(capacidad[0])}."
                )

            capacidad.append(fila)

    # Validación final
    if len(capacidad) != len(capacidad[0]):
        raise ValueError("La matriz NO es cuadrada.")

    return capacidad



def resolver_problema3(nombre_archivo):
    capacidad = leer_matriz_capacidades(nombre_archivo)

    n = len(capacidad)
    source = 0
    sink = n - 1

    flujo_maximo = edmonds_karp(capacidad, source, sink)

    print(f"Flujo máximo entre {chr(source+65)} y {chr(sink+65)}: {flujo_maximo}")
    return flujo_maximo
