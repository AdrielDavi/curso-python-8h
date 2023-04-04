# Criação dos conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 5, 6, 7, 8}

# União
print("União de A e B:", A.union(B))
print("União de B e C:", B.union(C))

# Interseção
print("Interseção de A e B:", A.intersection(B))
print("Interseção de B e C:", B.intersection(C))

# Diferença
print("Diferença de A e B:", A.difference(B))
print("Diferença de B e A:", B.difference(A))

# Diferença simétrica
print("Diferença simétrica de A e B:", A.symmetric_difference(B))
print("Diferença simétrica de B e C:", B.symmetric_difference(C))

# Pertinência
print("A é subconjunto de B:", A.issubset(B))
print("B é subconjunto de A:", B.issubset(A))
print("C é superconjunto de B:", C.issuperset(B))
print("B é superconjunto de C:", B.issuperset(C))

# Adição de elementos
A.add(5)
B.update({7, 8, 9})
print("A com elemento adicionado:", A)
print("B com elementos adicionados:", B)

# Remoção de elementos
C.remove(8)
B.discard(6)
print("C com elemento removido:", C)
print("B com elemento removido:", B)
