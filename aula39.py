# calculcadora dois

""" Calculadora com while """

while True:
    # entrada de dados
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    # validação de dados
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        # tenta converter as entradas para float
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    # se a conversão falhar, numeros_validos permanece None. ou seja, os números são inválidos. devem ser apenas números, sem letras ou caracteres especiais.
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    # permite apenas os operadores +, -, /, *
    operadores_permitidos = '+-/*'

    # verifica se o operador digitado está na string de operadores permitidos. se não estiver, o operador é inválido.
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    # verifica se o operador tem mais de um caractere. se tiver, o operador é inválido. deve ser apenas um caractere, sem espaços ou outros caracteres.
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    print('Realizando cálculos...')
    # cálculos
    if operador == '+':
       print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    elif operador == '/':
        # print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
        # # verifica se o segundo número é zero. se for, a divisão é inválida. não é possível dividir por zero.
        if num_2_float == 0:
            print('Divisão por zero é inválida.')
            continue
        resultado = num_1_float / num_2_float
        print(f'Resultado: {resultado}')
    else:
        print('Operação inválida.') 

# pergunta para sair do programa. se o usuário digitar 's' ou 'S', o programa termina. caso contrário, o programa continua executando.
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break