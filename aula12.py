# calculo do IMC
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
imc_formatado = "{:.2f}".format(imc)
print(f"{nome}, seu IMC é: {imc_formatado}")
print("Cálculo do IMC concluído.")


# outra forma
nome = "Manuel Pedro"
peso = 85
altura = 1.80
imc = peso / (altura ** 2)
imc_formatado = "{:.2f}".format(imc)    
print(f"{nome}, seu IMC é: {imc_formatado}")
print("Cálculo do IMC concluído.")