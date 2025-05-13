numeros = []

while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Você digitou {len(numeros)} numeros')#len, determina quantos do que voce colocou entre parenteses
numeros.sort(reverse=True)
print(f'Os números digitados foram {numeros}')
if 5 not in numeros:
    print('Não encontrei o valor 5')
else:
    print('O valor 5 foi Digitado!')
