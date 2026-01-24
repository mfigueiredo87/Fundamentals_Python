# formatacao de strings com fstrings (f'')
variavel = 'ABC'
print(f'Valor da variável: {variavel}')

#  acrscentando expressões
nome = 'João'
preco = 19.99
dados = f'{nome}, o preço é KZ {preco:,.2f}'
print(dados)

# acrescentado valores a equerda e direita
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
saida = f'O {nome} tem {idade} anos'
print(saida)
# alinhamento: < esquerda, > direita, ^ centro

resultado = f'O {nome:<10} tem {idade:>3} anos'
print(resultado)

# exibindo o hexadecimal de um número
num = 1500
hexadecimal = f'O hexadecimal de {num} é {num:08X}'
print(hexadecimal)

# usando .2f para formatar números float
preco = 1999.90
valor = f'O preço do produto é KZ {preco:,.2f}'