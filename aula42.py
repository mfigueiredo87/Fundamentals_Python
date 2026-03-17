# for / in

texto = 'Python'
for letra in texto:
    print(letra)
    
    # adicionar o * entre as letras
texto = 'Python'
resultado = ''
for letra in texto:
    resultado += f'*{letra}'
    print(letra)
print(resultado)