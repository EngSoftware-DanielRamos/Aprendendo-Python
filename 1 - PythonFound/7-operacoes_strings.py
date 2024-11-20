gameDescription = """
FIFA 23 is a football simulation video game developed by EA Canada and published by EA Sports
"""
gameName = "Fifa"
gameVersion = "23"
line = "="

# 1 - Operação de Concatenação de Strings
print(line * 25)
gameFullName = gameName + " " + gameVersion
print(gameFullName)

# 2 - Operação de multiplicação de Strings
print(line * 25)

# 3 - Procura palavra dentro de um texto
print("FIFA" in gameDescription)
print("football" in gameDescription)