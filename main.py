from algorithms.problema1 import resolver_problema1
from algorithms.problema2 import resolver_problema2
from algorithms.problema3 import resolver_problema3
from algorithms.problema4 import resolver_problema4
from utils.io_utils import leer_centrales_y_casas


# ============================================================
# Función auxiliar para leer datos desde terminal
# ============================================================

def leer_centrales_y_casas():
    """
    Lee las coordenadas de centrales y nuevas casas desde input().
    Formato:
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


# Menu principal
def menu():
    while True:
        print("\n--- Act. Integradora TC2038 ---")
        print("1. Problema 1")
        print("2. Problema 2")
        print("3. Problema 3")
        print("4. Problema 4")
        print("0. Salir")

        try:
            op = int(input("Seleccione opción: "))
        except:
            print("Opción inválida")
            continue

        if op == 0:
            print("Saliendo del programa...")
            break

        elif op == 1:
            print("\n--- Ejecución del Problema 1 ---")
            resolver_problema1()  

        elif op == 2:
            print("\n--- Ejecución del Problema 2 ---")
            resolver_problema2()  

        elif op == 3:
            print("\n--- Ejecución del Problema 3 ---")
            resolver_problema3()  

        elif op == 4:
            print("\n--- Ejecución del Problema 4 ---")
            centrales, casas = leer_centrales_y_casas()
            resultados, poligonos = resolver_problema4(centrales, casas)
            print("\nRESULTADOS:")
            for r in resultados:
                print(r)
            print("\nPOLÍGONOS:")
            for i, p in enumerate(poligonos):
                print(f"Central {i}: {p}")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
