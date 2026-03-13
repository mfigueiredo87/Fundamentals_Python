"""
Flag (Bandeira) - Marcar um local
None = Nao valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True
# usando None
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faz algo')
else:
    print('Nao pode fazer nada.')

# exibindo o resultado do None, is not e is
# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)
# verificar 
if passou_no_if is None:
    print('Nao passou no if')

if passou_no_if is not None:
    print('Passou no if')
