# Natural Merging
import random

# Generar lista aleatoria (simula los registros en disco)
n = 20
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

# Natural merging (mezcla natural) - inline, sin funciones
# Idea: detectar runs crecientes ya presentes en los datos y fusionar runs adyacentes
# hasta obtener un único run ordenado. Simulación en memoria de un algoritmo de ordenación externo.

# Detectar runs naturales (subsecuencias no decrecientes)
runs = []
i = 0
while i < n:
    run = [arr[i]]
    i += 1
    while i < n and arr[i - 1] <= arr[i]:
        run.append(arr[i])
        i += 1
    runs.append(run)

print("Runs iniciales:", runs)

pass_num = 1
# Fusionar runs adyacentes hasta quedar con uno solo
while len(runs) > 1:
    print(f"\nPasada {pass_num}: fusionando {len(runs)} runs")
    new_runs = []
    k = 0
    while k < len(runs):
        if k + 1 < len(runs):
            left = runs[k]
            right = runs[k + 1]
            # merge típico de dos listas ordenadas
            l = 0
            r = 0
            merged = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            if l < len(left):
                merged.extend(left[l:])
            if r < len(right):
                merged.extend(right[r:])
            new_runs.append(merged)
            print(f"  Merge runs {k} y {k+1} -> tamaño {len(merged)}")
            k += 2
        else:
            # run sin pareja, se pasa a la siguiente fase tal cual
            new_runs.append(runs[k])
            print(f"  Run {k} sin pareja -> tamaño {len(runs[k])}")
            k += 1
    runs = new_runs
    pass_num += 1
    # mostrar estado parcial (concatenado)
    estado = [x for run in runs for x in run]
    print("Estado concatenado:", estado)

# Resultado final
sorted_arr = runs[0] if runs else []
print("\nOrdenado (resultado final de Natural Merging):", sorted_arr)

# Notas:
# - Natural merging aprovecha runs ya existentes en los datos, pudiendo reducir el número de pasadas.
# - Complejidad promedio O(n log n) en número de comparaciones/lecturas, pero depende de la
#   estructura de runs iniciales.
# - En un entorno externo real, cada run y cada fusión se haría leyendo/escribiendo bloques desde disco.
# ...existing code...