# usando o try except para tratar exceções
# int(12345)
# int(1563)
# int('ola mundo')  # ValueError

# numero_str = print("Digite um número para dobrar: ")

# numero_float = float(numero_str)

# print(f'O dobro de {numero_float} é {numero_float * 2}')

try:
    numero_str = input("Digite um número para dobrar: ")
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except ValueError:
    print(f'Ups! {numero_str} é um valor incorreto, digite um número válido.')
    