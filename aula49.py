# for in lista
lista = ['Manuel', 'Figueiredo', 2026]
lista.append('Audrey')
lista.append('Adameire')

for letra in 'ABC':
    print(letra)
    
    # lista iteravel
    for nome in lista:
        print(nome)
    
    indice = 0
    # imprimir com indices
    # exibir o tamanho da lista
    indices = range(len(lista))
    
    for indice in indices:
        print(indice, lista[indice])
    