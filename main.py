import time
import sys

def set_time(tempo):
    min, secs = divmod(tempo,60)
    timer = '{:2d}:{:2d}'.format(min,secs)
    time.sleep(1)
    tempo-=1


# tempos pré-definidos (1 min, 3 min, 5 min)
tempos_pre_definidos = {
    "1 minuto":60,
    "3 minutos":180,
    "5 minutos":300
    }

def sair():
    sys.exit()