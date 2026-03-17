# iterando strings com while
# frase = 'Python é uma linguagem de programação '\
        # 'multiparadigma. ' \
        # 'Python foi criado por Guido van Rossum e lançado em 1991.'

# frase = frase.upper()
# frase = frase.replace(' ', 'x')
frase = 'O Senhor é meu bom pastor e nada me faltará. Salmos 23:1'

# saber o tamanho da string
tamanho_frase = len(frase)
contador = 0
while contador < tamanho_frase:
    letra = frase[contador]
    print(letra, end=' ')
    contador += 1
print('\n A frase tem ', tamanho_frase, ' caracteres')

# contar qual letra aparece mais vezes
i = 0
qtd_letras_mais_vezes = 0
letra_mais_vezes = ''
while i <len(frase):
    letra = frase[i]
    
    # ignorar os espaços
    if letra == ' ':
        i += 1
        continue
    
    total_vezes = frase.count(letra)
   
    if qtd_letras_mais_vezes < total_vezes:
        qtd_letras_mais_vezes = total_vezes
        letra_mais_vezes = letra
    
    i += 1
    
print(f'A letra mais frequente no texto é: "{letra_mais_vezes}"')
    # print(f'A letra {letra}, aparece {total_vezes} vezes')  
print(
    'A letra que aparece mais vezes foi ' 
    f'"_ {letra_mais_vezes} _", cerca de ' 
    f' {qtd_letras_mais_vezes} vezes'
    )   
            
    # print(f'A letra {letra}, aparece {total_vezes} vezes')
    # i += 1
    # essa solução é ineficiente, pois conta a letra várias vezes, o ideal seria criar uma lista para armazenar as letras já contadas e não contar novamente.
    