# Ordenamiento externo: Polyphase Sort
import random

# Generar lista aleatoria (simula los registros en disco)
n = 25
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

# Polyphase Sort (simulación en memoria) - inline, sin funciones
# Idea (simulada): crear runs iniciales, distribuirlos en 3 'cintas' (listas) según
# aproximación de Fibonacci y luego realizar fusiones repetidas donde dos cintas
# actúan como fuentes y la tercera como destino. Esta es una simplificación didáctica
# del algoritmo polyphase usado en ordenamiento externo real.

# 1) Crear runs iniciales (ordenar bloques pequeños)
run_size = 3
runs = []
for i in range(0, n, run_size):
    run = arr[i:i + run_size]
    run.sort()
    runs.append(run)

print("\nRuns iniciales (ordenados):", runs)

# 2) Obtener una distribución inicial aproximada usando Fibonacci
fib = [1, 1]
while fib[-1] + fib[-2] < len(runs):
    fib.append(fib[-1] + fib[-2])

# fib[-1] y fib[-2] son los dos últimos números de Fibonacci que usaremos
f1 = fib[-2]
f2 = fib[-1]

# Distribuir runs en 3 "tapes" (listas de runs). 
# Asignamos f1 runs a tape0, f2 runs a tape1, el resto (si hay) a tape2.
tapes = [[], [], []]
idx = 0
for _ in range(min(f1, len(runs) - idx)):
    tapes[0].append(runs[idx]); idx += 1
for _ in range(min(f2, len(runs) - idx)):
    tapes[1].append(runs[idx]); idx += 1
while idx < len(runs):
    tapes[2].append(runs[idx]); idx += 1

print("\nDistribución inicial en cintas (runs por cinta):")
for i, t in enumerate(tapes):
    print(f"  cinta {i}: {len(t)} runs")

pass_num = 1
# 3) Ciclo de fusiones: mientras haya más de un run total
while sum(len(t) for t in tapes) > 1:
    print(f"\nPasada {pass_num}: estado runs por cinta -> {[len(t) for t in tapes]}")
    # elegir cinta destino: preferir la cinta vacía; si no hay, elegir la de menor runs
    dest = None
    for i in range(3):
        if len(tapes[i]) == 0:
            dest = i
            break
    if dest is None:
        dest = min(range(3), key=lambda x: len(tapes[x]))

    # fuentes = las otras dos cintas
    srcs = [i for i in range(3) if i != dest]

    # si ambas fuentes tienen runs, fusionar la primera run de cada una
    if len(tapes[srcs[0]]) > 0 and len(tapes[srcs[1]]) > 0:
        left = tapes[srcs[0]].pop(0)
        right = tapes[srcs[1]].pop(0)
        # fusión típica de dos runs ordenados
        l = r = 0
        merged = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged.append(left[l]); l += 1
            else:
                merged.append(right[r]); r += 1
        if l < len(left):
            merged.extend(left[l:])
        if r < len(right):
            merged.extend(right[r:])
        tapes[dest].append(merged)
        print(f"  Merge runs de cintas {srcs[0]} y {srcs[1]} -> cinta {dest} (tamaño run {len(merged)})")
    else:
        # si solo una fuente tiene runs, mover su primer run al destino (simula run 'pasante' en polyphase)
        non_empty = srcs[0] if len(tapes[srcs[0]]) > 0 else srcs[1]
        moved = tapes[non_empty].pop(0)
        tapes[dest].append(moved)
        print(f"  Mover run de cinta {non_empty} a cinta {dest} (tamaño run {len(moved)})")

    pass_num += 1
    estado = [x for t in tapes for run in t for x in run]
    print("  Estado concatenado (parcial):", estado)

# Resultado final: la cinta que contiene el único run restante
final_run = []
for t in tapes:
    if len(t) == 1:
        final_run = t[0]
        break

print("\nOrdenado (resultado final de Polyphase Sort simulado):", final_run)

# Notas:
# - Esta implementación es una simplificación para ilustrar el mecanismo de polyphase.
# - En un entorno externo real se utilizan 'tapes' o ficheros, y la distribución inicial
#   de runs sigue reglas de Fibonacci y uso de runs ficticios (dummies) para equilibrar.
# - Polyphase reduce el número de pasadas de I/O comparado con merges balanceados en ciertos casos.
# ...existing code...