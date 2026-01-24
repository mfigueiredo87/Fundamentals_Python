#  interpolacao de strings com o operador %
nome = 'João'
preco = 19.99
variavel = '%s, o preço é KZ %.2f' % (nome, preco)
print(variavel)

# outro exemplo
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
variavel = 'O %s tem %d anos' % (nome, idade)
print(variavel)

# exibindo hexadecimal
numero = input('Digite um número inteiro: ')
numero = int(numero)
print('O número %d em hexadecimal é %04x' % (numero, numero))