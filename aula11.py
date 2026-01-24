# precedencia entre variaveis 
# ordem de resolucao de operacoes
# 1 - parenteses (1+1)
# 2 - exponenciacao (**)
# 3 - multiplicacao e divisao (*, /, //, %)
# 4 - adicao e subtracao (+, -)


conta = (2 + int(0.5 +0.5)) ** (2+2)
conta = "Valor da conta é: " + str(conta)
print(conta)
print("Conta sem parenteses:", conta)