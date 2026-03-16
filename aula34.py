# operadores de atribuica
"""
# = operador de atribuicao
# += operador de atribuicao de adicao
-= operador de atribuicao de subtracao
*= operador de atribuicao de multiplicacao
/= operador de atribuicao de divisao
//= operador de atribuicao de divisao inteira
**= operador de atribuicao de potencia
%= operador de atribuicao de modulo
# com exemplos praticos
x = 10      # atribui o valor 10 à variável x

x += 5      # x = x + 5  → resultado: 15

x -= 3      # x = x - 3  → resultado: 12

x *= 2      # x = x * 2  → resultado: 24

x /= 4      # x = x / 4  → resultado: 6.0

x //= 2     # x = x // 2 → resultado: 3.0 (divisão inteira)

x **= 2     # x = x ** 2 → resultado: 9.0 (potência)

x %= 4      # x = x % 4  → resto da divisão por 4, resultado: 1.0

"""
contador = 10
# contador += 1 # contador = contador + 1
# contador -= 1 # contador = contador - 1
# contador *= 2 # contador = contador * 2
# contador /= 2 # contador = contador / 2
# contador //= 2 # contador = contador // 2
# contador **= 2 # contador = contador ** 2
# contador %= 2 # contador = contador % 2
contador %=2

if contador == 0:
    print('O numero é par')
else:
    print('O numero é impar')
# print('Valor do contador: ',contador)
# usar numero com potencia
potencia = 2 ** 3
print('Valor da potencia: ',potencia)
# outra forma
potencia = pow(2,3)
print('Valor da potencia: ',potencia)

# outra forma 
potencia = 2
potencia **= 3
print('Valor da potencia: ',potencia)