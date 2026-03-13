# complexidade dos codigos e boas praticas

velocidade = 61 #velociddade atual do carro
local_carro = 101 #local onde o carro esta na estrada (km)

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

# if LOCAL_1 <= local_carro <= (LOCAL_1 + RADAR_RANGE):
#     if velocidade > RADAR_1:
#         print('MULTADO! Você excedeu o limite de velocidade')
#     else:
#         print('Não foi multado. Dirija com segurança!')
val_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
    
if val_carro_pass_radar_1:
        print('Velocidade do carro passou pelo radar 1'
              f'Valor: {val_carro_pass_radar_1}'
              f'Local: {carro_multado_radar_1}')
        if carro_multado_radar_1 and val_carro_pass_radar_1:
            if val_carro_pass_radar_1:
                print('MULTADO! Você excedeu o limite de velocidade')
            else:
                print('Não foi multado. Dirija com segurança!')
