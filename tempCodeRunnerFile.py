
    resolver_problema1(str(ruta))


def correr_problema2() -> None:
    print("\n--- Problema 2: (a definir por el equipo) ---")
    default_path = ruta_por_defecto_problema2()
    ruta = input(
        f"Ruta del archivo de entrada (Enter para usar {default_path}): "
    ).strip()

    if not ruta:
        ruta = default_path

    resolver_problema2(str(ruta))


def correr_problema3() -> None:
    print("\n--- Problema 3: Ruta mínima tipo TSP ---")
    default_path = ruta_por_defecto_problema3()
    ruta = input(
        f"Ruta del archivo de entrada (Enter para usar {default_path}): "
    ).strip()

    if not ruta:
        ruta = default_path

    resolver_problema3(str(ruta))
