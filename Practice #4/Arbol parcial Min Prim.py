import random
import time
from heapq import heappush, heappop

# Delay entre pasos para que se vea en "tiempo real" en la terminal
STEP_DELAY = 2  # puedes subir/bajar este valor


def generate_random_graph(num_nodes=8, min_weight=1, max_weight=20):
    """
    Genera un grafo NO dirigido, CONECTADO y aleatorio.

    - num_nodes: cantidad de nodos (usaremos 8)
    - min_weight, max_weight: rango de pesos aleatorios de las aristas

    Devuelve:
        graph: diccionario {nodo: [(vecino, peso), ...]}
        start_node: nodo desde el que empieza Prim
    """

    # Nombres "intuitivos" para 8 nodos de un almacén
    node_names = [
        "Inicio",
        "Pasillo_1",
        "Pasillo_2",
        "Estante_A",
        "Estante_B",
        "Estante_C",
        "Zona_Carga",
        "Zona_Embarque",
    ]

    # Por si algún día quieres num_nodes != 8, recortamos o repetimos nombres
    if num_nodes <= len(node_names):
        nodes = node_names[:num_nodes]
    else:
        # Si pidieras más de 8, generaría nombres extra genéricos
        nodes = node_names + [f"Nodo_{i}" for i in range(num_nodes - len(node_names))]

    graph = {node: [] for node in nodes}
    existing_edges = set()  # para no repetir aristas

    # 1) Generar un árbol aleatorio (spanning tree) para asegurar CONECTIVIDAD
    order = nodes[:]           # copia
    random.shuffle(order)      # orden aleatorio de nodos

    for i in range(1, len(order)):
        u = order[i]
        v = random.choice(order[:i])  # conecta con cualquiera previo (ya conectado)
        w = random.randint(min_weight, max_weight)

        graph[u].append((v, w))
        graph[v].append((u, w))
        existing_edges.add(frozenset({u, v}))

    # 2) Agregar algunas aristas extra al azar para que el grafo no sea solo una línea
    density = 0.30  # probabilidad de agregar arista extra entre dos nodos cualquiera
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if frozenset({u, v}) in existing_edges:
                continue  # ya existe esta arista

            if random.random() < density:
                w = random.randint(min_weight, max_weight)
                graph[u].append((v, w))
                graph[v].append((u, w))
                existing_edges.add(frozenset({u, v}))

    # Usamos como nodo inicial el "Inicio" si existe, si no el primero
    start_node = "Inicio" if "Inicio" in nodes else nodes[0]
    return graph, start_node


def prim_mst(graph, start):
    """
    Implementación sencilla del algoritmo de Prim (MST).

    - graph: {nodo: [(vecino, peso), ...]}
    - start: nodo inicial

    Muestra en la terminal:
        - El grafo generado
        - Los pasos del algoritmo de forma "cruda"
    """

    print("=" * 60)
    print("      GRAFO ALEATORIO PARA PRIM (8 nodos)")
    print("=" * 60)
    print("\nEstructura del grafo (vecino(peso)):\n")

    for node, neighbors in graph.items():
        vecinos_str = ", ".join(f"{nbr}({w})" for nbr, w in neighbors)
        print(f"  {node} Conecta con: {vecinos_str}")

    time.sleep(STEP_DELAY)

    visited = set([start])
    heap = []
    mst_edges = []
    total_cost = 0
    step = 1

    # Inicializar heap con las aristas que salen del nodo inicial
    for neighbor, w in graph[start]:
        heappush(heap, (w, start, neighbor))

    print("\nNodo inicial para Prim:", start)
    time.sleep(STEP_DELAY)

    # Bucle principal de Prim
    while heap and len(visited) < len(graph):
        w, u, v = heappop(heap)

        print(f"\nPaso {step}: saco {u} -> {v} (costo {w})")
        step += 1

        if v in visited:
            print("  ya visitado, se descarta")
            time.sleep(STEP_DELAY)
            continue

        print("  se añade al MST")
        visited.add(v)
        mst_edges.append((u, v, w))
        total_cost += w

        print("  visitados:", ", ".join(sorted(visited)))
        print("  costo acumulado:", total_cost)

        # Agregar nuevas aristas que salen de v hacia nodos NO visitados
        for neighbor, w2 in graph[v]:
            if neighbor not in visited:
                heappush(heap, (w2, v, neighbor))

        time.sleep(STEP_DELAY)

    print("\n" + "=" * 60)
    print("          RESULTADO FINAL DEL MST (PRIM)")
    print("=" * 60)
    for u, v, w in mst_edges:
        print(f"  {u} - {v}  (costo {w})")
    print("Costo total:", total_cost)


if __name__ == "__main__":
    # Generar grafo aleatorio y correr Prim
    random_graph, start_node = generate_random_graph()
    prim_mst(random_graph, start_node)
    print("Camino que pasa por todos los nodos con costo mínimo encontrado.") 
