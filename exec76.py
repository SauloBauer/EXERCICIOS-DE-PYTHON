listagem = ("Arroz", 10.50, "Feijão", 8.30, "Macarrão", 5.20, "Carne", 32.90, "Leite", 4.80)
print('=-='*15)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('=-='*15)
for pos in range(0, len(listagem)):
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('=-='*15)