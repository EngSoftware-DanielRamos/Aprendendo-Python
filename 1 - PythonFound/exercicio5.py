# Verificação Letra Maiúscula e Minúscula 
def check_char(text):
    type ={"Uppercase": 0, "Lowercase":0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
print("Texto original:", text)
print("Letras Maiúsculas:", type["Uppercase"])
print("Letras Minúsculas:", type["Lowercase"])

check_char("A melhor forma de Prever o Futuro é Criá-lo")