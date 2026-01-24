# exercicio de if e comparacao
primeiro_valor = input("Digite um numero inteiro: ")
segundo_valor = input("Digite outro numero inteiro: ")
# comparando os valores
if primeiro_valor == segundo_valor:
    print("Os valores sao iguais.") 
else:
    print("Os valores sao diferentes.")
    # imprimindo o maior valor inserido
    if primeiro_valor > segundo_valor:
        print( f"O {primeiro_valor=} valor inserido é maior do que {segundo_valor=}")    
    else:
        print( f"O {segundo_valor=} valor inserido é maior do que {primeiro_valor=}")
        
