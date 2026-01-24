# exercicio aula26.py
# pedir o nome  completo do usuario e depois a idade.
# Depois se o nome e a idade forem digitaos correctamente, mostrar o nome e a idede,
# caso contrario, mostrar uma mensagem de erro
# mostrar o nome do usuario na forma invertida
# mostrar se nome contem ou nao espacos
# mostrar quantas letras te o nome
# mostrar a primeira letra do nome
# mostrar a ultima letra do nome
# se nada for digitado, mostrar uma mensagem de erro: Desculpa, voce nao digitou nada
nome = input("Digite seu nome completo: ").strip()
idade = input("Digite sua idade: ").strip()
if nome and idade:
    print(f"Nome: {nome}, Idade: {idade}")
    print(f"Nome invertido: {nome[::-1]}")
    if ' ' in nome:
        print("Contem espacos: Sim")
    else:
        print("Contem espacos: Nao")
    # print(f"Contem espacos: {' ' in nome}")
    print(f"Quantidade de letras no nome: {len(nome)}")
    print(f"Quantidade de numeros na idade: {len(idade)}")
    print(f"Primeira letra do nome: {nome[0]}")
    print(f"Ultima letra do nome: {nome[-1]}")
else:
    print("Desculpe,Voce deixou campos vazios.")
    
