gameName = "Fifa 23"
gameDescription = """
FIFA 23 is a football simulation video game developed by EA Canada and published by EA Sports
"""

# string[inínio:fim] - índice começa na posição 0 / índice fim -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:7])

# 3 - Busque toda string a partir da terceira até a última posição
print(gameName[2:])

"""
string[inínio:fim:passo] - índice começa na posição 0 / índice fim -1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Busque toda a string de 2 em 2 caracteres 
print(gameName[::2])

# 5 - Busque toda a string nos índices ímpares
print(gameName[1::2])

# 6 - Inverter uma string de trás para frente
print(gameName[::-1])