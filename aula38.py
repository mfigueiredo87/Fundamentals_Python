# calculadora com while a partir de dois numeros

# calculadora com while a partir de dois numeros

tentativas_nome = 0

while tentativas_nome < 3:
    nome = input('Digite seu nome: ')

    if nome == 'Manuel':
        print('Bem-vindo, Manuel!')
        break
    else:
        tentativas_nome += 1
        print('Nome incorreto!')

if tentativas_nome == 3:
    print('Nome incorreto, acesso negado!')
else:
    # verificação da senha
    tentativas_senha = 0

    while tentativas_senha < 3:
        senha = input('Digite a senha: ')

        if senha == 'figueiredo':
            print('Senha correta, acesso concedido!')
            print('Vamos usar a calculadora, Manuel!')
            break
        else:
            tentativas_senha += 1
            print('Senha incorreta!')

    if tentativas_senha == 3:
        print('Senha incorreta, acesso negado!')
    else:
        while True:
            # codigo da calculadora
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            operacao = input('Digite a operação (+, -, *, /): ')

            if operacao == '+':
                resultado = num1 + num2
                tipo_operacao = 'soma'

            elif operacao == '-':
                resultado = num1 - num2
                tipo_operacao = 'subtração'

            elif operacao == '*':
                resultado = num1 * num2
                tipo_operacao = 'multiplicação'

            elif operacao == '/':
                resultado = num1 / num2
                tipo_operacao = 'divisão'

            else:
                print('Operação inválida!')
                continue

            print(f'A {tipo_operacao} de {num1} e {num2} tem como resultado: {resultado}')

            sair = input('Deseja sair? (s/n) ').lower().startswith('s')

            if sair:
                print('Programa terminado com sucesso...')
                break

    # sair = input('Deseja sair? (s/n) ')
    # sair = sair.lower()  # Convertendo a resposta para minúscula para evitar problemas de case sensitivity
    # # verificar se a telca digitada comecou com s
    # sair = sair.startswith('s') # verificar se a resposta comecou com a letra s, independente de ser maiuscula ou minuscula. aqui devolve True ou False
    # # outra forma de fazer tudo isso
    # sair = input('Deseja sair? (s/n) ').lower().startswith('s') # tudo em uma linha, sem necessidade de criar variaveis intermediarias
    # terminar o programa se a resposta comecar com a letra s
    
    
    # if sair == 's':
    #     print('Programa terminado com sucesso...')
    #     break