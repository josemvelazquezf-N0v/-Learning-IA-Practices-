# kruskal_almacen.py
# Ejemplo didáctico del Árbol Parcial Mínimo usando el algoritmo de Kruskal.
# Grafo con nombres de nodos tipo almacén.

# ------------------------------------------------------------
# GRAFO PARA KRUSKAL
# ------------------------------------------------------------
#
# Imagina otro almacén con esta forma:
#
#   [Recepción] --1-- [Pasillo_A] --4-- [Pasillo_B]
#        |              |   \           |
#        3              2    3          5
#        |              |     \         |
#   [Estante_1] --4-- [Estante_2] --1-- [Oficina_Admin]
#
# Representamos el grafo como lista de aristas:
#   edges = [(peso, u, v), ...]


nodes = [
    "Recepción",
    "Pasillo_A",
    "Pasillo_B",
    "Estante_1",
    "Estante_2",
    "Oficina_Admin",
]

edges = [
    (1, "Recepción", "Pasillo_A"),
    (4, "Pasillo_A", "Pasillo_B"),
    (3, "Recepción", "Estante_1"),
    (2, "Pasillo_A", "Estante_2"),
    (3, "Pasillo_A", "Estante_2"),  # arista redundante a propósito
    (5, "Pasillo_B", "Oficina_Admin"),
    (4, "Estante_1", "Estante_2"),
    (1, "Estante_2", "Oficina_Admin"),
]


# ------------------------------------------------------------
# Estructura Union-Find (Disjoint Set Union) para Kruskal
# ------------------------------------------------------------

class UnionFind:
    def __init__(self, elements):
        # Cada nodo empieza siendo su propio padre (cada uno es su propio conjunto)
        self.parent = {e: e for e in elements}
        self.rank = {e: 0 for e in elements}  # ayuda a mantener el árbol "plano"

    def find(self, x):
        # Búsqueda con compresión de caminos
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        # Une los conjuntos que contienen a y b
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False  # ya están en el mismo conjunto, formarían ciclo

        # Unión por rango
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


def kruskal_mst(nodes, edges):
    """
    Implementación didáctica del algoritmo de Kruskal.
    - nodes: lista de nodos
    - edges: lista de tuplas (peso, u, v)

    Imprime paso a paso cómo se construye el MST.
    Devuelve:
        mst_edges: lista de aristas del MST (u, v, peso)
        total_cost: suma de los pesos del MST
    """
    print("\n" + "=" * 70)
    print("   DEMOSTRACIÓN DEL ALGORITMO DE KRUSKAL (Árbol Parcial Mínimo)")
    print("=" * 70)
    print("Nodos del grafo:")
    print("  ", nodes)

    print("\nAristas originales (costo, origen, destino):")
    for w, u, v in edges:
        print(f"  ({w}, {u}, {v})")

    # Paso 1: ordenar todas las aristas por costo
    print("\nPASO 1: Ordenar las aristas por costo (de menor a mayor)")
    edges_sorted = sorted(edges)
    for w, u, v in edges_sorted:
        print(f"  -> ({w}, {u}, {v})")

    uf = UnionFind(nodes)
    mst_edges = []
    total_cost = 0
    step = 2

    # Paso 2: recorrer las aristas en orden, añadiéndolas si no forman ciclo
    for w, u, v in edges_sorted:
        print("\n" + "-" * 70)
        print(f"PASO {step}: Considerar la arista ({u} - {v}) con costo {w}")
        step += 1

        root_u = uf.find(u)
        root_v = uf.find(v)
        print(f"  -> Representante (conjunto) de '{u}': {root_u}")
        print(f"  -> Representante (conjunto) de '{v}': {root_v}")

        if root_u == root_v:
            print("  -> Ambos nodos ya están en el MISMO conjunto.")
            print("  -> Si añadimos esta arista, formaríamos un CICLO. Se DESCARTA.")
            continue

        print("  -> Están en conjuntos DISTINTOS. Podemos unirlos sin formar ciclo.")
        uf.union(u, v)
        mst_edges.append((u, v, w))
        total_cost += w

        print(f"  -> Arista añadida al MST: ({u} - {v}) con costo {w}")
        print(f"  -> Costo acumulado del MST: {total_cost}")
        print(f"  -> Estado actual de los padres (Union-Find):")
        print(f"     {uf.parent}")

    print("\n" + "=" * 70)
    print("                RESULTADO FINAL (KRUSKAL)")
    print("=" * 70)
    print("Aristas del Árbol Parcial Mínimo (MST):")
    for (u, v, w) in mst_edges:
        print(f"  {u} - {v}  (costo = {w})")
    print(f"Costo total del MST: {total_cost}\n")

    return mst_edges, total_cost


if __name__ == "__main__":
    kruskal_mst(nodes, edges)
