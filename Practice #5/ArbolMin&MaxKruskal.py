# kruskal_random_almacen.py
# Grafo aleatorio (8 nodos), pesos aleatorios, MST con Kruskal,
# impresión paso a paso con delay y exportación a README en formato Mermaid.

import random
import time

STEP_DELAY = 0.4  # segundos entre pasos, ajústalo a tu gusto


# ------------------------------------------------------------
# Generación de grafo aleatorio CONECTADO (para Kruskal)
# ------------------------------------------------------------
def generate_random_graph_kruskal(num_nodes=8, min_weight=1, max_weight=20):
    """
    Genera un grafo NO dirigido, CONECTADO, con:
      - num_nodes nodos
      - pesos aleatorios entre min_weight y max_weight

    Devuelve:
        nodes: lista de nombres de nodos
        edges: lista de aristas (peso, u, v)
    """

    # Nombres tipo almacén
    base_names = [
        "Entrada",
        "Pasillo_1",
        "Pasillo_2",
        "Estante_A",
        "Estante_B",
        "Estante_C",
        "Zona_Carga",
        "Zona_Embarque",
    ]

    if num_nodes <= len(base_names):
        nodes = base_names[:num_nodes]
    else:
        nodes = base_names + [f"Nodo_{i}" for i in range(num_nodes - len(base_names))]

    edges = []
    existing_edges = set()  # para evitar duplicados (u-v y v-u)

    # 1) Generar un árbol base (spanning tree) para asegurar conectividad
    order = nodes[:]
    random.shuffle(order)

    for i in range(1, len(order)):
        u = order[i]
        v = random.choice(order[:i])  # conectar con algún nodo ya conectado
        w = random.randint(min_weight, max_weight)

        key = frozenset({u, v})
        if key not in existing_edges:
            existing_edges.add(key)
            edges.append((w, u, v))

    # 2) Agregar aristas extra aleatorias para que no sea solo árbol
    density = 0.30  # probabilidad de arista extra entre cada par posible
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            key = frozenset({u, v})
            if key in existing_edges:
                continue
            if random.random() < density:
                w = random.randint(min_weight, max_weight)
                existing_edges.add(key)
                edges.append((w, u, v))

    return nodes, edges


# ------------------------------------------------------------
# Union-Find (Disjoint Set Union) para Kruskal
# ------------------------------------------------------------
class UnionFind:
    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}

    def find(self, x):
        # Búsqueda con compresión de caminos
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        # Une los conjuntos de a y b, si son distintos
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False  # formarían ciclo

        # Unión por rango
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


# ------------------------------------------------------------
# Algoritmo de Kruskal (paso a paso)
# ------------------------------------------------------------
def kruskal_mst(nodes, edges):
    """
    Implementación didáctica de Kruskal.

    nodes: lista de nodos
    edges: lista de aristas (peso, u, v)

    Devuelve:
        mst_edges: lista de aristas del MST [(u, v, w), ...]
        total_cost: costo total del MST
    """

    print("=" * 60)
    print("     GRAFO ALEATORIO PARA KRUSKAL (8 nodos)")
    print("=" * 60)

    print("\nNodos:")
    print("  ", ", ".join(nodes))

    print("\nAristas generadas (costo, origen, destino):\n")
    for w, u, v in edges:
        print(f"  ({w}, {u}, {v})")

    time.sleep(STEP_DELAY)

    # Ordenar aristas por peso
    print("\n--- Ordenando aristas por costo (ascendente) ---")
    edges_sorted = sorted(edges)
    for w, u, v in edges_sorted:
        print(f"  ({w}, {u}, {v})")
    time.sleep(STEP_DELAY)

    uf = UnionFind(nodes)
    mst_edges = []
    total_cost = 0
    step = 1

    # Recorrer aristas en orden
    for w, u, v in edges_sorted:
        print(f"\nPaso {step}: considerar {u} - {v} (costo {w})")
        step += 1
        time.sleep(STEP_DELAY / 2)

        ru = uf.find(u)
        rv = uf.find(v)
        print(f"  conjuntos: {u}->{ru}, {v}->{rv}")

        if ru == rv:
            print("  ya están en el mismo conjunto, forma ciclo -> se descarta")
            time.sleep(STEP_DELAY)
            continue

        print("  están en conjuntos distintos -> se añade al MST")
        uf.union(u, v)
        mst_edges.append((u, v, w))
        total_cost += w
        print("  costo acumulado:", total_cost)
        print("  aristas en MST hasta ahora:")
        for (uu, vv, ww) in mst_edges:
            print(f"    {uu} - {vv} (costo {ww})")

        time.sleep(STEP_DELAY)

    print("\n" + "=" * 60)
    print("          RESULTADO FINAL DEL MST (KRUSKAL)")
    print("=" * 60)
    for u, v, w in mst_edges:
        print(f"  {u} - {v}  (costo {w})")
    print("Costo total:", total_cost)

    return mst_edges, total_cost


# ------------------------------------------------------------
# Actualizar README 
# ------------------------------------------------------------
def update_readme_with_graphs_kruskal(nodes, edges, mst_edges, readme="README.md"):
    
    FULL_BEGIN = "<!-- BEGIN_GRAPH_FULL_KRUSKAL -->"
    FULL_END = "<!-- END_GRAPH_FULL_KRUSKAL -->"

    MST_BEGIN = "<!-- BEGIN_GRAPH_MST_KRUSKAL -->"
    MST_END = "<!-- END_GRAPH_MST_KRUSKAL -->"

    with open(readme, "r", encoding="utf-8") as f:
        content = f.read()

    # Comprobar que existan los marcadores
    for tag in (FULL_BEGIN, FULL_END, MST_BEGIN, MST_END):
        if tag not in content:
            print(f"ERROR: No se encontró el marcador {tag} en {readme}.")
            return

    # Construir bloque Mermaid del grafo completo
    full_graph_block = [FULL_BEGIN, "```mermaid", "graph LR"]
    # edges ya son únicas, no hace falta filtrar duplicados
    for w, u, v in edges:
        full_graph_block.append(f"  {u} -- {w} --> {v}")
    full_graph_block.append("```")
    full_graph_block.append(FULL_END)
    full_graph_block_str = "\n".join(full_graph_block)

    # Bloque Mermaid del MST
    mst_block = [MST_BEGIN, "```mermaid", "graph LR"]
    for u, v, w in mst_edges:
        mst_block.append(f"  {u} -- {w} --> {v}")
    mst_block.append("```")
    mst_block.append(MST_END)
    mst_block_str = "\n".join(mst_block)

    # Función interna para reemplazar secciones
    def replace_section(text, begin, end, new_block):
        start_i = text.index(begin)
        end_i = text.index(end) + len(end)
        before = text[:start_i].rstrip() + "\n\n"
        after = text[end_i:].lstrip()
        return before + new_block + "\n\n" + after

    content = replace_section(content, FULL_BEGIN, FULL_END, full_graph_block_str)
    content = replace_section(content, MST_BEGIN, MST_END, mst_block_str)

    with open(readme, "w", encoding="utf-8") as f:
        f.write(content)

    print("\nREADME.md actualizado con grafo completo y MST de Kruskal.")


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
if __name__ == "__main__":
    nodes, edges = generate_random_graph_kruskal()
    mst_edges, total_cost = kruskal_mst(nodes, edges)

    # Actualizar README con la versión visual en Mermaid
    update_readme_with_graphs_kruskal(nodes, edges, mst_edges, readme="README.md")
