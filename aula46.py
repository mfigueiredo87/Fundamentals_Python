"""
Faça um jogo para o usuario advinhar qual a palavra secreta. 
Você vai propor uma palavra secreta e o usuario vai tentar advinhar 
qual é a palavra digitando uma letra por vez. 
Quando o usuario digitar uma letra, você vai conferir se a letra 
digitada está na palavra secreta. 
Se a letra estiver na palavra secreta, você vai mostrar a letra na tela, 
no lugar correto. Se a letra não estiver na palavra secreta, 
você vai mostrar um aviso e vai contar quantas tentativas o usuario ainda tem. 
O jogo termina quando o usuario advinhar a palavra secreta ou quando ele não 
tiver mais tentativas.
"""
# importando o modulo para limpar a tela
import os

palavra_secreta = 'Manuel'
letras_acertadas = ''
numero_tentativas = 0

while True:
       
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    
    if letra_digitada in palavra_secreta:
        # print(f'Parabéns! A letra "{letra_digitada}" está na palavra secreta!')
        letras_acertadas += letra_digitada
    
    else:
        print(f'Ops! A letra "{letra_digitada}" não está na palavra secreta. Tente novamente!')
    
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
      if letra_secreta in letras_acertadas:
          palavra_formada += letra_secreta
        # print(letra_secreta, end=' ')
      else:
          palavra_formada += '*'
        # print('*')
    
    print(f'Palavra formada: {palavra_formada}')
    if palavra_formada == palavra_secreta:
        # limpar o terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Parabéns! Você acertou a palavra secreta!')
        print('A palavra secreta era: ', palavra_secreta)
        print('Número de tentativas: ', numero_tentativas)
        print('Fim de jogo!')       
        break
    