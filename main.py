from pathlib import Path

from algorithms.problema1 import resolver_problema1
from algorithms.problema2 import resolver_problema2
from algorithms.problema3 import resolver_problema3


BASE_DIR = Path(__file__).parent


def ruta_por_defecto_problema1() -> Path:
    """
    Ruta por defecto del archivo de entrada para el Problema 1.
    Ajusta el nombre del archivo si es necesario.
    """
    return BASE_DIR / "data" / "inputsProblema1" / "inputProblema1.txt"


def ruta_por_defecto_problema2() -> Path:
    """
    Ruta por defecto del archivo de entrada para el Problema 2.
    Si aún no tienes carpeta/archivo, puedes crearla después
    o simplemente ignorar el valor por defecto en la ejecución.
    """
    return BASE_DIR / "data" / "inputsProblema1" / "inputProblema1.txt"


def ruta_por_defecto_problema3() -> Path:
    """
    Ruta por defecto del archivo de entrada para el Problema 3.
    Ajusta el nombre del archivo según tu estructura real.
    """
    return BASE_DIR / "data" / "inputsProblema3" / "inputProblema3.txt"


def correr_problema1() -> None:
    print("\n--- Problema 1: Cableado óptimo de colonias (MST) ---")
    default_path = ruta_por_defecto_problema1()
    ruta = input(
        f"Ruta del archivo de entrada (Enter para usar {default_path}): "
    ).strip()

    if not ruta:
        ruta = default_path

    resolver_problema1(str(ruta))
    x = input('\n\n')
    print('\n' * 15)


def correr_problema2() -> None:
    print("\n--- Problema 2: (a definir por el equipo) ---")
    default_path = ruta_por_defecto_problema2()
    ruta = input(
        f"Ruta del archivo de entrada (Enter para usar {default_path}): "
    ).strip()

    if not ruta:
        ruta = default_path

    resolver_problema2(str(ruta))
    x = input('\n\n')
    print('\n' * 15)


def correr_problema3() -> None:
    print("\n--- Problema 3: Ruta mínima tipo TSP ---")
    default_path = ruta_por_defecto_problema3()
    ruta = input(
        f"Ruta del archivo de entrada (Enter para usar {default_path}): "
    ).strip()

    if not ruta:
        ruta = default_path

    resolver_problema3(str(ruta))
    x = input('\n\n')
    print('\n' * 15)



def mostrar_menu() -> None:
    print("\n--- Act. Integradora TC2038 ---")
    print("1. Ejecutar Problema 1 (MST)")
    print("2. Ejecutar Problema 2")
    print("3. Ejecutar Problema 3 (TSP)")
    print("0. Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            correr_problema1()
        elif opcion == "2":
            correr_problema2()
        elif opcion == "3":
            correr_problema3()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
