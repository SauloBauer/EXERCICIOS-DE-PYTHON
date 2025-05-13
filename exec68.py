from random import randint
print('-='*50)
print('VAMOS JOGAR PAR OU ÍMPAR')
cont = 0
while True:
    print('-=' * 50)
    valor = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = valor + computador
    r = ' '
    while r not in 'PI':
        r = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {valor} e o computador {computador}. O total é {total}.')
    print('=' * 50)
    if r == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    if r == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você ganhou {cont} vezes.')