# while dentro do while
linhas = 5
colunas = 5

linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(f' Quando estiver na: {linha=} - a coluna é: {coluna=}')
        coluna += 1
    linha += 1