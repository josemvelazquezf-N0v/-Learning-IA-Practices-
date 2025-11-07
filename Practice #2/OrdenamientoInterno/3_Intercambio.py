# Ordenamiento por selección
import random

# Generar lista aleatoria (simula los datos a ordenar)
n = 10
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

# Ordenamiento por intercambio (Exchange Sort) - inline, sin funciones
# Idea: comparar cada par (i, j) con j>i y si están fuera de orden, intercambiarlos.
# Es in-place, estable solo en ciertos casos, y tiene complejidad O(n^2).
comparisons = 0
swaps = 0

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        comparisons += 1
        if arr[i] > arr[j]:
            # intercambiar elementos para colocar el menor en la posición i
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    # comentario: tras cada iteración completa de i, el elemento en arr[i] es el correcto

print("Ordenado:", arr)
print("Comparaciones:", comparisons, "Intercambios:", swaps)

# Notas:
# - Exchange sort realiza comparaciones para cada par (i,j) con j>i.
# - Peor y promedio: O(n^2) comparaciones y hasta O(n^2) intercambios.
# ...existing code...