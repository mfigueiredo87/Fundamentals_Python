# empacotamento e desempacotamento

lista = ['Manuel', 'Adameire', 'Audrey', 'Armando']

# desempacotar
# nome1, nome2, nome3, nome4, nome5 = ['Manuel', 'Adameire', 'Audrey', 'Armando']

# pegando apenas o primeiro valor e ignorar o resto
nome2, *resto = ['Manuel', 'Adameire', 'Audrey', 'Armando']

# em vez de usar a variavel resto, usar o _
nome1, *_ = ['Figas', 'Adameire', 'Audrey', 'Armando']
print('Primeiro nome: ',nome1)
print(_)
# para pular o primeiro valor da lista usamos o _ antes
_, _, nome3, *_ = ['Figas', 'Adameire', 'Audrey', 'Armando']
print('Terceiro nome: ',nome3)