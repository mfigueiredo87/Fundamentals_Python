# while/else

string = 'Valor qualquer'


i = 0
while i < len(string):
    letra = string[i]
    
    # supondo que estou procurando o espaco e parar o while quando encontrar
    if letra == ' ':
        break
    
    print(letra)
    i += 1
else:
    print('Fim do while.')