# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(fname, Lname):
    print(f"Nome completo: {fname} {Lname}")
    
full_name("Daniel", "Ramos")

# 2 - Crie uma função que some dois números via parâmetros
def sum(a, b):
    return a + b

print(sum(10, 50))

# 3 - Argumentos default numa função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
    
address()
address("Canadá")

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo\n"))
        sum += note # sum = sum + note
    print(f"Média de avaliação do jogo {game_name} é: {sum / qtdRating}")

rating = int(int("Digite quantas avaliações deseja fazer no jogo\n"))
rating_game(2)