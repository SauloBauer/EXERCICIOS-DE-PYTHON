dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos Km o carro percorreu? '))
valordias = dias * 60
valorkm = km * 0.15
resultado = valorkm + valordias
print('Você deverá pagar R${} pelos dias alugados e R${:.2f} pelos KM rodados, totalizando R${:.2f}!'.format(valordias, valorkm, resultado))

#tambem poderia ser: pago = (dias * 60) + (km * 0,15)
#depois só era preciso printar o PAGO, mas a mensagem final ficaria só o total!