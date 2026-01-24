# not
senha = input('Senha: ')
senha_correta = '12345'
if not senha == senha_correta:
    print('Acesso negado!')
else:
    print('Acesso permitido')
    
    # outra forma 
senha = input('Senha: ')
senha_correta = '12345'
if not senha:
    print('Nao digitou nada!')
else:
    print('Acesso permitido')
    
    # outra forma 
senha = input('Senha: ')
senha_correta = '12345'
if senha != senha_correta:
    print('Acesso negado!')
else:
    print('Acesso permitido')
    