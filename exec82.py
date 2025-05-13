todos = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    todos.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'A lista completa é: {todos}')

if pares == []:
    print('Não houve números pares digitados')
else:
    print(f'A lista de pares é: {pares}')

if impares == []:
    print('Não houve números impares digitados')
else:
        print(f'A lista de impares é: {impares}')