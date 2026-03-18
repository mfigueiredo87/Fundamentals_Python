# sando range
# range(start, stop, step)
# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Aqui o start é 0, o stop é 10 e o step é 1 (padrão)
# range(1, 10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9. Aqui o start é 1, o stop é 10 e o step é 1 (padrão)
# range(1, 10, 2) -> 1, 3, 5, 7, 9. Aqui pula de 2 em 2


numeros = range(0, 10, 2)
for numero in numeros:
    print(numero)
    
# pegar os multiplos de 8 usando o range
multiplos = range(0,100,8)
for multiplo in multiplos:
    print(f'Os multiplos de 8 sao: {multiplo}')
    