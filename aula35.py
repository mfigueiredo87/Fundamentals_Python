# while continue

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('Nao vou mostrar o: ', contador)
        continue
    
    # ocultar numeros de 20 a 30
    if contador >= 20 and contador <= 30:
        print('Nao mostrar o: ', contador)
        continue
    
    print('Contador: ',contador)
        
    if contador == 50:
        print('Contador atingiu o valor 50, saindo do loop...')
        break
    
    # if contador and contador % 2 == 0: