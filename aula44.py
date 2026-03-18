"""
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter - me entregue seu iterador
"""

texto = iter('Manuel')
iterador = iter(texto)
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# outra forma 
# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break
    
    # com for fica assim:
for letra in texto:
    print(letra)
