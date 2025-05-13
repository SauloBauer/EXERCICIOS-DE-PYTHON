num = int(input('Digite um número para ver sua tabuada: '))
cont = 0
for c in range(0, 11):
    cont = num * c
    print('{}  x {:2} = {}'.format(num, c, cont))

---------------------------------------------------------------------

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(0, 11):
    print('{}  x {:2} = {}'.format(num, c, num*c))