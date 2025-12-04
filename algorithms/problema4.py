import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

# Distancia y proximidad
def distancia(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def central_mas_cercana(punto, centrales):
    min_d = float("inf")
    idx = -1
    for i, c in enumerate(centrales):
        d = distancia(punto, c)
        if d < min_d:
            min_d = d
            idx = i
    return idx, min_d



# Convex Hull
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    lower = []
    for p in pts:
        while len(lower)>=2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(pts):
        while len(upper)>=2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


# Voronoi aproximado
def bounding_box(centrales, margen=80):
    xs = [c[0] for c in centrales]
    ys = [c[1] for c in centrales]
    return min(xs)-margen, max(xs)+margen, min(ys)-margen, max(ys)+margen

def generar_grid(min_x, max_x, min_y, max_y, paso):
    pts = []
    y = min_y
    while y <= max_y:
        x = min_x
        while x <= max_x:
            pts.append((x, y))
            x += paso
        y += paso
    return pts


# Funcion principal
def resolver_problema4(centrales, nuevas_casas, paso=10):
    """
    Esta función:
        - Calcula la central más cercana para cada nueva casa
        - Genera Voronoi aproximado (grid + convex hull)
        - GRAFICA  la solución
        - Devuelve (resultados, poligonos)
    """

    # Resultados por casa
    resultados = []
    for casa in nuevas_casas:
        idx, dist = central_mas_cercana(casa, centrales)
        resultados.append({
            "casa": casa,
            "central_idx": idx,
            "central_pos": centrales[idx],
            "distancia": dist
        })

    # Voronoi aproximado
    min_x, max_x, min_y, max_y = bounding_box(centrales)
    grid = generar_grid(min_x, max_x, min_y, max_y, paso)

    regiones = [[] for _ in centrales]

    for p in grid:
        idx, _ = central_mas_cercana(p, centrales)
        regiones[idx].append(p)

    poligonos = []
    for region in regiones:
        if len(region) < 3:
            poligonos.append([])
        else:
            poligonos.append(convex_hull(region))


    # Visualizacion
    cmap = cm.get_cmap("tab20", max(20, len(centrales)))
    fallback = [(random.random(), random.random(), random.random()) for _ in centrales]

    plt.figure(figsize=(8,8))

    # Regiones
    for i, pts in enumerate(regiones):
        color = cmap(i) if i < 20 else fallback[i]
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        plt.scatter(xs, ys, s=8, color=color, alpha=0.25)

    # Polígonos
    for i, poly in enumerate(poligonos):
        if len(poly) > 2:
            color = cmap(i) if i < 20 else fallback[i]
            px = [p[0] for p in poly] + [poly[0][0]]
            py = [p[1] for p in poly] + [poly[0][1]]
            plt.plot(px, py, color=color, linewidth=2)

    # Centrales
    cx = [c[0] for c in centrales]
    cy = [c[1] for c in centrales]
    plt.scatter(cx, cy, s=200, color="yellow", edgecolor="black")

    for i, c in enumerate(centrales):
        plt.text(c[0]+5, c[1]+5, chr(65+i), fontsize=12, weight="bold")

    plt.title("Voronoi aproximado + Convex Hull (Problema 4)")
    plt.grid(True)

    plt.show(block=False)
    plt.pause(0.001)


    return resultados, poligonos
