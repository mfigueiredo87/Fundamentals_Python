# alterando uma lsita com indices, del, append, insert, pop, clear

lista = [1, 2, 3, 4, 5]
lista[0] = 10  # mudando o valor do indice 0 da lista
print(lista)  # [10, 2, 3, 4, 5]

print(lista[2])

del lista[1]  # deletando o indice 1 da lista
print(f'Foi deletado o valor {lista[1]} da lista {lista}')  # [10, 3, 4, 5]

# adicionando um valor no final da lista
lista.append(6)
print(lista)  # [10, 3, 4, 5, 6]
print('Foi adicionado o valor 6 no final da lista', lista)

# adicionando um valor em um indice especifico da lista
lista.insert(1, 20)  # adicionando o valor 20 no indice 1 da lista
print(lista)  # [10, 20, 3, 4, 5, 6]
print('Foi adicionado o valor 20 no indice 1 da lista', lista)

# removendo o ultimo valor da lista
removido = lista.pop()  # removendo o ultimo valor da lista
print(lista)  # [10, 20, 3, 4, 5]
print(f'Foi removido o valor {removido} da lista', lista)

# adicionar uma string no final da lista
string = lista.append('Manuel')
print(lista)  # [10, 20, 3, 4, 5, 'Python']
print(f'Foi adicionado o valor {string} no final da lista', lista)

# limpando a lista
limpar = lista.clear()  # limpando a lista
print(lista)  # []

if lista == []:
    print('A lista está vazia')
    
print(f'Foi limpada a lista, agora ela é {lista}')

# concatenar a lista
lista1 = [1, 2, 3]
lista2 = [46, 5, 6]
lista3 = lista1 + lista2  # concatenando as listas
print(f'Foi concatenada a lista1 {lista1} com a lista2 {lista2}, resultando em {lista3}')

# repetir a lista
lista4 = lista1 * 3  # repetindo a lista 3 vezes
print(f'Foi repetida a lista1 {lista1} 3 vezes, resultando em {lista4}')

# extendendo a lista
lista1.extend(lista2)  # extendendo a lista1 com a lista2
print(f'Foi extendida a lista1 {lista1} com a lista2 {lista2}, resultando em {lista1}')

# copiar o valor de listas 
lista_a = ['Manuel', 'Roberto']
lista_b = lista_a


# se quiser copiar o valor da lista_a
lista_b = lista_a.copy()

lista_a[0] = 'Mai assim fica como?'

print("Valores da lista A",lista_a)
print("Valores da lista B",lista_b)


