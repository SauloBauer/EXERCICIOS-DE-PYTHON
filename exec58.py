from random import randint
from time import sleep
count = 0
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
sleep(3)

computador = randint (0,5)
jogador = int(input('Em que número pensei? '))
print('Processando...')

sleep(3)

while jogador != computador:
    print('Errou, Eu pensei no {}'.format(computador))
    sleep(1)
    computador = randint(0, 5)
    jogador = int(input('Tente novamente, em que número pensei? '))
    print('Processando...')
    count += 1
    sleep(3)

if jogador == computador:
    print('PARABÉNS! Você ganhou, tambem pensei no {}. Acertou com {} tentativas!'.format(computador, count))
