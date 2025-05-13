numeros = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('valor não adicionado')

    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if continua == 'N':
        break
numeros.sort()
print(f'Os valores digitados foram os {numeros}')