def ordenacao(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def entradas():
    lista = []
    for i in range(3):
        while True:
            try:
                n = int(input("Insira um número inteiro: "))
                lista.append(n)
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
    return lista





retorno_entradas = entradas()

retorno_ordenacao = ordenacao(retorno_entradas)

print("Saídas ordenadas:")
for n in retorno_entradas:
    print (n, end=" ")