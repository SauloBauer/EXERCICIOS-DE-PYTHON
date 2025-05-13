from math import hypot
cateto1 = float(input('Comprimento do Cateto oposto: '))
cateto2 = float(input('Comprimento do Cateto adjacente: '))
hipotenusa = hypot(cateto1, cateto2)

print('A sua hipotenusa vai medir: {:.2f}'.format(hipotenusa))
