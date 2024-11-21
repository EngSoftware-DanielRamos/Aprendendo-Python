gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports, e que possibilita jogar localmente ou online
"""

print(gameName.upper()) # Retorar string em maiusculo
print(gameName.lower()) # Retornar string em minusculo
print(gameName.capitalize()) # Retornar string com a primeira letra em maiusculo e o resto em minusculo
print(gameName.title()) # Retornar string com a primeira letra de cada palavra em maiusculo e o resto em minusculo 
print(gameName.center(10, '-')) # Retorna a string centralizada com o tamanho de 10 e o caractere '-' como preenchimento
print(gameName.find("a")) # Retorna a posição da primeira ocorrência da string "i"
print(gameDescription.count("f")) # Conta a quantidade de ocorrências da string vazia
print(gameDescription.count("a")) # Conta a quantidade de ocorrências da string "a"
print(gameDescription.replace("Fifa", "Pes")) # Substitui a string "Fifa" pela string "Pes"
print(gameDescription.split(',')) # Divide a string em uma lista de strings, separadas pelo caractere ','