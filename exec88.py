from random import randint
from random import randint
from time import sleep

lista = []
jogos = []
print('-'*50)
print('              JOGA NA MEGA SENA')
print('-'*50)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-='*4, f"SORTEANDO {quantidade} JOGOS", '-=' * 3)

for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)

print("-="*5, "< Boa Sorte! >", "-="*5)