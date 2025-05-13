maior = 0
menor = 0
for pessoas in range (1,6):
    peso = float(input('Peso da {}º pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso registrado foi {}Kg'.format(maior))
print('O menor peso registrado foi {}Kg'.format(menor))
