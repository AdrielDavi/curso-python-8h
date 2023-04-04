# criando uma lista com os números de 0 a 100
numeros = list(range(101))

# marcando o número 0 e 1 como compostos (não primos)
numeros[0] = numeros[1] = None

# percorrendo os números de 2 a 10 (raiz de 100)
for i in range(2, 11):
    # se o número i não foi marcado como composto, ele é primo
    if numeros[i]:
        # marcando todos os múltiplos de i como compostos
        for j in range(i*i, 101, i):
            numeros[j] = None

# imprimindo os números primos
print("Números primos de 0 a 100:")
for num in numeros:
    if num:
        print(num)
