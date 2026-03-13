# exercicios - Enunciados
"""
Questao 1: 
Fazer um programa que possa pedir ao usuario para digitar um numero inteiro, 
informe se este numero é par ou impar. Caso o usuario não digite um numero inteiro,
 informe que não é um numero inteiro.
"""
"""
entrada = input('Digite um numero: ')
# isdigit verifica se o numero introduzido eh um digito ou inteiro
if entrada.isdigit():
    # converter entrada para numero inteiro
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Ímpar'
  
    # verfica o tipo do numero digitado sabendo que por predefinicao é impar
    # a variavel par_impar ja tem o calculo certo, recebe o numero e acha o resto da divisao por 2 sendo igual a 0
    if par_impar:
        par_impar_texto = 'Par'        
        
    print(f'O numero {entrada_int} é {par_impar_texto}. ') 
else:
    print('Voce nao digitou um numero inteiro.')
"""
# outra solucao
entrada = input('Digite um numero: ')

# isdigit verifica se o valor digitado é um número inteiro
if entrada.isdigit():
    
    # converter entrada para inteiro
    entrada_int = int(entrada)

    # verificar se é par
    par_impar = entrada_int % 2 == 0

    if par_impar:
        par_impar_texto = 'Par'
        msg = 'Parabéns! Você acertou.'
    else:
        par_impar_texto = 'Ímpar'
        msg = 'Tente novamente.'

    print(f'O número {entrada_int} é {par_impar_texto}. {msg}')

else:
    print('Você não digitou um número inteiro.')

"""
try:
    entrada_int = float(entrada)
    par impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'

if par_impar:
    par_impar_texto = 'par'

    print(f'O numero {entrada} eh {par_impar_texto}')
except:
    print('Voce não digitou um numero inteiro')
"""
"""
Questao 2: 
Faça um programa que pergunte a hora ao usuaio e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noie 18-23.
"""
# solucao
hora = input('Digite uma hora valida de 0 a 23.')
nome = 'Manuel Figueiredo'
try:
    hora_in = int(hora)

    if hora_in >= 0 and hora_in <= 11:
        print(f'Bom dia, {nome}')
    elif hora_in >= 12 and hora_in <= 17:
        print(f'Boa tarde, {nome}')
    elif hora_in >= 18 and hora_in <= 23:
        print(f'Boa noite, {nome}')
    else:
        print('Hora inválida.')
except ValueError:
    print('Por favor, digite uma hora válida.')
    
"""
Questao 3:
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se iver entre 5 e 6 letras, escreva "Seu nome é 
normal"; maior que 6 letras, escreva "Seu nome é muito grande".
"""
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)
if tamanho_nome == '':
    print('digite pelo menos uma letra.')
if tamanho_nome <= 4:
    print('Seu nome é curto.')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
    