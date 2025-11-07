# Ordenamiento por selección
import random

# Generar lista aleatoria (simula los datos a ordenar)
n = 10
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

# Selection Sort (ordenamiento por selección) - inline, sin funciones
comparisons = 0
swaps = 0

for i in range(len(arr) - 1):
    # asumir que el mínimo está en la posición i
    min_idx = i
    # buscar el mínimo en la porción no ordenada
    for j in range(i + 1, len(arr)):
        comparisons += 1
        if arr[j] < arr[min_idx]:
            min_idx = j
    # si el mínimo no está ya en i, intercambiar
    if min_idx != i:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    # comentario: después de cada iteración, arr[0..i] está ordenado

print("Ordenado:", arr)
print("Comparaciones:", comparisons, "Intercambios:", swaps)
# ...existing code...