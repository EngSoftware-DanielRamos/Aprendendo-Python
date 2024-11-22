gamesTuple = ("Fifa 23", "Red Dead 2", "Star Wars", "Mario Odyssey", "The Legend of Zelda")
print(gamesTuple)
print(type(gamesTuple))
# name = ("Daniel",)
# print(type(name))

# 1 - Buscar os dois primeiros elementos da tupla
print(gamesTuple[:2])

# 2 - Buscar o último elemento da tupla
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos a partir de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo índice
print(gamesTuple.index("Red Dead 2"))

# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla