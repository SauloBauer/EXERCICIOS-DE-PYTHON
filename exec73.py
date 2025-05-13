times = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
         "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama",
         "Vitória", "Atlético Mineiro", "Fluminense", "Grêmio", "Juventude",
         "Red Bull Bragantino", "Athletico Paranaense", "Criciúma", "Atlético Goianiense", "Cuiabá")
print('='*50)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('='*50)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('='*50)
print(f'Times em ordem alfabetica {sorted(times)}')
print('='*50)
print(f'O time Flamengo está na {times.index("Flamengo") + 1}ª posição')