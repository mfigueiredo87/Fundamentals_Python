# aula sobre enumerate para enumerar valores iteraveis

lista = ['Manuel', 'Armando', 'Engenheiro', 'Empresario', 'Programador']
lista.append('Cibersegurança')

lista_enumerada = enumerate(lista)
print(lista_enumerada)
print(next(lista_enumerada))

# converter o enumerate para uma lista
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)

for item in lista_enumerada:
    print(item)
# para enumerar a partir de um numero diferente do 0, basta passar o segundo parametro
lista_enumerada = enumerate(lista, start=1) 
print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

