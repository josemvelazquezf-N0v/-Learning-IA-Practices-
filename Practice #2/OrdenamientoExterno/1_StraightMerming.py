# ...existing code...
import random

# Simulación del "Straight merging" (mezcla directa) como un ordenamiento externo
# Nota: aquí lo simulamos en memoria con listas para ilustrar el proceso.
# Idea: construir runs iniciales (tamaño 1) y luego hacer pasadas de mezcla
# donde se fusionan runs adyacentes de tamaño `run_size`, duplicando run_size en cada pasada.

# generar lista aleatoria (simula los registros en disco)
n = 20
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

run_size = 1   # tamaño inicial de los runs (1 = cada elemento es un run)
pass_num = 1

# Bucle de pasadas: mientras el tamaño de run sea menor que n
while run_size < n:
    print(f"\nPasada {pass_num}: mezcla de runs de tamaño {run_size}")
    merged = []
    i = 0
    # recorrer el arreglo en bloques de 2*run_size y fusionar cada par (left, right)
    while i < n:
        left = arr[i:i + run_size]
        right = arr[i + run_size:i + 2 * run_size]
        # fusionar left y right (merge típico)
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        # añadir residuos si algún lado queda
        if l < len(left):
            merged.extend(left[l:])
        if r < len(right):
            merged.extend(right[r:])
        i += 2 * run_size

    # Si quedan elementos (por seguridad), mantenerlos
    if len(merged) < n:
        merged.extend(arr[len(merged):])

    arr = merged  # resultado de la pasada
    print("Después de la pasada:", arr)

    run_size *= 2
    pass_num += 1

print("\nOrdenado (resultado final de straight merging):", arr)
# Propiedades:
# - Simulación en memoria de mezcla directa (two-way balanced merging).
# - Cada pasada fusiona runs adyacentes; número de pasadas ≈ log2(n).
# - Complejidad temporal: O(n log n) en esta implementación (simulación).
# - En un entorno externo real, las fusiones se harían leyendo/escribiendo en 'tapes' o ficheros.
# ...existing code...