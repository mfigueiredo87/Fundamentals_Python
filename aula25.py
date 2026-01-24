# fatiamento de strings
variavel = 'Curso de Python'
print(variavel[0:5])  # 'Curso'
print(variavel[9:])   # 'Python'
print(variavel[:5])   # 'Curso'
print(variavel[::2])  # 'Crs dPto'
# usando o i:f:p
print(variavel[0:15:3])  # 'Cso yhn'
print(variavel[::-1])    # 'nohtyP ed osruC' (string invertida)
print(variavel[::-2])    # 'nhy dCr' (string invertida com passo 2)
print(variavel[5::-1])   # 'osruC' (fatiamento invertido do início até o índice 5)
print(variavel[-1::-1])  # 'nohtyP ed osruC' (string invertida usando índice negativo)
print(variavel[-1:0:-1]) # 'nohtyP ed osru' (string invertida do último caractere até o índice 1)
print(variavel[-5::-1])  # 'P yhtnoC ed osruC' (string invertida do índice -5 até o início)
print(variavel[-5:-1])   # 'Pyth' (fatiamento usando índices negativos)
print(variavel[-5:])     # 'Python' (fatiamento do índice -5 até o final)
print(variavel[:-5])     # 'Curso de ' (fatiamento do início até o índice -5)
print(variavel[-len(variavel):-10])  # 'Curs' (fatiamento usando comprimento da string)
print(variavel[-len(variavel):])      # 'Curso de Python' (fatiamento completo usando comprimento da string)
print(variavel[-len(variavel):-len(variavel)+5])  # 'Curso' (fatiamento usando comprimento da string)
print(variavel[::len(variavel)//3])  # 'C dP' (fatiamento com passo baseado no comprimento da string)
print(variavel[::-len(variavel)//4])  # 'nhtyP ed osruC' (string invertida com passo baseado no comprimento da string)
# funcao len()
print(len(variavel))  # 15
print(variavel[0:15:2])  # 'Crs d'