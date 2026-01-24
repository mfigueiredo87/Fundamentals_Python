# operadores logicos: and, or, not
# operador and: todas as condicoes devem ser verdadeiras
condicao1 = True
condicao2 = True
if condicao1 and condicao2:
    print("As duas condicoes sao verdadeiras")  
else:
    print("Uma ou ambas as condicoes sao falsas")
    
    # simulando um sistema de login
usuario_cadastrado = "admin"
senha_cadastrada = "12345"
usuario_input = input("Digite o nome de usuario: ")
senha_input = input("Digite a senha: ")
if usuario_input == usuario_cadastrado and senha_input == senha_cadastrada:
    print("Login bem-sucedido!")
else:
    print("Nome de usuario ou senha incorretos.")
    
    if 0 and 1:
        print("True com 0 and 1")