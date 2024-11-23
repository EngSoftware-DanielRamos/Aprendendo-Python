import os

# 1 - Desligar o computador
# os.system("shutdown /s") # Desliga o computador em 60s
# os.system("shutdown /s /t 0") # Desligar o computador imediatamente
# os.system("shutdown now") - Linux

# 2 - Cancelar o desligamento
# os.system("shutdown /a") # Cancela o desligamento

def turn_off_one_hour():
    os.system("shutdown /s /t 3600") # Desliga o computador em 1h
    
def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800") # Desliga o computador em 30m
    
def cancel_shutdown():
    os.system("shutdown /a") # Cancela o desligamento
    
turn_off_one_hour()
cancel_shutdown()