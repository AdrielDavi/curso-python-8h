# criando uma lista com alguns elementos
minha_lista = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# adicionando um novo elemento no final da lista
minha_lista.append(11)

# imprimindo a lista atualizada
print("Lista com novo elemento adicionado:", minha_lista)

# removendo o primeiro elemento da lista
minha_lista.pop(0)

# imprimindo a lista atualizada
print("Lista com o primeiro elemento removido:", minha_lista)

# ordenando a lista em ordem crescente
minha_lista.sort()

# imprimindo a lista ordenada
print("Lista ordenada:", minha_lista)

# verificando se um elemento está presente na lista
if 5 in minha_lista:
    print("5 está na lista!")
else:
    print("5 não está na lista!")

# calculando o tamanho da lista
tamanho = len(minha_lista)

# imprimindo o tamanho da lista
print("Tamanho da lista:", tamanho)

# calculando a soma dos elementos da lista
soma = sum(minha_lista)

# imprimindo a soma dos elementos da lista
print("Soma dos elementos da lista:", soma)

# calculando a média dos elementos da lista
media = soma / tamanho

# imprimindo a média dos elementos da lista
print("Média dos elementos da lista:", media)

# invertendo a ordem dos elementos na lista
minha_lista.reverse()

# imprimindo a lista invertida
print("Lista invertida:", minha_lista)

# criando uma nova lista com os elementos pares da lista original
lista_pares = [x for x in minha_lista if x % 2 == 0]

# imprimindo a lista com os elementos pares
print("Lista com elementos pares:", lista_pares)

# criando uma nova lista com os elementos ímpares da lista original
lista_impares = [x for x in minha_lista if x % 2 != 0]

# imprimindo a lista com os elementos ímpares
print("Lista com elementos ímpares:", lista_impares)

# criando uma nova lista com os elementos elevados ao quadrado
lista_quadrados = [x**2 for x in minha_lista]

# imprimindo a lista com os elementos elevados ao quadrado
print("Lista com elementos elevados ao quadrado:", lista_quadrados)
