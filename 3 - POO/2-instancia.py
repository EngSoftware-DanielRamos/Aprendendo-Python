class Movie:
    name = ""
    yearLaunch = 0
    includePlan = False
    note = 0
    durationMinutes = 0
    
# Primeiro filme
movie = Movie()
movie.name = "Super Mario Bros"
movie.yearLaunch = 2023
movie.includePlan = False
movie.note = 5.0
movie.durationMinutes = 130

# Segundo filme
movie2 = Movie()
movie2.name = "The Lord of the Rings"
movie2.yearLaunch = 2022
movie2.includePlan = True
movie2.note = 6.0
movie2.durationMinutes = 120

movie2 = Movie()
print("Dados do Filme##")
print(f"Nome do filme: {movie.name} \n Ano de Lançamento {movie.yearLaunch}")