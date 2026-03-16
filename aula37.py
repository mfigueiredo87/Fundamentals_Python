# iteracao de string
texto = 'Python é uma linguagem de programação poderosa e versátil.'

# tamanho da string
tamanho = len(texto)
print('Tamanho da string: ',tamanho)
#indicar os indices
indice = 0
novo_texto = ''
while indice < tamanho:
    print(f'Indice: {indice} - Caracter: {texto[indice]}')
    novo_texto += texto[indice] + '*'
   
    indice += 1
print('Novo texto: ',novo_texto)

# outra forma de iterar a string
print('Outra forma de Iterar a string com while e indices:')

while indice < len(texto):
   letra = texto[indice]
   novo_texto += f'*{letra}'
   indice += 1
print('Novo texto: ',novo_texto)


