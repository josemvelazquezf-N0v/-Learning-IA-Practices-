#
# Construye una sublista ordenada al frente del arreglo. Para cada elemento (clave) toma su valor y lo "inserta" en la posición correcta dentro de la sublista ya ordenada moviendo hacia la derecha los elementos mayores.
# Propiedades:
# In-place: no usa estructura adicional (O(1) espacio extra).
# Estable: conserva el orden relativo de elementos iguales.
# Complejidad: peor y promedio O(n^2), mejor caso O(n) (si ya está ordenado).
#

import random

# generar lista aleatoria
n = 10
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

# Ordenamiento por inserción 

comparisons = 0
shifts = 0

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0:
        comparisons += 1
        if arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        else:
            break
    arr[j + 1] = key
    shifts += 1

print("Ordenado:", arr)
print("Comparaciones:", comparisons, "Movimientos (shifts):", shifts)
