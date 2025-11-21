# Funciones auxiliares de entrada/salida

def leer_centrales_y_casas():
    """
    Lee las coordenadas de centrales y nuevas casas desde input().
    Formato esperado:
        Numero de centrales
        x y
        x y
        ...
        Numero de casas
        x y
        x y
        ...
    """
    N = int(input("Numero de centrales: "))
    centrales = []
    for _ in range(N):
        x, y = map(int, input("central x y: ").split())
        centrales.append((x, y))

    M = int(input("Numero de nuevas casas: "))
    casas = []
    for _ in range(M):
        x, y = map(int, input("casa x y: ").split())
        casas.append((x, y))

    return centrales, casas
