real = float(input('Digite qual valor você tem em reais: R$'))
dolar = real / 4.97
euro = real / 5.43
print('Com R${:.2f} voce pode comprar ${:.2f} dolares e €{:.2f} euros'.format(real, dolar, euro))
