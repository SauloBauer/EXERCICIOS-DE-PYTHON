from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1,8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Foram registradas {} pessoas maiores de idade e {} menores!'.format(maior, menor))

