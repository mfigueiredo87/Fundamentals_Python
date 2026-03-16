"""
documentacao do python: https://docs.python.org/pt-br/3/library/stdtypes.html

"""
# tipos imutaveis 
# string, int, float, bool, tuple
string = 'Olá, manuel Armando!'
outra_variavel = string

print('Carater na posicao 5:',string[5]) # acessar o caractere na posição 3 da string
print(outra_variavel)
# se quiser substituir o valor da posicao 6 da string, não é possível, pois a string é imutável
# string[6] = 'M' # isso vai gerar um erro, pois a string é imutável
# para substituir o valor da posicao 6 da string, é necessário criar uma nova string
# string[6] = 'T' # isso vai gerar um erro, pois a string é imutável
nova_string = f'{string[:5] + 'M' + string[6:]}' # isso vai criar uma nova string com o valor da posicao 6 substituido por 'T'

print(nova_string)  
# executando acoes dos objectos 
print(string.upper()) # isso vai imprimir a string em maiusculo
print(string.lower()) # isso vai imprimir a string em minusculo
print(string.replace('manuel', 'maria')) # isso vai substituir a palavra 'manuel' por 'maria' na string
print(string.split()) # isso vai dividir a string em uma lista de palavras
print(string.split(', ')) # isso vai dividir a string em uma lista de palavras, usando a virgula como separador
print(string.split('a')) # isso vai dividir a string em uma lista de palavras, usando
# a letra 'a' como separador
print(string.split('l')) # isso vai dividir a string em uma lista de palavras, usando
print(string.capitalize()) # isso vai imprimir a string com a primeira letra maiuscula e as outras minusculas
print(string.title()) # isso vai imprimir a string com a primeira letra de cada palavra maius
print(string.count('a')) # isso vai contar quantas vezes a letra 'a' aparece na string
print(string.count('l')) # isso vai contar quantas vezes a letra 'l' aparece
print(string.zfill(20)) # isso vai preencher a string com zeros a esquerda, até que a string tenha 20 caracteres
print(string.center(30, '-')) # isso vai centralizar a string em um campo de 30 caracteres, preenchendo os espaços com '-'
print(string.ljust(30, '-')) # isso vai alinhar a string a esquerda em um campo de 30 caracteres, preenchendo os espaços com '-'
print(string.rjust(30, '-')) # isso vai alinhar a string a direita em um campo de 30 caracteres, preenchendo os espaços com '-'