# operadores in e not in
frase = 'O rato roeu a roupa do rei de Roma'

print('roeu' in frase)        # True
print('banana' in frase)      # False
print(10 * '-')
print(frase[10])  # True
print('Rato' in frase)        # False (case sensitive)
# outro exemplo
nome = input('Digite seu nome:')
encontrar = input('O que deseja encontrar no seu nome? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    