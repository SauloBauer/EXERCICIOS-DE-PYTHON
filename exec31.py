viagem = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(viagem))
preco = viagem * 0.50
promo = viagem * 0.45
if viagem <= 200:
    print('E o preço da sua viagem será de R${:.2f}'.format(preco))
else:
    print('E o preço da sua viagem será de R${:.2f}'.format(promo))
