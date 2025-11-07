# Ordenamiento externo: Ba|lanced Multiway Merging
import random

# Generar lista aleatoria (simula los registros en disco)
n = 20
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

# Balanced Multiway Merging (mezcla multiway balanceada) - inline, sin funciones
# Idea: crear runs iniciales (cada run es un bloque ordenado), luego fusionar k runs a la vez
# hasta que quede un único run ordenado. Simulación en memoria de un ordenamiento externo.

# construir runs iniciales (tamaño fijo)
run_size = 4
runs = []
for i in range(0, n, run_size):
    run = arr[i:i + run_size]
    run.sort()          # cada bloque inicial se ordena (simula runs en disco)
    runs.append(run)

print("Runs iniciales:", runs)

k = 3  # número de vías (k-way merge)
pass_num = 1

# Mientras haya más de un run, fusionar por grupos de k runs
while len(runs) > 1:
    print(f"\nPasada {pass_num}: fusionando por bloques de {k} runs (total runs: {len(runs)})")
    new_runs = []
    i = 0
    while i < len(runs):
        group = runs[i:i + k]  # tomar hasta k runs
        # fusión k-way simple: mantener un índice por run y escoger el mínimo entre las cabezas
        indices = [0] * len(group)
        merged = []
        while True:
            min_val = None
            min_idx = -1
            for idx in range(len(group)):
                if indices[idx] < len(group[idx]):
                    val = group[idx][indices[idx]]
                    if min_val is None or val < min_val:
                        min_val = val
                        min_idx = idx
            if min_idx == -1:
                # todas las runs vacías
                break
            merged.append(min_val)
            indices[min_idx] += 1
        new_runs.append(merged)
        print(f"  Merge runs {i}..{i+len(group)-1} -> tamaño {len(merged)}")
        i += k
    runs = new_runs
    pass_num += 1
    # mostrar estado parcial concatenado
    estado = [x for run in runs for x in run]
    print("Estado concatenado:", estado)

# Resultado final
sorted_arr = runs[0] if runs else []
print("\nOrdenado (resultado final de Balanced Multiway Merging):", sorted_arr)

# Notas:
# - Simulación en memoria de mezcla multiway balanceada (k-way).
# - En un sistema externo real, cada run residiría en un archivo/tape y
#   el merge k-way se haría leyendo bloques desde múltiples fuentes.
# - Complejidad: cada pasada realiza O(n) comparaciones (selección lineal entre k cabezas),
#   y el número de pasadas ≈ log_k(#runs_iniciales).
# ...existing code...