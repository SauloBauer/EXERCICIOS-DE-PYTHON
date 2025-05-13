from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(1,3)
jogador = int(input('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=-'*20)
print('O computador escolheu {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*20)
if pc == 1: #JOGOU PEDRA
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    elif jogador == 3:
        print('VOCÊ PERDEU!')
    else:
        print('\033[1;31;40m OPÇÃO INVÁLIDA \033[m')
elif pc == 2: #JOGOU PAPEL
    if jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    else:
        print('\033[1;31;40m OPÇÃO INVÁLIDA \033[m')
elif pc == 3: #JOGOU TESOURA
    if jogador == 3:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('\033[1;31;40m OPÇÃO INVÁLIDA \033[m')