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
lista_enumerada = enumerate(lista, start=2) 
print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)
# desempacotando os valores do enumerate
for indice, nome in enumerate(lista):
    print(f'Indice: {indice} - Nome: {nome}')
"""    
for item in enumerate(lista):
    indice, nome = item
    print(f'Indice: {indice} - Nome: {nome}')
"""
