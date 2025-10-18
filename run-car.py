RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # localização do radar
RADAR_RANGE = 1 # alcance do radar

velocidade = 64 # velocidade do carro
local_carro = 99 # localização do carro

def velocidade_Carro():
    if velocidade > RADAR_1:
        print("Multado por excesso de velocidade!")



if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and \
   velocidade_Carro():
    print("Multado por passar no radar!")




