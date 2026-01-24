# formatando strings
a = 'Angola'
b = 'Fica na África'
c = 'na costa ocidental'
formato = 'a = {}, b = {}, c = {}'.format(a, b, c)
print(formato)
# pegar os valores por indice
formato2 = 'b = {1}, c = {2}, a = {0}'.format(a, b, c)
print(formato2)
# usando parametro nomeado
formato3 = 'c = {pais3}, a = {pais1}, b = {pais2}'.format(pais1=a, pais2=b, pais3=c)
print(formato3)
# misturando paramentros posicionais e nomeados
formato4 = 'c = {2}, a = {pais1}, b = {pais2}'.format(a, b, c, pais1=a, pais2=b)
print('Misturando os valores: ',formato4)

nome = "João"
idade = 25
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))