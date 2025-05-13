p = 'S'
soma = cont = media = maior = menor = 0
while p in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = str(input('Deseja continuar? [S/N]: ')).strip().upper()

media = soma / cont
print('''Você digitou {} números e a média entre eles foi {:.1F}, 
O maior número entre eles foi {} e o menor foi {}'''.format(cont, media, maior, menor))
