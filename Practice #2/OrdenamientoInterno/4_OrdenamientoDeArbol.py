# Ordenamiento de árbol
import random

# Generar lista aleatoria (simula los datos a ordenar)
n = 10
arr = [random.randint(0, 99) for _ in range(n)]
print("Original:", arr)

# Ordenamiento por árbol (Tree Sort) - inline, con clase Node para el BST
# Idea: insertar todos los elementos en un árbol binario de búsqueda (BST)
# y luego realizar un recorrido inorder para obtener los elementos ordenados.

comparisons = 0  # contador aproximado de comparaciones durante las inserciones

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, val):
        # usar variable global para contabilizar comparaciones realizadas
        global comparisons
        comparisons += 1  # comparar val con self.value
        if val < self.value:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

# Construir el BST con los elementos de arr
if len(arr) == 0:
    sorted_arr = []
else:
    root = Node(arr[0])
    for v in arr[1:]:
        root.insert(v)

    # recorrido inorder (izquierda, raíz, derecha) para obtener la lista ordenada
    sorted_arr = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        sorted_arr.append(node.value)
        inorder(node.right)

    inorder(root)

print("Ordenado:", sorted_arr)
print("Comparaciones (aprox. durante inserciones):", comparisons)

# Notas:
# - Tree Sort tiene promedio O(n log n) tiempo si el BST está balanceado,
#   pero en el peor caso (árbol degenerado) es O(n^2).
# - Esta implementación no balancea el árbol; para casos reales conviene usar
#   árboles balanceados (AVL, Red-Black) o estructuras como heap/merge/quick.
# ...existing code...