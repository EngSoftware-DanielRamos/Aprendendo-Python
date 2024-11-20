name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrince = float(input("Digite o preço do jogo\n"))
planIncluded = input("Está incluso no serviço mensal\n")

print("###Dados do Jogo###")
print("===================")
# Alternativa 1
# print("Nome do Jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrince)
# print("Está incluido no plano?", planIncluded)

# Alternativa 2
# print("Nome do Jogo:", name, "\n Ano de Lançamento:", yearLaunch,
#       "\n Preço do Jogo:", gamePrince, "\n Está incluso no serviço mensal?", planIncluded)

# Alternativa 3
print(f"Nome do Jogo: {name} \nAno de Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrince} \nEstá incluso no serviço mensal? {planIncluded}")