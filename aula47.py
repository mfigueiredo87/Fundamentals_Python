# aula de listas

string = 'ABCDE'
lista = [1, 2, 3, 4, 5]
# lista com varios tipos de dados
lista2 = [1, 'Angola', 3.14, True, [1, 2, 3]]
lista2[1] = 'Brasil'  # mudando o valor do indice 1 da lista2
print(string[0])  # A
print(lista[0])  # 1
print(lista2[0])  # 1
print(lista2[1].upper())  # Angola
print(lista2[2])  # 3.14
print(lista2[3])  # True
print(lista2[4])  # [1, 2, 3]
# checar o type de um indice na lista
print(type(lista2[0]))  # <class 'int'>
print(type(lista2[1]), type(lista2[2]), type(lista2[3]), type(lista2[4]))  # <class 'str'> <class 'float'> <class 'bool'> <class 'list'>