# entrada = input('[E]ntrada [S]air: ')
# senha = input('Senha: ')

# senha_correta = '12345'

# if (entrada == 'E' or entrada == 'e') and senha == senha_correta:
#         print('Acesso permitido')
# else:
#         print('Acesso negado!')

# avaliacao do curto circuito
print(True or False)  # True
print(False and True)  # False
print(False or (True and False))  # False
print((False or True) and False)  # False
print(not False or True)  # True
print(not (False or True))  # False