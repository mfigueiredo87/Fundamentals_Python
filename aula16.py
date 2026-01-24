# aula sobre if e else

entrada = input("Voce quer entrar no jogo? (s/n): ")
if entrada.lower() == 's':
    print("Bem-vindo ao jogo!")
elif entrada.lower() == 'n':
    print("Que pena! Talvez na próxima vez.")
else:
    print("Saindo do jogo porque nao indicou valor algum.")
    
# verificando se a pessoa é maior ou menor de idade

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
# verificando se o numero é par ou impar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")