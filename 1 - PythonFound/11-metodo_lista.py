gamesList = ["Resident Evil 4", "Star Wars Jedi Survivor", "The Legend of Zelda", "Red Dead 2", "Mario Odyssey", "Luigis Mansion 3"]

# 1 - Tamanho da Lista
print(len(gamesList))

# 2 - Recuperar um item da lista pelo índice
print(gamesList.index("Mario Odyssey"))

# 3 - Adicionar item ao final da lista
gamesList.append("God of War")
print(gamesList)

# 4 - Ordernar a lista
gamesList.sort()
print(gamesList)

# 5 - Copiar  os itens da lista para outra lista
gameReset = gamesList.copy()
gameReset.remove("Star Wars Jedi Survivor")
print(gameReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)