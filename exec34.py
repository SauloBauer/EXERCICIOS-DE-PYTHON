salario = int(input('Informe seu salário: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Parabéns! Seu salário anterior de R${:.2F} agpra passa a ser R${:.2F}'.format(salario, novo))