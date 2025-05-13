from time import sleep
cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    cont += 1
    print('-='*50)
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-=' * 50)
    sleep(3)

print(f'Você solicitou {cont} tabuadas')
print('PROGRAMA ENCERRADO, VOLTE SEMPRE!')